# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_event_comlete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='comlete',
            new_name='complete',
        ),
    ]
