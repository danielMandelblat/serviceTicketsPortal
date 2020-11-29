from django.shortcuts import render
from portal.forms import new_ticket_form
from portal.models import ticket

menu = [
        {'page': 'My Tickets', 'url': 'tickets'},
        {'page': 'New Ticket', 'url': 'new_ticket'},
        {'page': 'Test', 'url': 'test'},
    ]

def tickets(request):
    context = {'menu': menu, 'title': 'Tickets'}
    context['tickets'] = ticket.objects.all()
    return render(request, template_name='tickets.html', context=context)

def new_ticket(request):
    context = {'menu': menu, 'title': 'New Ticket'}

    #Create a new form object
    form = new_ticket_form(request.POST or None)
    if form.is_valid():

        form.save()
        form = new_ticket_form()

    context['form'] = form
    return render(request, template_name='new_ticket.html', context=context)

def test(request):
    context = {'menu': menu, 'title': 'Test'}
    return render(request, template_name='test.html', context=context)