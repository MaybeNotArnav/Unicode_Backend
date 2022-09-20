import requests
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.db.models import F
from testapp.models import apis


def api(request):
    query = request.GET.get("userid", 96479162)
    url = "https://twitter154.p.rapidapi.com/user/id"

    querystring = {"user_id": query}

    headers = {
        "X-RapidAPI-Key": "2571ca3296msh575ff6ba1557501p1bec38jsne5a1bdc2f650",
        "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    if 'detail' in response.keys():
        error = 'Username for user id = {} not found'
        data = {
            'case': 404,
            'detail': error.format(query)
        }
    else:
        username = response['username']

        data = {
            'case': 1,
            'userid': query,
            'username': username
        }

        id = request.GET.get("userid")
        if id != None:
            count = 0
            apireq = apis(userid=id, username=username, no=count)
            finder = apis.objects.filter(userid=id)
            if finder.first() == None:
                apireq.save()

    # return HttpResponse(response.text)
    return render(request, 'website.html', data)
