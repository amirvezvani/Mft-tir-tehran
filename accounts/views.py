from django.shortcuts import render,redirect
from .models import UserProfileModel,AddEducationModel,AddExperienceModel
# Create your views here.


def addeducation(request):
    if request.method=='POST':
        school=request.POST.get('school')
        degree=request.POST['degree']
        field=request.POST['field']
        start=request.POST['start']
        description=request.POST['description']
        
        AddEducationModel.objects.create(school=school,
                                         degree=degree,
                                         field=field,
                                         start=start,
                                         description=description
                                         
        )
        return redirect('dashboard')
    elif request.method=='GET':
        return render(request,'accounts/addeducation.html')

def addexperience(request):
    if request.method=='POST':
        job=request.POST['job']
        company=request.POST['company']
        location=request.POST['location']
        start=request.POST['start']
        end=request.POST['end']
        description=request.POST['description']
        
        AddExperienceModel.objects.create(job=job,
                                          company=company,
                                          location=location,
                                          start=start,
                                          end=end,
                                          description=description
                                          )
        return redirect('dashboard')

    elif request.method=='GET':
        return render(request,'accounts/addexperience.html',{})

def createprofile(request):
    return render(request, 'accounts/createprofile.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def login(request):
    return render(request, 'accounts/login.html', {})


def profile(request,pk):
    user_education=AddEducationModel.objects.get(id=pk)
    user_exprience=AddExperienceModel.objects.get(id=pk)
    user_profile=UserProfileModel.objects.get(id=pk)
    return render(request, 'accounts/profile.html', {'user_profile':user_profile, 'user_education':user_education,'user_exprience':user_exprience})


def profiles(request):
    users=UserProfileModel.objects.all()
    return render(request, 'accounts/profiles.html', {'users':users})


def register(request):
    return render(request, 'accounts/register.html', {})
