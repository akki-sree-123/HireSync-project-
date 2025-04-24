from django import forms
from .models import Job, JobApplication, RemoteJob, RemoteJobApplication, WalkInJob, WalkInJobApplication

# Domain Job Form
class JobForm(forms.ModelForm):
    # Custom field widgets
    responsibilities = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each responsibility on a new line'}),
        required=False
    )
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each requirement on a new line'}),
        required=False
    )
    benefits = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each benefit on a new line'}),
        required=False
    )
    
    class Meta:
        model = Job
        fields = [
            'title', 
            'companyImage', 
            'description', 
            'company', 
            'location',
            'responsibilities',
            'requirements',
            'benefits',
            'job_type',
            'experience',
            'education',
            'salary',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe the job position'}),
            'experience': forms.TextInput(attrs={'placeholder': 'e.g., 3+ years'}),
            'education': forms.TextInput(attrs={'placeholder': 'e.g., Bachelor\'s Degree'}),
            'salary': forms.TextInput(attrs={'placeholder': 'e.g., 60,000 - 80,000 or Based on experience'}),
        }



# Remote Job Form
class RemoteJobForm(forms.ModelForm):
    # Custom field widgets
    responsibilities = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each responsibility on a new line'}),
        required=False
    )
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each requirement on a new line'}),
        required=False
    )
    benefits = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each benefit on a new line'}),
        required=False
    )
    
    class Meta:
        model = RemoteJob
        fields = [
            'title', 
            'companyImage', 
            'description', 
            'company', 
            'location',
            'responsibilities',
            'requirements',
            'benefits',
            'job_type',
            'experience',
            'education',
            'salary',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe the job position'}),
            'experience': forms.TextInput(attrs={'placeholder': 'e.g., 3+ years'}),
            'education': forms.TextInput(attrs={'placeholder': 'e.g., Bachelor\'s Degree'}),
            'salary': forms.TextInput(attrs={'placeholder': 'e.g., 60,000 - 80,000 or Based on experience'}),
        }



# Walk-In Job Form
class WalkInJobForm(forms.ModelForm):
    # Custom field widgets
    responsibilities = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each responsibility on a new line'}),
        required=False
    )
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each requirement on a new line'}),
        required=False
    )
    benefits = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter each benefit on a new line'}),
        required=False
    )
    
    class Meta:
        model = WalkInJob
        fields = [
            'title', 
            'companyImage', 
            'description', 
            'company', 
            'location',
            'responsibilities',
            'requirements',
            'benefits',
            'job_type',
            'experience',
            'education',
            'salary',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe the job position'}),
            'experience': forms.TextInput(attrs={'placeholder': 'e.g., 3+ years'}),
            'education': forms.TextInput(attrs={'placeholder': 'e.g., Bachelor\'s Degree'}),
            'salary': forms.TextInput(attrs={'placeholder': 'e.g., 60,000 - 80,000 or Based on experience'}),
        }







# Job Application Form
# Domain Job Application Form
class JobApplicationForm(forms.ModelForm):
    """
    Form for job applications with custom validation and styling
    """
    # Add custom validators or field types if needed
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    linkedin = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    current_title = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    experience_years = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Select'),
            ('0-1', 'Less than 1 year'),
            ('1-3', '1-3 years'),
            ('3-5', '3-5 years'),
            ('5-10', '5-10 years'),
            ('10+', '10+ years'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    education = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('High School', 'High School'),
            ('Associate\'s Degree', 'Associate\'s Degree'),
            ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
            ('Master\'s Degree', 'Master\'s Degree'),
            ('Doctorate', 'Doctorate'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    notice_period = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Immediate', 'Immediate'),
            ('1 Week', '1 Week'),
            ('2 Weeks', '2 Weeks'),
            ('1 Month', '1 Month'),
            ('More than 1 Month', 'More than 1 Month'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'List your relevant skills (comma separated)',
            'rows': 4
        })
    )
    resume = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    cover_letter = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    relocate = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Maybe', 'Maybe'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    additional_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Any additional information you\'d like to share',
            'rows': 4
        })
    )
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    future_contact = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    
    class Meta:
        model = JobApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'location', 'linkedin',
            'current_title', 'experience_years', 'education', 'notice_period', 'skills',
            'resume', 'cover_letter', 'relocate', 'additional_info',
            'terms_agree', 'future_contact'
        ]
    
    def clean_resume(self):
        """Validate resume file type and size"""
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check file extension
            file_extension = resume.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for resume.")
            
            # Check file size (limit to 5MB)
            if resume.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Resume file size must be under 5MB.")
        return resume
    
    def clean_cover_letter(self):
        """Validate cover letter file type and size if provided"""
        cover_letter = self.cleaned_data.get('cover_letter')
        if cover_letter:
            # Check file extension
            file_extension = cover_letter.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for cover letter.")
            
            # Check file size (limit to 5MB)
            if cover_letter.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Cover letter file size must be under 5MB.")
        return cover_letter
    



# Remote Job Application Form
class RemoteJobApplicationForm(forms.ModelForm):
    """
    Form for job applications with custom validation and styling
    """
    # Add custom validators or field types if needed
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    linkedin = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    current_title = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    experience_years = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Select'),
            ('0-1', 'Less than 1 year'),
            ('1-3', '1-3 years'),
            ('3-5', '3-5 years'),
            ('5-10', '5-10 years'),
            ('10+', '10+ years'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    education = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('High School', 'High School'),
            ('Associate\'s Degree', 'Associate\'s Degree'),
            ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
            ('Master\'s Degree', 'Master\'s Degree'),
            ('Doctorate', 'Doctorate'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    notice_period = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Immediate', 'Immediate'),
            ('1 Week', '1 Week'),
            ('2 Weeks', '2 Weeks'),
            ('1 Month', '1 Month'),
            ('More than 1 Month', 'More than 1 Month'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'List your relevant skills (comma separated)',
            'rows': 4
        })
    )
    resume = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    cover_letter = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    relocate = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Maybe', 'Maybe'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    additional_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Any additional information you\'d like to share',
            'rows': 4
        })
    )
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    future_contact = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    
    class Meta:
        model = RemoteJobApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'location', 'linkedin',
            'current_title', 'experience_years', 'education', 'notice_period', 'skills',
            'resume', 'cover_letter', 'relocate', 'additional_info',
            'terms_agree', 'future_contact'
        ]
    
    def clean_resume(self):
        """Validate resume file type and size"""
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check file extension
            file_extension = resume.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for resume.")
            
            # Check file size (limit to 5MB)
            if resume.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Resume file size must be under 5MB.")
        return resume
    
    def clean_cover_letter(self):
        """Validate cover letter file type and size if provided"""
        cover_letter = self.cleaned_data.get('cover_letter')
        if cover_letter:
            # Check file extension
            file_extension = cover_letter.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for cover letter.")
            
            # Check file size (limit to 5MB)
            if cover_letter.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Cover letter file size must be under 5MB.")
        return cover_letter
    



# Walk-In Job Application Form
class WalkInJobApplicationForm(forms.ModelForm):
    """
    Form for job applications with custom validation and styling
    """
    # Add custom validators or field types if needed
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    linkedin = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    current_title = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    experience_years = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Select'),
            ('0-1', 'Less than 1 year'),
            ('1-3', '1-3 years'),
            ('3-5', '3-5 years'),
            ('5-10', '5-10 years'),
            ('10+', '10+ years'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    education = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('High School', 'High School'),
            ('Associate\'s Degree', 'Associate\'s Degree'),
            ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
            ('Master\'s Degree', 'Master\'s Degree'),
            ('Doctorate', 'Doctorate'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    notice_period = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Immediate', 'Immediate'),
            ('1 Week', '1 Week'),
            ('2 Weeks', '2 Weeks'),
            ('1 Month', '1 Month'),
            ('More than 1 Month', 'More than 1 Month'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'List your relevant skills (comma separated)',
            'rows': 4
        })
    )
    resume = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    cover_letter = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'file-input'})
    )
    relocate = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Maybe', 'Maybe'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    additional_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Any additional information you\'d like to share',
            'rows': 4
        })
    )
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    future_contact = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    
    class Meta:
        model = WalkInJobApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'location', 'linkedin',
            'current_title', 'experience_years', 'education', 'notice_period', 'skills',
            'resume', 'cover_letter', 'relocate', 'additional_info',
            'terms_agree', 'future_contact'
        ]
    
    def clean_resume(self):
        """Validate resume file type and size"""
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check file extension
            file_extension = resume.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for resume.")
            
            # Check file size (limit to 5MB)
            if resume.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Resume file size must be under 5MB.")
        return resume
    
    def clean_cover_letter(self):
        """Validate cover letter file type and size if provided"""
        cover_letter = self.cleaned_data.get('cover_letter')
        if cover_letter:
            # Check file extension
            file_extension = cover_letter.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed for cover letter.")
            
            # Check file size (limit to 5MB)
            if cover_letter.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Cover letter file size must be under 5MB.")
        return cover_letter