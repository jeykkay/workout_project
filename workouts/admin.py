from django.contrib import admin

from workouts.models import Workout, Exercise, WorkoutSession


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('type_workout', 'date', )


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'muscle_group', )


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'duration', )
