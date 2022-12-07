from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers



class HelloView(APIView):
    """test api views"""
    serializer_class = serializers.HelloSerializer
    def get(self, request,format=None):
        """return list of api views feature""" 
        
        
        an_api_view = [
        "usee https methods",
        "is similar to traditional django views",
        "gives you access most applicsation ",
        "is mapped to urls"
        ]
        return Response({'message':"hello!",'an_apiview':an_api_view})
        
    def post(self, request):
        """create a new api view"""
        serializer=self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message = f'your response {name}'
            return Response({'message':message})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
                
    def put(self, request,pk=None):
        """update a new api view"""
        return Response({'method':'PUT'})
        
    def patch(self, request,pk=None):
        """update a new api view"""
        return Response({'method':'PATCH'})
    def delete(self, request,pk=None):
        """update a new api view"""
        return Response({'method':'DELETE'})
        
class HelloViewSet(viewsets.ViewSet):
    """test view set"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """list views"""
        an_view_set = [
        "usee name like list methods",
        "is similar to traditional django views",
        "gives you access more  ",
        "is mapped to urls"
        ]
        return Response({'message':"hello!",'an_apiview':an_view_set})
        
    def create(self,request):
        """create a new """
        serializer=self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name=serializer.validated_data.get('name')
            message = f'your response {name}'
            return Response({'message':message})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    def retrive(self,request):
        """retrieve"""
        return Response({'message':"get specific"})    
        
        
    def update(self,request):
        """retrieve"""
        return Response({'message':"get update"})    
        
    def partial_update(self,request):
        """update"""
        return Response({'message':"update"})    
        
        
    def destroy(self,request):
        """update"""
        return Response({'message':"delete"})    