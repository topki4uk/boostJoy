# Generated by Django 4.2.1 on 2023-06-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_doc_comments'),
        ('accounts', '0008_alter_user_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, to='app.doc'),
        ),
    ]