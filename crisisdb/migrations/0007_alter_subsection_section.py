# Generated by Django 4.0 on 2022-02-17 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0006_rename_sect_subsection_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsections', to='crisisdb.section'),
        ),
    ]
