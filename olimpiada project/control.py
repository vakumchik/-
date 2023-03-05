from db import insert_H , insert_Hb , insert_T
from get_data_from_api import get_T , get_H , get_Hb , get_mean_values

import time



#добавление данных в базу данных
while True:
  for i in range(1 ,4+1):
    insert_T(get_T(i)[0] , get_T(i)[1] , get_T(i)[2] , get_mean_values()[1])
    insert_H(get_H(i)[0] , get_H(i)[1] , get_H(i)[2] , get_mean_values()[0])
  for i in range(1 , 6+1):
    insert_Hb(get_Hb(i)[0] , get_Hb(i)[1] , get_Hb(i)[2] , get_mean_values()[2])

  time.sleep(1)



