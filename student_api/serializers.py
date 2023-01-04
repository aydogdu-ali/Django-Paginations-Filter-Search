from rest_framework import serializers
from .models import Student, Path



class StudentSerializer(serializers.ModelSerializer):
      
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
       
        fields = ["id","first_name", "last_name","number", "path", "path_id"]

      
   
    
    
class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True)
  
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]