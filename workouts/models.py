from django.db import models

from users.models import Trainer, CustomUser


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Workout(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    type_workout = models.CharField(max_length=100)
    description = models.TextField()
    exercise = models.ManyToManyField(Exercise)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type_workout


class WorkoutSession(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return f'{self.client.user.username} - {self.workout.title}'
