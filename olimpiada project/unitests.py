from get_data_from_api import get_Hb

def get_data_hb():
  mean = 0
  for i in range(1 , 6+1):
    mean += get_Hb(i)[1]
  return mean/6

print(get_data_hb())