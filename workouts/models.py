from django.db import models

from users.models import Trainer, CustomUser


class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название упражнения')
    description = models.TextField(verbose_name='Описание упражнения')
    muscle_group = models.CharField(max_length=100, verbose_name='Группа мышц')

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name


class Workout(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название тренировки')
    description = models.TextField(verbose_name='Описание тренировки')
    exercise = models.ManyToManyField(Exercise, verbose_name='Упражнения')
    duration = models.DurationField(verbose_name='Продолжительность тренировки')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return self.name


class TrainingPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название плана тренировок')
    description = models.TextField(verbose_name='Описание плана тренировок')
    workouts = models.ManyToManyField(Workout, verbose_name='Тренировки в плане')
    start_date = models.DateField(verbose_name='Дата начала выполнения')
    end_date = models.DateField(verbose_name='Дата окончания выполнения')

    class Meta:
        verbose_name = 'План тренировки'
        verbose_name_plural = 'План тренировок'

    def __str__(self):
        return self.name


class TrainingLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, verbose_name='Тренировка')
    date_completed = models.DateField(verbose_name='Дата выполнения')
    notes = models.TextField(null=True, blank=True, verbose_name='Заметки')

    class Meta:
        verbose_name = 'Журнал тренировки'
        verbose_name_plural = 'Журнал тренировок'

    def __str__(self):
        return f"{self.workout} - {self.notes}"


class DietPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название плана питания')
    description = models.TextField(verbose_name='Описание плана питания')
    start_date = models.DateField(verbose_name='Дата начала выполнения')
    end_date = models.DateField(verbose_name='Дата окончания выполнения')

    class Meta:
        verbose_name = 'План питания'
        verbose_name_plural = 'План питания'

    def __str__(self):
        return self.name
