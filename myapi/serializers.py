from rest_framework import serializers

from .models import Shelter

class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelter
        fields = ('id', 'name', 'address', 'service', 'hours', 'contact')
        
        
# https://www.django-rest-framework.org/tutorial/quickstart/#serializers