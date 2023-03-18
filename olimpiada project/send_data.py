import requests

#?----------------------------------OPEN FORK--------------------------------------------------------------------------------
def fork(state_value):
  response = requests.patch(f'https://dt.miet.ru/ppo_it/api/fork_drive?state={state_value}')      #управление форточками  
  return eval(response.text)

#?----------------------------------WATERING--------------------------------------------------------------------------------
def watering(device_id , state_value):
  response = requests.patch(f'https://dt.miet.ru/ppo_it/api/watering?id={device_id}&state={state_value}')   #управление поливом 
  return eval(response.text) 

#?-----------------------------------HUMI--------------------------------------------------------------------------------
def huming(state_value):
  response = requests.patch(f' https://dt.miet.ru/ppo_it/api/total_hum?state={state_value}')   #управление системой увлажнения   
  return eval(response.text)

print(fork(1))