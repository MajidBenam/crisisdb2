# Generated by Django 4.0 on 2022-02-12 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agr_prod_pop',
            name='citations',
            field=models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', to='crisisdb.Citation'),
        ),
        migrations.AlterField(
            model_name='agr_prod_pop',
            name='tag',
            field=models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5),
        ),
        migrations.AlterField(
            model_name='rulertransition',
            name='citations',
            field=models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', to='crisisdb.Citation'),
        ),
        migrations.CreateModel(
            name='Majid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('my_total_population', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', to='crisisdb.Citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crisisdb.polity')),
                ('section', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crisisdb.section')),
                ('subsection', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crisisdb.subsection')),
            ],
            options={
                'ordering': ['polity'],
                'abstract': False,
            },
        ),
    ]
