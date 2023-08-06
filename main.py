import os
import requests
import json

try:
    city = input("Enter Your City\n")
    url = f"https://api.weatherapi.com/v1/current.json?key=2c9bcd3730ec4586a31134125230608&q={city}&aqi=no"
    get = requests.get(url)
    Wather_dic =  json.loads(get.text)
    temp_value = Wather_dic['current']['temp_c']
    commend = f"say 'The Current Wather In{city} City Was {temp_value} Degree'"
    print(f"{temp_value} Degree")
    os.system(commend)
except Exception as err:
    print("We Just Got Some Error !!!!!") 

 
