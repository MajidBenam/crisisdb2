# Generated by Django 4.0 on 2022-02-16 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0005_alter_agr_prod_pop_section_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsection',
            old_name='sect',
            new_name='section',
        ),
    ]
