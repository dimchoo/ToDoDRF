from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from users.models import UserDRF


class Project(models.Model):
    name = models.CharField('Название', max_length=32, unique=True)
    repo_link = models.URLField('Репозиторий', max_length=255, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    created_by = models.ForeignKey(
        UserDRF,
        verbose_name='Создатель',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='created_projects'
    )
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectUser(models.Model):
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(UserDRF, verbose_name='Юзер', on_delete=models.CASCADE, related_name='project_users')

    def __str__(self):
        return f'{self.user}. {self.project}'


class TaskStatus(models.Model):
    name = models.CharField('Название', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус задач'
        verbose_name_plural = 'Статусы задач'


class Task(models.Model):
    name = models.CharField('Название', max_length=62, unique=True)
    project = models.ForeignKey(
        Project,
        verbose_name='Проект',
        null=True,
        blank=True, on_delete=models.CASCADE,
        related_name='tasks'
    )
    description = models.TextField('Описание', null=True, blank=True)
    created_by = models.ForeignKey(
        UserDRF,
        verbose_name='Инициатор',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='created_tasks'
    )
    users = models.ManyToManyField(ProjectUser, verbose_name='Пользователи', related_name='tasks', null=True, blank=True)
    status = models.ForeignKey(TaskStatus, verbose_name='Статус', null=True, blank=True, on_delete=models.SET_NULL)
    deadline = models.DateField('Срок', null=True, blank=True)
    color_code = models.CharField('Цвет', max_length=6, null=True, blank=True)
    created = models.DateTimeField('Создана', auto_now_add=True)
    updated = models.DateTimeField('Обновлена', auto_now=True)
    is_active = models.BooleanField('Активна', default=True)

    def save(self, *args, **kwargs):
        if self.deadline and self.deadline < timezone.now().date:
            raise ValidationError('The date cannot be in the past!')
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
