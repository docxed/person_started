from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Person

# Create your views here.


def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {'all_person': all_person})


def about(request):
    return render(request, 'about.html')


def form(request, person_id=None, delete_person_id=None):
    if request.method == 'POST':
        if request.POST['person_id']:  # Update
            person = Person.objects.get(id=request.POST['person_id'])
            person.firstname = request.POST['firstname']
            person.lastname = request.POST['lastname']
            person.email = request.POST['email']
            person.age = request.POST['age']
            person.save()
        else:  # Create
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            age = request.POST['age']
            person = Person(firstname=firstname, lastname=lastname,
                            email=email, age=age)
            person.save()
        return HttpResponseRedirect('/')
    elif person_id:
        person = Person.objects.get(id=person_id)
        return render(request, 'form.html', {'person': person})
    elif delete_person_id:  # Delete
        person = Person.objects.get(id=delete_person_id)
        person.delete()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'form.html')
