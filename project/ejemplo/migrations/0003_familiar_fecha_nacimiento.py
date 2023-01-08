from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]