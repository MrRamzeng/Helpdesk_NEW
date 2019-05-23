from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from help.models import Tutorial, Ticket
from help.forms import CreateTicket
from datetime import datetime, timedelta, date

@login_required(login_url='login')
def ticket(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        tutorials = Tutorial.objects.all()[:4]
        counter = None
        if Tutorial.objects.count() > 4:
            counter = Tutorial.objects.count()
        if request.method == 'POST':
            form = CreateTicket(request.POST)
            if form.is_valid():
                account = request.user
                text = form.cleaned_data.get('text')
                cabinet = form.cleaned_data.get('cabinet')
                priority = form.cleaned_data.get('priority')
                Ticket.objects.create(
                    client=account,
                    text=text,
                    priority=priority,
                    cabinet=cabinet
                )
                return redirect('tickets')
        else:
            form = CreateTicket()
        tickets = Ticket.objects.filter(
            client=request.user
        ).order_by('priority', 'published_date')
        Ticket.objects.filter(
            status='Исполнена', 
            published_date=datetime.today().date() - timedelta(days=7)
        ).delete()
        return render(
            request, 'tickets.html', 
            {'tutorials': tutorials, 'counter': counter, 'form': form, 'tickets': tickets}
        )
    
def tutorials(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorials.html', {'tutorials': tutorials})

def tutorial(request, tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    return render(request, 'tutorial.html', {'tutorial': tutorial})


