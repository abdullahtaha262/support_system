from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.translation import gettext_lazy as _
from .models import Ticket
from .forms import TicketForm, TicketUpdateForm
from users.models import UserProfile

# Helper functions to determine user type
def is_customer(user):
    return hasattr(user, 'userprofile') and user.userprofile.user_type == 'customer'

def is_support(user):
    return hasattr(user, 'userprofile') and user.userprofile.user_type == 'support'

# Customer: View Tickets and Open New Ticket
@login_required
@user_passes_test(is_customer)
def customer_dashboard(request):
    tickets = Ticket.objects.filter(customer=request.user.userprofile)
    return render(request, 'tickets/customer_dashboard.html', {'tickets': tickets})

@login_required
@user_passes_test(is_customer)
def open_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = request.user.userprofile
            ticket.save()
            return redirect('customer_dashboard')
    else:
        form = TicketForm()
    return render(request, 'tickets/open_ticket.html', {'form': form})

# Support: View and Update Assigned Tickets
@login_required
@user_passes_test(is_support)
def support_dashboard(request):
    tickets = Ticket.objects.filter(assigned_to=request.user.userprofile)
    return render(request, 'tickets/support_dashboard.html', {'tickets': tickets})

@login_required
@user_passes_test(is_support)
def update_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, assigned_to=request.user.userprofile)
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')
    else:
        form = TicketUpdateForm(instance=ticket)
    return render(request, 'tickets/update_ticket.html', {'form': form})