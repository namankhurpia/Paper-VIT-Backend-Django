from rest_framework import serializers
from .models import fat_papers

class fat_papersSerializer(serializers.ModelSerializer):
    class Meta:
        model = fat_papers
        fields='id','course_name','course_code','slot','year','data_dir'
