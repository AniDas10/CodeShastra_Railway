from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class CollegeApplication(models.Model):
    # student info  
    year_choices =(
        ('FE', 'First Year'),
        ('SE', 'Second Year'),
        ('TE', 'Third Year'),
        ('BE', 'Fourth Year')
    )
    student_photo = models.ImageField(upload_to='students/%m/%d/', blank=True)
    student_collegeId = models.CharField(max_length=255)
    student_emailId = models.EmailField()
    student_aadharId = models.CharField(max_length=255)
    student_fullname = models.CharField(max_length=1024)
    student_contact = models.CharField(max_length=100)
    student_dob = models.DateField()
    student_year = models.CharField(choices=year_choices, max_length=20)
    student_department = models.CharField(max_length=512)
    student_address = models.TextField()

    # railway info 
    trainClasses = (
        ('First', 'First Class'),
        ('Second', 'Second Class')
    )
    source_station = models.CharField(max_length=255)
    destination_station = models.CharField(max_length=255)
    train_class = models.CharField(choices=trainClasses, max_length=50)

    # application info 
    isApproved_college = models.BooleanField(default=False)
    application_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.student_fullname

    def get_application_date(self):
        return self.application_date.strftime("%m/%d/%Y")

    def get_dob(self):
        return self.student_dob.strftime("%m/%d/%Y")

    def get_age(self):
        start_date = self.student_dob
        end_date = self.application_date
        difference  = end_date - start_date
        return (difference.days + difference.seconds/86400)/365.2425
