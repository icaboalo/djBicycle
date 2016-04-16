from rest_framework import serializers
from bicycle.models import *

#---------DEFAULT---------#
#Bicycle serializer
class DefaultBicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = ['id', 'brand', 'model', 'track', 'color', 'year', 'latitude', 'longitude']
