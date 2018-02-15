# Generated by Django 2.0.2 on 2018-02-15 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180213_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('cast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='potential_cast', to='accounts.Cast')),
                ('crew', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='potential_crew', to='accounts.Crew')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='accounts.Project')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]