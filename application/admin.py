from django.contrib import admin
from .models import user_mapping,Questions,Question_vote,answers,Customer_mobile,Answer_vote
from twilio.rest import Client
from sms import send_sms
from django.conf import settings 
from django.contrib.gis.geoip2 import GeoIP2
import requests
# from .translate import googleTranslate
# Register your models here.

admin.site.register(user_mapping)
admin.site.register(Questions)
admin.site.register(Question_vote)
admin.site.register(answers)
admin.site.register(Answer_vote)

@admin.action(description='send weather details')
def make_published(modeladmin, request, queryset):
    
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    print(queryset)
    for i in queryset:
        ph = str(i.mobile)
        city = str(i.city)
        print(city)
        my_weather =requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d7a7824d87bf02042e2803c0c10f8f46").json()
        print(my_weather)
        message_to_broadcast = ("\nHi Mr/Mrs "+str(i.user)+"\n"+"Weather Forecast for "+str(my_weather['name'])
                        +"\n"+ "weather : "+str(my_weather['weather'][0]['main']) + "\nDescription:"+ str(my_weather['weather'][0]['description'])
                        +"\nPressure : "+str(my_weather['main']['pressure'])+"\nWindspeed : "+str(my_weather['wind']['speed']))
        print(message_to_broadcast)
        client.messages.create(to=ph,from_=settings.TWILIO_NUMBER,body=message_to_broadcast)

# 8a0ec96d-a252-41b7-9583-f184ac33a77e

class Customer_mob(admin.ModelAdmin):
    list_display = ['user', 'mobile','city']
    ordering = ['user']
    actions = [make_published]
admin.site.register(Customer_mobile,Customer_mob)