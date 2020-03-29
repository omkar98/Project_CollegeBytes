from django.db import models
from django.utils import timezone
# Since django has already created a users models for us. We can import it using:
# author = models.ForiegnKey(User, on_delete=models.CASCADE)
from django.contrib.auth.models import User
from django.urls import reverse


class Employment(models.Model):
    role = models.CharField(max_length=100, null=False, default="Not specified")
    salary = models.CharField(max_length=100, default="Best in Industry")
    openings = models.IntegerField(default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    desc = models.TextField(default="No Description Available", null=True)
    company_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Admin", null=False)
    author_email = models.CharField(max_length=100, default="N.A.", null=False)
    eligibility = models.TextField(null=False, default="N.A.")
    last_date = models.DateField(null=True)
    website = models.CharField(max_length=100, null=True)
    type = [(1, 'JOB'),(2, 'INTERNSHIP')]
    post_type = models.IntegerField(choices=type, default=1)
    company_logo_link = models.TextField(null=True)
    status_type = [(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')]
    status = models.IntegerField(choices=status_type, default=2)

    def get_absolute_url(self):
        return reverse('job-post',args=[str(self.id)])

    # def __repr__(self):
    #     self.role
