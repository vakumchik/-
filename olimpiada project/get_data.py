import requests
import time
from datetime import datetime
now = datetime.now()
date = '"'+ now.strftime('%Y-%m-%d %H:%M:%S')+'"'

#?----------------------------------GET T-----------------------------------------------------------------------------------------------------------------------
def get_T(device_id):
  response = requests.get(url = f'https://dt.miet.ru/ppo_it/api/temp_hum/{device_id}')  #температура
  return [eval(response.text).get('id') , eval(response.text).get('temperature') , date]


#?----------------------------------GET H-----------------------------------------------------------------------------------------------------------------------
def get_H(device_id):
  response = requests.get(url = f'https://dt.miet.ru/ppo_it/api/temp_hum/{device_id}')  #влажность воздуха
  return [eval(response.text).get('id') , eval(response.text).get('humidity') , date]


#?----------------------------------GET Hb-----------------------------------------------------------------------------------------------------------------------
def get_Hb(device_id):
  response = requests.get(f'https://dt.miet.ru/ppo_it/api/hum/{device_id}')   #влажность почвы
  return [eval(response.text).get('id') , eval(response.text).get('humidity') , date]

#?----------------------------GET data for graph-----------------------------------------------------------------------------------------------------------------------
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

