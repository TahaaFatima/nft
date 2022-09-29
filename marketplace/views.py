from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Collection, Testimonials


def home(request):
    rating = Testimonials.objects.all()
    context1 = {
        'rate': rating
    }
    return render(request, 'index.html', context1)


def collect(request):
    data = Collection.objects.all()
    collectionList = {'collectionList': data}
    return render(request, 'collect.html', collectionList)


def connect_wallet(request):
    return render(request, 'connect-wallet.html')


def create(request):
    return render(request, 'create.html')


def faq(request):
    return render(request, 'faq.html')

def roadmap(request):
    return render(request, 'roadmap.html')

def check_out(request):
    data = Collection.objects.all()
    collectionList = {'collectionList': data}
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        data = {
            'email':email,
            'name':name
        }
        send_mail('NFT',
                'Dear' + name +'You have successfully purchased NFT',
                'enaftee34@gmail.com', 
                ['hzehra34@gmail.com'],
                fail_silently=False)
    return render(request, 'check_out.html')

def nft_detail(request, data_id):
    information = get_object_or_404(Collection,id=data_id)
    context = {
        'data' : information
    }
    return render(request , 'details.html' , context)