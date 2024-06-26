# Generated by Django 5.0.4 on 2024-04-16 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('question_count', models.IntegerField()),
                ('title', models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Answer Title')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='polls.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='polls.quizzes'),
        ),
    ]
