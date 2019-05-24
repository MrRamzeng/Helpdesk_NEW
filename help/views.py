from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from help.models import Ticket, Manual
from help.forms import CreateTicket
from datetime import datetime, timedelta, date

@login_required(login_url='login')
def ticket(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        manuals = Manual.objects.all()[:4]
        counter = None
        if Manual.objects.count() > 4:
            counter = Manual.objects.count()
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
            {'manuals': manuals, 'counter': counter, 'form': form, 'tickets': tickets}
        )
    
def manuals(request):
    manuals = Manual.objects.all()
    return render(request, 'manuals.html', {'manuals': manuals})

def manual(request, manual_id):
    manual = Manual.objects.get(id=manual_id)
    return render(request, 'manual.html', {'manual': manual})


