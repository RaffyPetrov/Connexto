from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        # Ensure the 'cars' app migration is applied first
        ('cars', '0001_initial'),
    ]

    operations = [
        # No operations are required here if only creating the initial model
    ]
