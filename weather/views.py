from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    api_url = url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b164f270413252f348002aa44a1eee1a'
    error_msg = ''
    message = ''
    message_class = ''
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count =City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                b = requests.get(url.format(new_city)).json()
                print(b)
                if b['cod'] == 200:
                    form.save()                
                else:
                    error_msg = 'City does not exist in the world!'            
            else:
                error_msg = 'City already exists!'
        if error_msg:
            message = error_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        b = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : b['main']['temp'],
            'description' : b['weather'][0]['description'],
            'icon' : b['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {'weather_data' : weather_data,
     'form' : form,
     'message' : message,
     'message_class' : message_class,
     }
    return render(request, 'weather/weather.html', context)

def delete_city(request, city_name, indexPosition=None):
    City.objects.get(name=city_name).delete()
    return redirect('index')