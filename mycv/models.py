from django.db import models

# Create your models here.
class Userp(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, default=None)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    about = models.TextField()
    interest = models.TextField()
    image = models.ImageField(upload_to='profile/image')
    resume = models.FileField(upload_to='resume', blank=True)
    ico = models.ImageField(upload_to='profile/image', blank=True)

    def __str__(self):
        return self.fname

class Education(models.Model):
    inc_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    start_yer = models.DateField()
    end_yer = models.DateField(blank=True,default=None)
    passing_yer = models.DateField(blank=True, default=None)
    results = models.CharField(max_length=50, blank=True, default=None)


    def __str__(self):
        return self.inc_name

class Language(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()


    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Social(models.Model):
    icon_name = models.CharField(max_length=50)
    urls = models.URLField(max_length=200)

    def __str__(self):
        return self.icon_name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    present_time = models.CharField(max_length=50,default='Present', blank=True, null=True)

    def __str__(self):
        return self.job_title
