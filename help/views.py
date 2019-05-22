from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from help.models import Tutorial

@login_required(login_url='login')
def ticket(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        tutorials = Tutorial.objects.all()[:5]
        return render(request, 'tickets.html', {'tutorials': tutorials})
    
def tutorials(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorials.html', {'tutorials': tutorials})

def tutorial(request, tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    return render(request, 'tutorial.html', {'tutorial': tutorial})


