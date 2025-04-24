from django.db import models
from app1.models import CustomUser
from django.utils import timezone

# Create your models here.
# Domain Job Model
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=100)
    companyImage = models.ImageField(upload_to='CompanyImages/', null=True, blank=True)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    # New fields
    responsibilities = models.TextField(blank=True, help_text="Enter responsibilities separated by new lines")
    requirements = models.TextField(blank=True, help_text="Enter requirements separated by new lines")
    benefits = models.TextField(blank=True, help_text="Enter benefits separated by new lines")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='Full-time')
    experience = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def responsibilities_list(self):
        """Return responsibilities as a list of items"""
        if self.responsibilities:
            return [item.strip() for item in self.responsibilities.split('\n') if item.strip()]
        return []
    
    def requirements_list(self):
        """Return requirements as a list of items"""
        if self.requirements:
            return [item.strip() for item in self.requirements.split('\n') if item.strip()]
        return []
    
    def benefits_list(self):
        """Return benefits as a list of items"""
        if self.benefits:
            return [item.strip() for item in self.benefits.split('\n') if item.strip()]
        return []
    


# Remote Job Model
class RemoteJob(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=100)
    companyImage = models.ImageField(upload_to='CompanyImages/', null=True, blank=True)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    # New fields
    responsibilities = models.TextField(blank=True, help_text="Enter responsibilities separated by new lines")
    requirements = models.TextField(blank=True, help_text="Enter requirements separated by new lines")
    benefits = models.TextField(blank=True, help_text="Enter benefits separated by new lines")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='Full-time')
    experience = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def responsibilities_list(self):
        """Return responsibilities as a list of items"""
        if self.responsibilities:
            return [item.strip() for item in self.responsibilities.split('\n') if item.strip()]
        return []
    
    def requirements_list(self):
        """Return requirements as a list of items"""
        if self.requirements:
            return [item.strip() for item in self.requirements.split('\n') if item.strip()]
        return []
    
    def benefits_list(self):
        """Return benefits as a list of items"""
        if self.benefits:
            return [item.strip() for item in self.benefits.split('\n') if item.strip()]
        return []


# Walk-In Job Model
class WalkInJob(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=100)
    companyImage = models.ImageField(upload_to='CompanyImages/', null=True, blank=True)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    # New fields
    responsibilities = models.TextField(blank=True, help_text="Enter responsibilities separated by new lines")
    requirements = models.TextField(blank=True, help_text="Enter requirements separated by new lines")
    benefits = models.TextField(blank=True, help_text="Enter benefits separated by new lines")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='Full-time')
    experience = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def responsibilities_list(self):
        """Return responsibilities as a list of items"""
        if self.responsibilities:
            return [item.strip() for item in self.responsibilities.split('\n') if item.strip()]
        return []
    
    def requirements_list(self):
        """Return requirements as a list of items"""
        if self.requirements:
            return [item.strip() for item in self.requirements.split('\n') if item.strip()]
        return []
    
    def benefits_list(self):
        """Return benefits as a list of items"""
        if self.benefits:
            return [item.strip() for item in self.benefits.split('\n') if item.strip()]
        return []
    




# Job Application Table
# Domain Job Application
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offered', 'Offered'),
        ('Accepted', 'Accepted'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_applications')
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True, null=True)
    current_title = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=50)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    relocate = models.CharField(max_length=10)
    additional_info = models.TextField(blank=True, null=True)
    terms_agree = models.BooleanField(default=False)
    future_contact = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title} ({self.status})"
    
    class Meta:
        ordering = ['-applied_date']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'



# Remote Job Application
class RemoteJobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offered', 'Offered'),
        ('Accepted', 'Accepted'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='remote_job_applications')
    job = models.ForeignKey('RemoteJob', on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True, null=True)
    current_title = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=50)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    relocate = models.CharField(max_length=10)
    additional_info = models.TextField(blank=True, null=True)
    terms_agree = models.BooleanField(default=False)
    future_contact = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title} ({self.status})"
    
    class Meta:
        ordering = ['-applied_date']
        verbose_name = 'Remote Job Application'
        verbose_name_plural = 'Remote Job Applications'



# Walk-In Job Application
class WalkInJobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offered', 'Offered'),
        ('Accepted', 'Accepted'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='walkin_job_applications')
    job = models.ForeignKey('WalkInJob', on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True, null=True)
    current_title = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=50)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    relocate = models.CharField(max_length=10)
    additional_info = models.TextField(blank=True, null=True)
    terms_agree = models.BooleanField(default=False)
    future_contact = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title} ({self.status})"
    
    class Meta:
        ordering = ['-applied_date']
        verbose_name = 'Walk-In Job Application'
        verbose_name_plural = 'Walk-In Job Applications' 





