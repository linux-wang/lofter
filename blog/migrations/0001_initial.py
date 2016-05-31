# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='\u6587\u7ae0\u9898\u76ee', max_length=50, verbose_name=b'title')),
                ('author', models.CharField(default='wswang', help_text='\u6587\u7ae0\u4f5c\u8005', max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name=b'create time')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name=b'update time')),
                ('abstract', models.CharField(help_text='\u6587\u7ae0\u6458\u8981', max_length=255)),
                ('content', models.TextField(help_text=b'content', verbose_name=b'content')),
                ('tags', models.CharField(help_text=b'tags', max_length=30, null=True, verbose_name=b'tags')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u7c7b\u522b\u540d\u79f0', max_length=255)),
                ('alias', models.CharField(help_text='\u82f1\u6587\u522b\u540d', max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name=b'create time')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name=b'update time')),
            ],
            options={
                'verbose_name': 'category',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(help_text='\u5206\u7c7b', to='blog.Category'),
        ),
    ]
