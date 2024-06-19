# Generated by Django 5.0.6 on 2024-06-19 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_faqsmodel_role_alter_feedbackmodel_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='comment.service'),
        ),
    ]
