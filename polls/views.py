from django.shortcuts import render
from polls.models import Company

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = []
    phoneinterview = []
    test = []
    offer = []
    denied = []
    company_text = []

    queryset = Company.objects.order_by('company_text')[:10]
    for company in queryset:
        company_text.append(company.company_text)
        response.append(company.response)
        phoneinterview.append(company.phoneinterview)
        test.append(company.test)
        offer.append(company.offer)
        denied.append(company.denied)

    return render(request, 'homepage.html', {
        'company': company_text,
        'response': response,
        'phoneinterview': phoneinterview,
        'test': test,
        'offer': offer,
        'denied': denied,
    })
