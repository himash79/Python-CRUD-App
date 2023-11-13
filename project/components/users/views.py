from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from django.contrib import messages

from components.users.models import User


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def submit_remove_user(req, id):
    User.objects.filter(id=id).delete()
    return redirect('/')


def submit_form(req):
    id = req.POST['id']
    name = req.POST['name']
    email = req.POST['email']
    status = req.POST['status']

    userObj = User()
    userObj.id = id
    userObj.name = name
    userObj.email = email
    userObj.status = status

    if User.objects.filter(id=id).exists():
        messages.error(req, 'User added failed', 40)
        print('User ID exists !')
        return redirect('/')
    elif User.objects.filter(email=email).exists():
        messages.error(req, 'User added failed', 40)
        print('User email exists !')
        return redirect('/')

    user = User.objects.create(id=userObj.id, name=userObj.name, email=userObj.email, status=userObj.status)
    user.save()
    messages.success(req, 'User added successfully !', 25)
    print('user added')
    return redirect('/')


def redirect_update_page(req, id):
    user = User.objects.filter(id=id).get()
    template = loader.get_template('updateUser.html')
    context = {
        'user': user,
    }
    print(user)
    return HttpResponse(template.render(context, req))


def submit_update_form(req, id):
    name = req.POST['name']
    email = req.POST['email']
    status = req.POST['status']

    userObj = User.objects.filter(id=id).get()
    userObj.name = name
    userObj.email = email
    userObj.status = status
    userObj.save()
    messages.success(req, 'User updated successfully !', 25)
    return redirect('/')
