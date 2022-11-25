from django.shortcuts import render

from app.models import*

# Create your views here.


def homePage(request):
    gallery= Gallery.objects.all()
    project= Project.objects.all()
    print(gallery)
    print(project)
    context = {'gallery':gallery,'project':project,'navbar':homePage}
    return render(request,'base/home.html',context)

def projectview(request,pk):
     project= Project.objects.get(id=pk)
     context = {'project':project}
     return render(request,'base/project.html',context)

def aboutMe(request):
    return render(request, 'base/aboutme.html',{'navbar':aboutMe})



def allprojects(request):
    project= Project.objects.all()
    print(project)
    context = {'project':project,'navbar':allprojects}
    return render(request, 'base/allprojects.html',context)




def gallery(request):
    gallery= Gallery.objects.all()
    print(gallery)

    context = {'gallery':gallery,'navbar':gallery}
    return render(request,'base/gallery.html',context)

def contact(request):
    if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone_no = request.POST['phone']
            message = request.POST['message']
            profile_upload = Message.objects.create(sender_name=name,sender_email=email,sender_phone_no=phone_no,full_description=message)
    context = {}
    return render(request,'base/contacts.html',context)

