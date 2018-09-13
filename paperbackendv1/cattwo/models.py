from django.db import models

class cattwo_papers(models.Model):
    course_name=models.CharField(max_length=50)
    course_code=models.CharField(max_length=10)
    slot=models.CharField(max_length=10)
    year=models.CharField(max_length=20)
    data_dir=models.FileField(upload_to='cattwofiles')

    def __str__(self):
        return self.course_code+'-'+self.course_code