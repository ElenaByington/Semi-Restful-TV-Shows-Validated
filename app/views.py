from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def to_all_shows(request):
    # /shows - GET - method should return a template that displays all the shows in a table
    all_shows = Show.objects.all()
    context = {
        "shows":all_shows
    }
    return render(request,'index.html',context)

def add_new_show(request):
    # /shows/new- GET - method should return a template containing the form for adding a new TV show
    return render(request,'add_new_show.html')

def show_page(request,id):
    # /shows/<id> - GET - method should return a template that displays the specific show's information
    show_page = Show.objects.get(id=id)
    context = {
        "show":show_page
    }
    return render(request,'show_page.html',context)

def edit_show_page(request,id):
    # /shows/<id>/edit - GET - method should return a template that displays a form for editing the TV show with the id specified in the url
    edit_page = Show.objects.get(id=id)
    context = {
        "show":edit_page
    }
    return render(request,'edit_show.html',context)

def create_new_show(request):
    # /shows/create - POST - method should add the show to the database, then redirect to /shows/<id>
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')

    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    id = str(Show.objects.last().id)
    return redirect(f'/shows/{id}')

def update_show(request,id):
    # /shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>
    id = str(Show.objects.last().id)
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        context = {
            "show":show
        }
        return redirect(f'/shows/{id}',context)

def delete_show(request,id):
    # /shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
