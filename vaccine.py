import requests
import datetime
import time
from playsound import playsound

today = datetime.date.today()
day = int(today.strftime("%d"))

#To Make the server believe that the script is coming from a browser
headerss ={
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' 
}

#Function Section
def vaccine_finder(data , vaccine_list):
  if len(data) == 0 :
    return False
  else:
    for i in range(0 , len(data)):
      if data[i]["available_capacity_dose1"] > 0:
        vaccine_list.append(i)
        return True
      else :
        return False

              
def center_finder(data , vaccine_list):
  if vaccine_finder(data , vaccine_list) == True:
    for i in vaccine_list :
      return f"vaccine avaliable at {data[vaccine_list[i]][NAME]} ,address {data[vaccine_list[i]][ADDRESS]} at pincode {data[vaccine_list[i]][PINCODE]} time python searched {datetime.datetime.now()} {BELL} "
  else :
    return False    

#Constant Section
NAME = "name"
PINCODE = "pincode"
DISTRICT_NAME = "district_name"
DATE = "date"
ADDRESS = "address"
DISTRICT_ID = 764
BELL = "\a" * 60

#Empty_lists for storing values
vaccine_avalaible = [] 
vaccine_avalaible1 = []
vaccine_avalaible2 = []

#Looping section
  
while 3 > 2 : 
  #infinite loop
  request1 = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={DISTRICT_ID}&date={day}-05-2021" , headers=headerss)
  request2 = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={DISTRICT_ID}&date={day + 1}-05-2021" , headers=headerss)
  request3 = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={DISTRICT_ID}&date={day + 2}-05-2021" , headers=headerss)

  #Loading_data_sets

  data_today = request1.json()["sessions"] # {key:value , key: value}
  data_tommorow = request2.json()["sessions"]
  data_day_after_tommorow = request3.json()["sessions"]

  #Calling_functions

  print(center_finder(data_today , vaccine_avalaible)) #Vaccines_on_current_date
  print(center_finder(data_tommorow , vaccine_avalaible1)) #Vaccines_tommorow
  print(center_finder(data_day_after_tommorow , vaccine_avalaible2))#Vaccines_day_after_tommorow

  if center_finder(data_today , vaccine_avalaible) or center_finder (data_tommorow , vaccine_avalaible1) or center_finder(data_day_after_tommorow , vaccine_avalaible2) != False :
    playsound("Real_Police_Siren_freetone.at.ua.mp3")


  #Sleeping_because_of_API_limit
  print("\n")
  time.sleep(60)

  