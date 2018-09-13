from rest_framework import serializers
from .models import cattwo_papers

class cattwo_papersSerializer(serializers.ModelSerializer):
    class Meta:
        model = cattwo_papers
        fields='id','course_name','course_code','slot','year','data_dir'
