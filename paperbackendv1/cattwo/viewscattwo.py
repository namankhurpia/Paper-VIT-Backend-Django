from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import cattwo_papers
from .serializers import cattwo_papersSerializer

class cattwo(APIView):

    def get(self,request):
        cat=cattwo_papers.objects.all()
        serializer=cattwo_papersSerializer(cat,many=True)
        return Response(serializer.data)


    def post(self):
        pass

