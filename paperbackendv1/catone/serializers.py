from rest_framework import serializers
from .models import catone_papers

class catone_papersSerializer(serializers.ModelSerializer):
    class Meta:
        model = catone_papers
        fields='id','course_name','course_code','slot','year','data_dir'
