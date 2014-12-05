echo $WORKSPACE
export PROJECT_NAME=ohrockman
export APP_VERSION=`git rev-parse HEAD | cut -c -12`
export VENV_VERSION=`sha1sum ./requirements.txt | cut -c -12`
export ROOT="/usr/local/$PROJECT_NAME"
export APP_DIR="$ROOT/app_versions/$APP_VERSION"
export VENV_DIR="$ROOT/venv_versions/$VENV_VERSION"
export TEST_APP_DIR="$ROOT/app_test"
export ACTIVE_APP_DIR="$ROOT/app_$APP_ENV"
export ACTIVE_VENV_DIR="$ROOT/app_venv_$APP_ENV"
export MEDIA_DIR="$ROOT/media"
export DB_DIR="$ROOT/db_$APP_ENV"

mkdir -p "$MEDIA_DIR"
mkdir -p "$DB_DIR"

if [[ ! -e "$APP_DIR" ]]
then
  mkdir -p "$APP_DIR"
  cp -rv "./." "$APP_DIR"
fi

if [[ ! -e "$VENV_DIR/bin/activate" ]]
then
  virtualenv "$VENV_DIR"
  . "$VENV_DIR/bin/activate"
  pip install -r "./requirements.txt"
else
  . "$VENV_DIR/bin/activate"
fi

# Smoketest
ln -snf "$APP_DIR" "$TEST_APP_DIR"
# uwsgi smoke test command goes here

ln -snf "$APP_DIR" "$ACTIVE_APP_DIR"
ln -snf "$VENV_DIR" "$ACTIVE_VENV_DIR"

cd "$ACTIVE_APP_DIR"
if [[ ! -e "$DB_DIR/default.db" ]]
then
  python manage.py migrate --noinput || true
  python manage.py migrate --database="photos" --noinput || true
  python manage.py migrate --noinput
  python manage.py migrate --database="familytree" --noinput
  python manage.py loaddata backup_2014_12_05.json --database="familytree"
  python manage.py migrate --noinput
else:
  python manage.py migrate --noinput
  python manage.py migrate --database="photos" --noinput
  python manage.py migrate --database="familytree" --noinput
fi
python manage.py collectstatic --noinput

cp -f "$WORKSPACE/jenkins/nginx.conf" "/etc/nginx/sites-enabled/$PROJECT_NAME.conf"
cp -f "$WORKSPACE/jenkins/uwsgi_$APP_ENV.ini" "/usr/local/uwsgi/confs/${PROJECT_NAME}_$APP_ENV.ini"
