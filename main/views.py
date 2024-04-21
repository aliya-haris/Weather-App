from django.shortcuts import render
from .models import Weather

import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=960fb76517b04d20108b115cd1ea9f5e').read()
        
        list_of_data = json.loads(source) 

        wData = Weather()
        wData.city = city
        wData.country_code = str(list_of_data['sys']['country'])
        wData.coordinate = str(list_of_data['coord']['lon']) + '  ' + str(list_of_data['coord']['lat'])
        wData.temp = str(list_of_data['main']['temp'])
        wData.pressure = str(list_of_data['main']['pressure'])
        wData.humidity = str(list_of_data['main']['humidity'])
        wData.save()

        bdata = Weather.objects.all().order_by('-timestamp')

        data = { 
            "bdata":bdata,
            "city":city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + '  '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']), 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 


    else: 
        data ={} 
    return render(request, "index.html", data) 
    