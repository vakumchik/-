from db import insert_H , insert_Hb , insert_T , delete_T , delete_H , delete_HB
from get_data import get_T , get_H , get_Hb 

import time



#добавление данных в базу данных
while True:
  insert_T(get_T(1)[0] , get_T(1)[1] , get_T(1)[2])
  insert_H(get_H(1)[0] , get_H(1)[1] , get_H(1)[2])
  insert_Hb(get_Hb(1)[0] , get_Hb(1)[1] , get_Hb(1)[2])

  insert_T(get_T(2)[0] , get_T(2)[1] , get_T(2)[2])
  insert_H(get_H(2)[0] , get_H(2)[1] , get_H(2)[2])
  insert_Hb(get_Hb(2)[0] , get_Hb(2)[1] , get_Hb(2)[2])

  insert_T(get_T(3)[0] , get_T(3)[1] , get_T(3)[2])
  insert_H(get_H(3)[0] , get_H(3)[1] , get_H(3)[2])
  insert_Hb(get_Hb(3)[0] , get_Hb(3)[1] , get_Hb(3)[2])

  insert_T(get_T(4)[0] , get_T(4)[1] , get_T(4)[2])
  insert_H(get_H(4)[0] , get_H(4)[1] , get_H(4)[2])
  insert_Hb(get_Hb(4)[0] , get_Hb(4)[1] , get_Hb(4)[2])

  insert_Hb(get_Hb(5)[0] , get_Hb(4)[1] , get_Hb(4)[2])
  insert_Hb(get_Hb(6)[0] , get_Hb(4)[1] , get_Hb(4)[2])  

  time.sleep(1)



