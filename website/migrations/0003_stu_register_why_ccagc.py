# Generated by Django 4.0.4 on 2022-05-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_stu_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_register',
            name='why_ccagc',
            field=models.CharField(choices=[('None', 'None'), ('Placements', 'Placements'), ('Higher Studies', 'Higher Studies'), ('Enterpreneurship', 'Enterpreneurship'), ('Other', 'Other')], default='None', max_length=50, verbose_name='You are looking Career counselling and Guidance for'),
        ),
    ]
