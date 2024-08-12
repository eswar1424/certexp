from django.shortcuts import render
from django.http import HttpResponse
from .models import Domain
from .cert_utils import get_expiry_dates_of_file
import os

from .cert_utils import get_expiry_date as getexp
import csv

# Create your views here.

def home(request):
    return render(request,template_name="home.html")

def about(request):
    return render(request,template_name="about.html")

def dashboard(request):
    content = {}
    #get_expiry_dates_of_file("domains.csv")
    content["hosts"] = get_expiry_dates_db()
    print(content)
    return render(request,"dashboard.html",content)


def get_expiry_date(request):
    hostname = request.GET.get('host')
    date = getexp(hostname)
    response = {"hostname":hostname,
                "exp": str(date)
                }
    return HttpResponse(str(response))


def readFile():
    hosts = []
    reader = csv.reader(open("expiry_dates.csv","r"))

    for row in reader:
        temp = {}
        temp["host"] = row[0]
        temp["exp_date"] = row[1]
        temp["exp_time"] = row[2]
        hosts.append(temp)

    return hosts

def save_file_in_db(request):
    reader = csv.reader(open('domains.csv','r'))
    for row in reader:
        hostname = row[0]
        domain = Domain(hostname=hostname)
        domain.save()
        return HttpResponse("Success")



def get_expiry_dates_db():
    hosts = []

    domains = Domain.objects.all()

    for domain in domains:
        expiry = getexp(domain.hostname)
        temp = {}
        temp['host'] = domain.hostname
        temp['exp_date'] = expiry.date().__str__
        temp['exp_time'] = expiry.time().__str__
        #print(temp)
        hosts.append(temp)

    return hosts
