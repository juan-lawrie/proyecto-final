from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajo_final', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
            ],
        ),
    ]