from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication, RemoteJob, RemoteJobApplication, WalkInJob, WalkInJobApplication
from .forms import JobForm, JobApplicationForm, RemoteJobForm, RemoteJobApplicationForm, WalkInJobForm, WalkInJobApplicationForm

# Create your views here.

# Domain Job List
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_on')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# Remote Job List
def remote_job_list(request):
    jobs = RemoteJob.objects.all().order_by('-posted_on')
    return render(request, 'jobs/remote_job_list.html', {'jobs': jobs})

# Walk-In Job List
def walkIn_job_list(request):
    jobs = WalkInJob.objects.all().order_by('-posted_on')
    return render(request, 'jobs/walkIn_job_list.html', {'jobs': jobs})


# Add Domain Job
def add_job(request):
    # if not request.user.is_staff:  # Only admin/developer can post
    #     return redirect('app2:add_job')

    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app2:job_list')
    else:
        form = JobForm()

    return render(request, 'jobs/add_job.html', {'form': form})

# Add Remote Job
def add_remote_job(request):
    # if not request.user.is_staff:  # Only admin/developer can post
    #     return redirect('app2:add_remote_job')

    if request.method == 'POST':
        form = RemoteJobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app2:remote_job_list')
    else:
        form = RemoteJobForm()

    return render(request, 'jobs/add_remote_job.html', {'form': form})

# Add Walk-In Job
def add_walkin_job(request):
    # if not request.user.is_staff:  # Only admin/developer can post
    #     return redirect('app2:add_walkin_job')

    if request.method == 'POST':
        form = WalkInJobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app2:walkIn_job_list')
    else:
        form = WalkInJobForm()

    return render(request, 'jobs/add_walkin_job.html', {'form': form})



# Domain Job Detail
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# Remote Job Detail
def remote_job_detail(request, job_id):
    job = get_object_or_404(RemoteJob, id=job_id)
    return render(request, 'jobs/remote_job_detail.html', {'job': job})

# Walk-In Job Detail
def walkIn_job_detail(request, job_id):
    job = get_object_or_404(WalkInJob, id=job_id)
    return render(request, 'jobs/walkIn_job_detail.html', {'job': job})









# Domain Job Application
@login_required(login_url='app1:login')
def job_application(request, job_id):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    """View to display and process the job application form"""
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create but don't save the job application instance yet
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.status = 'Applied'
            
            # Now save the application
            application.save()
            
            # Send confirmation email (optional)
            # send_application_confirmation_email(request.user.email, job)
            
            messages.success(request, f"Your application for {job.title} has been submitted successfully!")
            return redirect('app2:applied_jobs')
        else:
            messages.error(request, "There was an error with your application. Please check the form and try again.")
    else:
        form = JobApplicationForm()
    
    return render(request, 'jobs/job_application.html', {
        'job': job,
        'form': form,
    })


# Remote Job Application
@login_required(login_url='app1:login')
def remote_job_application(request, job_id):
    """View to display and process the job application form"""
    job = get_object_or_404(RemoteJob, id=job_id)
    
    if request.method == 'POST':
        form = RemoteJobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create but don't save the job application instance yet
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.status = 'Applied'
            
            # Now save the application
            application.save()
            
            # Send confirmation email (optional)
            # send_application_confirmation_email(request.user.email, job)
            
            messages.success(request, f"Your application for {job.title} has been submitted successfully!")
            return redirect('app2:applied_remote_jobs')
        else:
            messages.error(request, "There was an error with your application. Please check the form and try again.")
    else:
        form = RemoteJobApplicationForm()
    
    return render(request, 'jobs/remote_job_application.html', {
        'job': job,
        'form': form,
    })


# Walk-In Job Application
@login_required(login_url='app1:login')
def walkIn_job_application(request, job_id):
    """View to display and process the job application form"""
    job = get_object_or_404(WalkInJob, id=job_id)
    
    if request.method == 'POST':
        form = WalkInJobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create but don't save the job application instance yet
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.status = 'Applied'
            
            # Now save the application
            application.save()
            
            # Send confirmation email (optional)
            # send_application_confirmation_email(request.user.email, job)
            
            messages.success(request, f"Your application for {job.title} has been submitted successfully!")
            return redirect('app2:applied_walkin_jobs')
        else:
            messages.error(request, "There was an error with your application. Please check the form and try again.")
    else:
        form = WalkInJobApplicationForm()
    
    return render(request, 'jobs/walkIn_job_application.html', {
        'job': job,
        'form': form,
    })






# Domain Applied Jobs
@login_required(login_url='app1:login')
def applied_jobs(request):
    """View to display all jobs the user has applied for"""
    applications = JobApplication.objects.filter(user=request.user).order_by('-applied_date')
    
    return render(request, 'jobs/applied_jobs.html', {
        'applications': applications
    })

# Remote Applied Jobs
@login_required(login_url='app1:login')
def applied_remote_jobs(request):
    """View to display all jobs the user has applied for"""
    applications = RemoteJobApplication.objects.filter(user=request.user).order_by('-applied_date')
    
    return render(request, 'jobs/applied_remote_jobs.html', {
        'applications': applications
    })

# Walk-In Applied Jobs
@login_required(login_url='app1:login')
def applied_walkin_jobs(request):
    """View to display all jobs the user has applied for"""
    applications = WalkInJobApplication.objects.filter(user=request.user).order_by('-applied_date')
    
    return render(request, 'jobs/applied_walkin_jobs.html', {
        'applications': applications
    })