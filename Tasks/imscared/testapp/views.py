'''from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")'''

from email.policy import default
from itertools import count
from sqlite3 import paramstyle
from django.http import HttpResponse
from django.shortcuts import render
from testapp.models import apis
from django.db.models import F


def task2(request, start, end):
    from . import task1
    # Send the arguements from dynamic url to the function
    return task1.task2(request, start, end)


def task3(request):
    from . import task3
    return task3.api(request)


def query(request):
    query = request.GET.get("ask")
    if query == None:
        data = {
            'username': " ",
            'userid': ' '
        }

        # When the form is rendered the first time it has a NoneType entity present which gives error loading in database so this is to circumvent that
    else:
        # Checks if the entered username is in the objects that were searched in previous task
        check = apis.objects.filter(username=query)
        # Check if entered username is in the objects that were made during query
        checkquery = apis.objects.filter(username=query+" query")

        if check.first() == None:  # Checks if the enetered query gave an empty queryset
            username = "Not Found"
            userid = " "

        else:
            username = query
            userid = check.first().userid
            if checkquery.first() == None:  # If username entered is searched for the first time, it makes a new username query object
                count = 0
                queryreq = apis(
                    userid=userid, username=query+" query", no=count)
                queryreq.save()
            else:  # If username entered is already in the database it updates the count by 1
                checkquery.update(no=F('no')+1)

        data = {
            'username': username,
            'userid': userid
        }

    # Passes the dictionary to the template to render
    return render(request, 'Database.html', data)


def order(request):
    descending = apis.objects.all().order_by(
        '-no').values('userid', 'username', 'no')
    print(descending)
    data = {
        # order_by('-no') arranges all the objects in a descending order and returns a query set which is then sliced to get the top three queries
        'First': descending[0]['username'] + " was made "+str(descending[0]['no']),
        'Second': descending[1]['username'] + " was made "+str(descending[1]['no']),
        'Third': descending[2]['username'] + " was made "+str(descending[2]['no'])
    }
    return render(request, 'answer.html', data)
