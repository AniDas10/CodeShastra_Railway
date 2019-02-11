from django.contrib import admin
from .models import CollegeApplication
# Register your models here.

class CollegeApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_fullname','student_emailId', 'student_collegeId', 'student_aadharId', 'source_station', 'destination_station', 'train_class', 'isApproved_college')
    list_display_links = ('id', 'student_emailId', 'student_fullname')
    search_fields = ('student_emailId', 'student_aadharId', 'student_collegeId')
    list_editable = ('isApproved_college',)
    list_per_page = 25

    def get_ordering(self, request):
        return ['id']

admin.site.register(CollegeApplication, CollegeApplicationAdmin)
