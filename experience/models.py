from django.db import models
from django.utils import timezone
# Since django has already created a users models for us. We can import it using:
# author = models.ForiegnKey(User, on_delete=models.CASCADE)
from django.contrib.auth.models import User
from django.urls import reverse

class Organizer(models.Model):
    organization_name = models.CharField(max_length=100)
    organizer_logo_link = models.TextField()
    status_type = [(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')]
    status = models.IntegerField(choices=status_type, default=2)

class Experience(models.Model):
    author_name = models.CharField(max_length=100, default="Admin", null=False)
    author_email = models.CharField(max_length=100, null=False)
    author_about = models.TextField(null=False)
    result_type = [(1, 'Accepted'),(2, 'Rejected'),(3, 'Not Declared Yet'),(4, 'None of these')]
    result_field = models.IntegerField(choices=result_type, null=True)
    experience_result_more = models.CharField(max_length=100, null=True)
    experience_type = [(1, 'JOB INTERVIEW EXPERIENCE'),(2, 'INTERNSHIP EXPERIENCE'),(3, 'HACKATHON EXPERIENCE'),(4, 'OTHER EXPERIENCE')]
    experience_type_field = models.IntegerField(choices=experience_type, null=False, default=4)
    # organization_name = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    organization_role = models.CharField(max_length=100, null=True)
    experience_title = models.CharField(max_length=100, null=False)
    experience_desc = models.TextField(null=False)
    experience_recommendation = models.TextField(null=True)
    experience_start_date = models.DateField(null=True)
    experience_end_date = models.DateField(null=True)
    experience_date_posted = models.DateTimeField(default=timezone.now)
    status_type = [(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')]
    status = models.IntegerField(choices=status_type, default=2)
    website = models.CharField(max_length=100, null=True)
    experience_views = models.IntegerField(default=0)
    # organizer_logo_link = models.TextField(null=False)

    def get_absolute_url(self):
        return reverse('experience-post',args=[str(self.id)])
