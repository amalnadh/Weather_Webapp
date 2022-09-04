

from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=50ac73dd8577d1558f31e8b6d9d749d0'
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    form = CityForm()
    cities=City.objects.all()


    weather_data=[]

    for city in cities:
        re = requests.get(url.format(city)).json()

        city_weather= {
            'id':city.id,
            'city': city.city_name,
            'temperature': re['main']['temp'],
            'description': re['weather'][0]['description'],
            'icon':re['weather'][0]['icon'],
            'humidity':re['main']['humidity'],

        }
        weather_data.append(city_weather)

        context={
            'weather_data': weather_data,
            'form': form,
        }


    return render(request,'index.html',context)


def delete(request,c_id):
     dele=City.objects.get(id=c_id)
     if request.method=='POST':
        dele.delete()
        return redirect('/')

     return render(request,'delete.html')
