"""Platzigram views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

#Utilities
from datetime import datetime
import pdb



def hello_world(request):
    """Returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"Oh hi! Current time is {now}")


def sort_integers(request):
    numeros = request.GET['numeros']
    num_list = [int(i) for i in numeros.split(',')]

    data = {
        'status': 'ok',
        'numbers': num_list,
        'message': 'ok'        
        }

    return JsonResponse(data, json_dumps_params = {'indent':4})
    # Otra manera
    #return HttpResponse(json.dumps(data, indent=4), content_type = 'application/json')
    
    
def checking_age(request, name, age):
    if age<18:
        message = f"Hi {name} you are not allowed here, sorry"
    else:
        message = f"Hi {name}. Welcome, you can come in"

    return HttpResponse(message)

