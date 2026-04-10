from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True) 

    class Meta : 
        model =CustomUser
        fields = '__all__'
        