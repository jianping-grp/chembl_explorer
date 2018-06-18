# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chembl', '0001_initial'),
        ('phin', '0020_auto_20180115_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoleculeHierarchy',
            fields=[
                ('molregno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='phin_hierarchy', serialize=False, to='chembl.MoleculeDictionary')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chembl.MoleculeDictionary')),
            ],
        ),
        migrations.AlterField(
            model_name='molecule',
            name='molregno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phin_molecule', to='chembl.MoleculeDictionary'),
        ),
        migrations.AlterField(
            model_name='target',
            name='tid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phin_target', to='chembl.TargetDictionary'),
        ),
    ]