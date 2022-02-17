# Generated by Django 4.0 on 2022-02-17 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0007_alter_subsection_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='country',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='crisisdb.polity'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
