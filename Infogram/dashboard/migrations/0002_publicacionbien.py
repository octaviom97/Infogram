# Generated by Django 3.0.6 on 2020-05-14 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicacionBien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(max_length=350, upload_to='imgs/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pubs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]