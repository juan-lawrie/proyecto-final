from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajo_final', '0004_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]