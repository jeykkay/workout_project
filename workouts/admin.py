from django.contrib import admin

from workouts.models import Workout, Exercise, TrainingPlan, TrainingLog, DietPlan


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', )


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'muscle_group', )


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', )


@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', )


admin.site.register(TrainingLog)
