from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import fat_papers
from .serializers import fat_papersSerializer

class fat(APIView):

    def get(self,request):
        cat=fat_papers.objects.all()
        serializer=fat_papersSerializer(cat,many=True)
        return Response(serializer.data)


    def post(self):
        pass

