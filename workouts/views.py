from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from workouts.models import Workout, Exercise
from workouts.serializers import WorkoutSerializer, ExerciseSerializer


class WorkoutAPIView(APIView):
    def get(self, request):
        workouts = Workout.objects.all()
        return Response({'workouts': WorkoutSerializer(workouts, many=True).data})

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'workouts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'No pk'})

        try:
            instance = Workout.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = WorkoutSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'workouts': serializer.data})


class ExerciseAPIView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
