from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import random 
import json

@csrf_exempt
def index(request):
    api_url = 'https://countriesnow.space/api/v0.1/countries/capital'
    response = requests.get(api_url)
    data = response.json()

    global random_country
    random_country = random.choice(data['data'])
    country = random_country['name']
    correct_capital = random_country['capital']
    print(correct_capital)

    return render(request, 'mainapp/index.html', {'country': country})

@csrf_exempt
def checkCapital(request):
    if request.method == 'POST':
        country = random_country['name']
        correct_capital = random_country['capital']
        print(correct_capital)
        data = json.loads(request.body.decode('UTF-8'))
        guessed_capital = data['inputCapital']
        print(guessed_capital)
        message=""

        if guessed_capital.lower() == correct_capital.lower():
            message = "Correct! Sam guessed the capital correctly."
        else:
            message = f"Oops! the answer is incorrect, the correct capital of '{country}' is '{correct_capital}'."

        return JsonResponse({"message":message})


