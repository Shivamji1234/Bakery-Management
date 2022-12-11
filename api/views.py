from django.contrib.auth import get_user_model
from rest_framework import viewsets
from api.models import bakery,customer
from api.serializers import BakeryAdmin,CustomerSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):    

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()



# Create your views here
class BakeryViewSet(viewsets.ModelViewSet):
    queryset=bakery.objects.all()
    serializer_class=BakeryAdmin
    
#Create registration...
class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({'status': 403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj,_=Token.objects.get_or_create(user=user)
        return Response({'status': 200,'payload':serializer.data,'token':str(token_obj),'message':'your are now register'})
        

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=customer.objects.all()
    serializer_class=CustomerSerializer
    
 
        
       
    
        

