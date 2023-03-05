import requests
import time
from datetime import datetime

def get_time():
  now = datetime.now()
  date = '"'+ now.strftime('%Y-%m-%d %H:%M:%S')+'"'
  return date

#?----------------------------------GET T-----------------------------------------------------------------------------------------------------------------------
def get_T(device_id):
  response = requests.get(url = f'https://dt.miet.ru/ppo_it/api/temp_hum/{device_id}')  #температура
  return [eval(response.text).get('id') , eval(response.text).get('temperature'), get_time()]


#?----------------------------------GET H-----------------------------------------------------------------------------------------------------------------------
def get_H(device_id):
  response = requests.get(url = f'https://dt.miet.ru/ppo_it/api/temp_hum/{device_id}')  #влажность воздуха
  return [eval(response.text).get('id') , eval(response.text).get('humidity') , get_time()]


#?----------------------------------GET Hb-----------------------------------------------------------------------------------------------------------------------
def get_Hb(device_id):
  response = requests.get(f'https://dt.miet.ru/ppo_it/api/hum/{device_id}')   #влажность почвы
  return [eval(response.text).get('id') , eval(response.text).get('humidity') , get_time()]

#?----------------------------------GET MEAN-----------------------------------------------------------------------------------------------------------------------
def get_mean_values():
  mean_T , mean_H , mean_Hb = 0 , 0 , 0
  for i in range(1 , 4+1):
    response_T_H = requests.get(url = f'https://dt.miet.ru/ppo_it/api/temp_hum/{i}')  #температура #влажность воздуха       #влажность почвы
    mean_H += eval(response_T_H.text).get('humidity')
    mean_T += eval(response_T_H.text).get('temperature')

  for i in range(1 , 6+1):
    response_Hb = requests.get(url = f'https://dt.miet.ru/ppo_it/api/hum/{i}')   
    mean_Hb += eval(response_Hb.text).get('humidity')    
  return [round(mean_H/4 , 2) , round(mean_T/4, 2) , round(mean_Hb/6, 2)]

#----------------------------GET data for graph-----------------------------------------------------------------------------------------------------------------------
# def data_for_T_graph():
#   data = []
#   for i in range(7):
#     a = (get_T(1)[1]  + get_T(2)[1] + get_T(3)[1] + get_T(4)[1])/4
#     data.append(a)
#     time.sleep(1)
#   return(data)
    


# for i in range(4):
#   print(data_for_T_graph())
#   time.sleep(1)

print(get_T(1))
print(get_mean_values())
