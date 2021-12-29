from rest_framework import serializers

from .models import Drone, Medication, Command, Transaction


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ('serialNumber', 'model','weightLimit','batteryCapacity','state')

class CommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Command
        fields = ('drone','medication')



class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication
        fields = ('code', 'name','weight','image')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transactionId','achieved','command')


