from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajo_final', '0002_websitesetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=3000)),
                ('enviado_el', models.DateField(auto_now_add=True)),
            ],
        ),
    ]