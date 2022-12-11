from rest_framework import serializers
from api.models import bakery,customer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username','password']
        
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    

#Creating serializer for admin
class BakeryAdmin(serializers.HyperlinkedModelSerializer):
    bakery_id=serializers.ReadOnlyField()
    class Meta:
        model=bakery
        fields="__all__"
        
#Creating serializer for customer
class CustomerSerializer(serializers.ModelSerializer):
    customer_id=serializers.ReadOnlyField()
    class Meta:
        model=customer
        fields="__all__"        
        

        
    
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    pass