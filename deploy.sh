echo $WORKSPACE
export PROJECT_NAME=ohrockman
export VENV_ROOT=/Users/zoeserver/.virtualenvs/${PROJECT_NAME}/
export WEB_ROOT=/Volumes/STORAGE/Web/${PROJECT_NAME}

rm -rvf ${WEB_ROOT}
mkdir ${WEB_ROOT}
cp -rv ./* ${WEB_ROOT}
cd ${WEB_ROOT}

ln -s ${VENV_ROOT} ./.virtualenv
. ./.virtualenv/bin/activate
pip install --upgrade -r ./requirements.txt
rm -f /usr/local/etc/uwsgi/apps/${PROJECT_NAME}.ini
mv ./wsgi.ini /usr/local/etc/uwsgi/apps/${PROJECT_NAME}.ini

python manage.py collectstatic --noinput