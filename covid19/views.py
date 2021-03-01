"""Covid views."""

#django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import json

# Utilities
from datetime import datetime


@login_required
def details_covid(request):
    """Details of COVID-19 in the country."""

    url = "https://covid-19-data.p.rapidapi.com/report/totals"

    querystring = {"date":"2020-07-21"}

    headers = {
        'x-rapidapi-key': "248f4b976cmsh4d678ea7b62ac15p17b703jsne52f23805b41",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    update_covid = json.loads(response.content)

    return render(request, 'dashboard/feed.html', {'update_covid': update_covid})

@login_required
def details_country(request):
    """Details covid country."""
    if request.method == 'POST':
        co = request.POST['country']
        if co:
            url = "https://covid-19-data.p.rapidapi.com/country/code"

            querystring = {"code":co}

            headers = {
            'x-rapidapi-key': "248f4b976cmsh4d678ea7b62ac15p17b703jsne52f23805b41",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            country_covid = json.loads(response.content)

            return render(request, 'dashboard/country.html', {'country_covid': country_covid})
        else:
            return render(request,  'dashboard/country.html', {'error': 'Country code not found'})

    
    return render(request, 'dashboard/country.html')