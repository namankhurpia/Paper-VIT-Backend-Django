from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import catone_papers
from .serializers import catone_papersSerializer

class catone(APIView):

    def get(self,request):
        cat=catone_papers.objects.all()
        serializer=catone_papersSerializer(cat,many=True)
        return Response(serializer.data)


    def post(self):
        pass

