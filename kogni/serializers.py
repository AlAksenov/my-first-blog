from django.core import serializers
from .models import scenariy

class scenariySerializer(serializers.ModelSerializer):

    class Meta:
        model = scenariy
        #field =('id', 'ticker', 'image', 'file', 'description')
        fields ='__all__'
