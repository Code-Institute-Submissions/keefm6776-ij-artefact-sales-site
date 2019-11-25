from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import *
from .models import Bids
from artefacts.models import Artefact
from customer.models import Customer
from .forms import BidsForm
from artefacts.views import for_sale_artefacts



#def get_bids(request):
#    """
#    Create a view that will return a list
#    of Relevant Bids For The Artefact
#    and render them to the 'bids.html' template
#    """
#    bids = Bids.objects.get()
#    return render(request, "make_bid.html", {'bids': bids})

def make_bid(request, pk):
    """ Allows Customer To Make A bid On An Artefact """
    artefact_bid = get_object_or_404(Artefact, pk=pk) if pk else None
    user = request.user
    customer = get_object_or_404(Customer, pk=user.customer.id) if pk else None
    
    try:
        highest_bid = Bids.objects.filter(customer_id=customer, artefact_id=pk).latest('bid').bid
    except Bids.DoesNotExist:
        highest_bid = 0.00

    print(type(highest_bid))
    form = BidsForm(request.POST, request.FILES)
  
    if request.method == "POST":
        if form.is_valid():
            print(type(form.fields['bid']))
            if form.cleaned_data["bid"] > highest_bid:
                form = form.save(commit=False)
                form.customer_id = customer
                form.artefact_id = artefact_bid
                form.save()
                return redirect(for_sale_artefacts)
            else:
                form.add_error(None, "Your bid must be greater than the current maximum bid")
        else:
            form = BidsForm()
            return redirect(for_sale_artefacts)
            
    return render(request, "make_bid.html", {'form': form, 'highest_bid': highest_bid})
