from django.shortcuts import render
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import *
# Create your views here.

class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        recipe = [ {"name": recipe.name, "recipe": recipe.recipe} 
        for recipe in React.objects.all()]
        return Response(recipe)
    
    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    
