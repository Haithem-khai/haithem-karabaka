from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import DroneSerializer, CommandSerializer, MedicationSerializer, TransactionSerializer
from .models import Drone, Command, Transaction, Medication


class RegisterDrone(APIView):
    def post(self,request): # add some drone
        serialized = DroneSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({"status": "success", "data": serialized.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)


class CheckDroneBattery(APIView):
    def get(self,request,id=None):
        if(id):
            drone = Drone.objects.get(serialNumber = id)
            return Response({"status": "success", "batteryCapacity": drone.batteryCapacity}, status=status.HTTP_200_OK)
        pass

class CheckAvailableDrone(APIView):
    def get(self,request):
        drones = Drone.objects.all().filter(state='IDLE',batteryCapacity__gte = 24)
        serialized = DroneSerializer(drones,many=True)
        return Response({"status": "success", "data": serialized.data}, status=status.HTTP_200_OK)
        pass




class CheckLoadedMedication(APIView):
    def get(self,request,id=None):
        if (id):
            drone = Drone.objects.get(serialNumber=id)


            medications = Medication.objects.all().filter(command__drone=drone)#.filter(transaction__achieved=False)
            print(len(medications))
            serialized = MedicationSerializer(medications, many=True)
            return Response({"status": "success", "data": serialized.data}, status=status.HTTP_200_OK)
            pass

class LoadingDrone(APIView):
    def post(self, request):  # loading some drone
        serialized = TransactionSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({"status": "success", "data": serialized.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serialized.errors}, status=status.HTTP_400_BAD_REQUEST)