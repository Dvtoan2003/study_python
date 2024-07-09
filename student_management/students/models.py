from django.db import models

class Student(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10 , choices=[('Male','Nam'), ('Female','Nữ')])
    date_of_bitrh = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=15) 
    major = models.CharField(max_length=100)  
    year_of_enrollment = models.IntegerField() 
    class_name = models.CharField(max_length=50) 
    gpa = models.FloatField() 
    status = models.CharField(max_length=20, choices=[('Active', 'Đang học'), ('Graduated', 'Đã tốt nghiệp'), ('Suspended', 'Bị đình chỉ')]) 
    def __str__(self):
          return f"{self.student_id} - {self.name}"