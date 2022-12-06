from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    """test api views"""
    def get(self, request,format=None):
        """return list of api views feature""" 
        an_api_view = [
        "usee https methods",
        "is similar to traditional django views",
        "gives you access most applicsation ",
        "is mapped to urls"
        ]
        return Response({'message':"hello!",'an_apiview':an_api_view})