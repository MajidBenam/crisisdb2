# Generated by Django 4.0 on 2022-01-13 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book Genre Please...', max_length=200)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='owner_real',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.importantperson'),
        ),
    ]
