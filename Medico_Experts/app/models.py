from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=456)
    is_active=models.BooleanField(default=True)
    is_verfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    first_time_login=models.BooleanField(default=False)

class Doctor(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to='medico_experts/images/',blank=True,default='app/images/doc.png')
    firstname=models.CharField(max_length=50,blank=True)
    lastname=models.CharField(max_length=50,blank=True)
    aboutme=models.CharField(max_length=500,blank=True)
    gender=models.CharField(max_length= 10,blank=True)
    contactno=models.CharField(max_length= 10,blank=True)
    city=models.CharField(max_length=50,blank=True)
    country=models.CharField(max_length=70,blank=True)
    terms = models.BooleanField(default=False)

    hospital_affiliations=models.CharField(max_length= 50,blank=True)
    medical_school=models.CharField(max_length= 100,blank=True)
    residency=models.CharField(max_length= 100,blank=True)
    certifications=models.CharField(max_length= 100,blank=True)
    experience=models.CharField(max_length= 100,blank=True)
    internship=models.CharField(max_length= 100,blank=True)
    specialties=models.CharField(max_length= 500,blank=True)
    birthday=models.DateField(null=True,blank=True)
    task_notification=models.BooleanField(default=True)
    friend_notification=models.BooleanField(default=True)

    experience=models.CharField(max_length= 50,blank=True,default="None")
    awards=models.CharField(max_length= 50,blank=True,default="None")
    clients=models.CharField(max_length= 50,blank=True,default="None")
    

class Patient(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to='medico_experts/images/',blank=True,default='app/images/doc.png')
    firstname=models.CharField(max_length=50,blank=True)
    lastname=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length= 10,blank=True)
    contactno=models.CharField(max_length= 10,blank=True)
    terms = models.BooleanField(default=False)
    






