from django.http import HttpResponse
from django.shortcuts import render
from realtors.models import Realtor
from listings.choices import bedroom_choices,state_choices,price_choices
from listings.models import Listing

# Create your views here.

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_publisher=True)[:3]
    
    context ={
         'listings':listings,
         'state_choices':state_choices,
         'bedroom_choices': bedroom_choices,
         'price_choices': price_choices
    }
    return render(request, 'pages/home.html',context)
    
def about(request):
    # get all the realtore
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP
    mvp_realtors =Realtor.objects.all().filter(is_mvp=True)
    context = {
         'realtors':realtors,
         'mvp_realtors':mvp_realtors,
    }
    return render(request, 'pages/about.html',context)