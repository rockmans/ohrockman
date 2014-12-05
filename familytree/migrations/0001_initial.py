# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preferred_name', models.CharField(max_length=50, blank=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50)),
                ('maiden_name', models.CharField(max_length=50, blank=True)),
                ('ordinal', models.CharField(max_length=50, blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('step_child', models.BooleanField(default=False)),
                ('string_birth_date', models.CharField(max_length=120, verbose_name=b'String Birth Date', blank=True)),
                ('date_birth_date', models.DateField(null=True, verbose_name=b'Birth Date', blank=True)),
                ('birth_city', models.CharField(max_length=120, blank=True)),
                ('birth_state', models.CharField(max_length=120, blank=True)),
                ('birth_country', models.CharField(max_length=120, blank=True)),
                ('string_death_date', models.CharField(max_length=120, verbose_name=b'String Death Date', blank=True)),
                ('date_death_date', models.DateField(null=True, verbose_name=b'Death Date', blank=True)),
                ('death_city', models.CharField(max_length=120, blank=True)),
                ('death_state', models.CharField(max_length=120, blank=True)),
                ('death_country', models.CharField(max_length=120, blank=True)),
                ('bio', models.TextField(blank=True)),
                ('picture', models.CharField(max_length=50, blank=True)),
                ('children', models.ManyToManyField(related_name='c', null=True, to='familytree.FamilyMember', blank=True)),
                ('parents', models.ManyToManyField(related_name='p', null=True, to='familytree.FamilyMember', blank=True)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
                'verbose_name': 'Family Member',
                'verbose_name_plural': 'Family Members',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string_marriage_date', models.CharField(max_length=120, verbose_name=b'String Marriage Date', blank=True)),
                ('date_marriage_date', models.DateField(null=True, verbose_name=b'Marriage Date', blank=True)),
                ('marriage_city', models.CharField(max_length=120, blank=True)),
                ('marriage_state', models.CharField(max_length=120, blank=True)),
                ('marriage_country', models.CharField(max_length=120, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('descendant', models.ForeignKey(related_name='descendant', to='familytree.FamilyMember')),
                ('in_law', models.ForeignKey(related_name='in_law', to='familytree.FamilyMember')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
