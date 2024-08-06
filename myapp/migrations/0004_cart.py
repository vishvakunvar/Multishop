# Generated by Django 5.0.3 on 2024-05-20 11:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_top_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
