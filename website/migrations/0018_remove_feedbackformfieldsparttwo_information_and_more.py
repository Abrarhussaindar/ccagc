# Generated by Django 4.0.4 on 2022-06-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_feedbackformfieldsparttwo_beneficial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='Information',
        ),
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='address_my_concerns',
        ),
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='examine_my_alternatives',
        ),
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='genuine_interest',
        ),
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='knowledgeable',
        ),
        migrations.RemoveField(
            model_name='feedbackformfieldsparttwo',
            name='valuable',
        ),
    ]
