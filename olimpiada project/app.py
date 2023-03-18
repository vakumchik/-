from flask import Flask, render_template , url_for , request , jsonify , flash
from flask_sqlalchemy import SQLAlchemy

import asyncio
import time

from get_data_from_api import get_H , get_Hb , get_T , getmean_T , getmean_H
from send_data import fork , huming , watering

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QFNY4198'

of_mess = 'open'

@app.route('/_stuff' , methods = ['GET'])
def stuff():

  return jsonify(result=get_T(1)[1])

@app.route('/_stuff2' , methods = ['GET'])
def stuff2():

  return jsonify(result=get_T(2)[1])

@app.route('/_stuff3' , methods = ['GET'])
def stuff3():

  return jsonify(result=get_T(3)[1])

@app.route('/_stuff4' , methods = ['GET'])
def stuff4():

  return jsonify(result=get_T(4)[1])

@app.route('/_stuff5' , methods = ['GET'])
def stuff5():

  return jsonify(result=get_H(1)[1])

@app.route('/_stuff6' , methods = ['GET'])
def stuff6():

  return jsonify(result=get_H(2)[1])

@app.route('/_stuff7' , methods = ['GET'])
def stuff7():

  return jsonify(result=get_H(3)[1])

@app.route('/_stuff8' , methods = ['GET'])
def stuff8():

  return jsonify(result=get_H(4)[1])

@app.route('/_stuff9' , methods = ['GET'])
def stuff9():

  return jsonify(result=get_Hb(6)[1])

@app.route('/_stuff10' , methods = ['GET'])
def stuff10():

  return jsonify(result=get_Hb(5)[1])

@app.route('/_stuff11' , methods = ['GET'])
def stuff11():

  return jsonify(result=get_Hb(4)[1])

@app.route('/_stuff12' , methods = ['GET'])
def stuff12():

  return jsonify(result=get_Hb(3)[1])

@app.route('/_stuff13' , methods = ['GET'])
def stuff13():

  return jsonify(result=get_Hb(2)[1])

@app.route('/_stuff14' , methods = ['GET'])
def stuff14():

  return jsonify(result=get_Hb(1)[1])





optimals = [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]]

@app.route('/controlpanel' , methods=['GET' , "POST"])  
@app.route('/', methods=['GET' , 'POST'])
def index(): 
  
  global of_mess

  if request.method == 'POST':
    OptimalAirHum = request.form.get("OptimalAirHumiINP")
    OptimalAirTemp = request.form.get("OptimalAirTempINP")
    OptimalPlanthumi1 = request.form.get("OptimalPlantHumiINP1")    
    OptimalPlanthumi2 = request.form.get("OptimalPlantHumiINP2")
    OptimalPlanthumi3 = request.form.get("OptimalPlantHumiINP3")
    OptimalPlanthumi4 = request.form.get("OptimalPlantHumiINP4")
    OptimalPlanthumi5 = request.form.get("OptimalPlantHumiINP5")
    OptimalPlanthumi6 = request.form.get("OptimalPlantHumiINP6")    
    global optimals
    if OptimalAirTemp != None:
      optimals[0][0] = OptimalAirTemp

    if OptimalAirHum != None:
      optimals[1][0] = OptimalAirHum  

    if OptimalPlanthumi1 != None:
      optimals[2][0] = OptimalPlanthumi1  

    if OptimalPlanthumi2 != None:
      optimals[3][0] = OptimalPlanthumi2

    if OptimalPlanthumi3 != None:
      optimals[4][0] = OptimalPlanthumi3

    if OptimalPlanthumi4 != None:
      optimals[5][0] = OptimalPlanthumi4

    if OptimalPlanthumi5 != None:
      optimals[6][0] = OptimalPlanthumi5

    if OptimalPlanthumi6 != None:
      optimals[7][0] = OptimalPlanthumi6
    # print(OptimalAirHum ,OptimalAirTemp , OptimalPlanthumi1 , OptimalPlanthumi2)
    return ('', 204 )  





  if of_mess == '111':
    flash('1212121')

  return render_template("index.html" , of_mess = of_mess)

@app.route('/atcntrl' , methods=['GET' , "POST"])  
def atcntrl(): 

  return render_template("airtemp.html")
                                   
@app.route('/airhumi' , methods=['GET' , "POST"])  
def ahcntrl(): 

  return render_template("airhumi.html")

@app.route('/planthumi' , methods=['GET' , "POST"])  
def phcntrl(): 

  return render_template("planthumi.html")

@app.route('/openfork')
def open_fork_js():

  global optimals
  global fork_buttons_text

  if int(optimals[0][0]) != 0 and int(optimals[0][0]) < getmean_T():
    fork(1)
    fork_buttons_text[0] = 'opened'
    fork_buttons_text[1] = 'close'
    print('Fork was open' , fork(1))
  elif int(optimals[0][0]) == 0:
    fork(1)
    fork_buttons_text[0] = 'opened'
    fork_buttons_text[1] = 'close'
    print('Fork was open', fork(1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[0][0]) != 0 and int(optimals[0][0]) > getmean_T():
    fork(0)    
    fork_buttons_text[0] = 'open'
    fork_buttons_text[1] = 'closed'
    print('You cant open fork',  optimals[0][0])


  return ('nothing')

@app.route('/closefork')
def close_fork_js():

  global optimals
  global fork_buttons_text

  if int(optimals[0][0]) != 0 and int(optimals[0][0]) > getmean_T():
    fork(0)
    fork_buttons_text[0] = 'open'
    fork_buttons_text[1] = 'closed'
    print('Fork was closed' , fork(0))
  elif int(optimals[0][0]) == 0:
    fork(0)
    fork_buttons_text[0] = 'open'
    fork_buttons_text[1] = 'closed'
    print('Fork was closed', fork(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[0][0]) != 0 and int(optimals[0][0]) < getmean_T():
    fork(1)
    fork_buttons_text[0] = 'opened'
    fork_buttons_text[1] = 'close'
    print('You cant close fork')


  return ('nothing')

@app.route('/onairhumi')
def on_humi_js():
  global optimals
  global humi_buttons_text

  if int(optimals[1][0]) != 0 and int(optimals[1][0]) < getmean_H():
    huming(1)
    humi_buttons_text[0] = 'on ⬤'
    humi_buttons_text[1] = 'off'
    print('Fork was open' , huming(1))
  elif int(optimals[1][0]) == 0:
    huming(1)
    humi_buttons_text[0] = 'on ⬤'
    humi_buttons_text[1] = 'off'
    print('Fork was open', huming(1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[1][0]) != 0 and int(optimals[1][0]) > getmean_H():
    huming(0)    
    humi_buttons_text[1] = 'off ⬤'
    humi_buttons_text[0] = 'on'
    print('You cant open fork')


  return ('nothing')

@app.route('/offairhumi')
def off_humi_js():
  global optimals
  global fork_buttons_text

  if int(optimals[1][0]) != 0 and int(optimals[1][0]) > getmean_H():
    huming(0)
    humi_buttons_text[0] = 'on'
    humi_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[1][0]) == 0:
    huming(0)
    humi_buttons_text[0] = 'on'
    humi_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[1][0]) != 0 and int(optimals[1][0]) < getmean_H():
    huming(1)
    humi_buttons_text[0] = 'on ⬤'
    humi_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')


fork_buttons_text=['open' , 'close']

humi_buttons_text=['on'   , 'off']

phumi1_buttons_text=['on'   , 'off']
phumi2_buttons_text=['on'   , 'off']
phumi3_buttons_text=['on'   , 'off']
phumi4_buttons_text=['on'   , 'off']
phumi5_buttons_text=['on'   , 'off']
phumi6_buttons_text=['on'   , 'off']
def bttext():

  global fork_buttons_text
  global humi_buttons_text
  global phumi1_buttons_text
  global phumi2_buttons_text
  global phumi3_buttons_text
  global phumi4_buttons_text
  global phumi5_buttons_text
  global phumi6_buttons_text

  return [fork_buttons_text , humi_buttons_text ,phumi1_buttons_text ,phumi2_buttons_text , phumi3_buttons_text , phumi4_buttons_text , phumi5_buttons_text , phumi6_buttons_text]





@app.route('/open_ed' , methods = ['GET'])
def fk_open():

  return jsonify(result=bttext()[0][0])

@app.route('/close_ed' , methods = ['GET'])
def fk_close():

  return jsonify(result=bttext()[0][1])

@app.route('/on_ed' , methods = ['GET'])
def humi_on():

  return jsonify(result=bttext()[1][0])

@app.route('/off_ed' , methods = ['GET'])
def humi_off():

  return jsonify(result=bttext()[1][1])

@app.route('/p_on_ed' , methods = ['GET'])
def p_humi_on():

  return jsonify(result=bttext()[2][0])

@app.route('/p_off_ed' , methods = ['GET'])
def p_humi_off():

  return jsonify(result=bttext()[2][1])

@app.route('/p2_on_ed' , methods = ['GET'])
def p_humi_on2():

  return jsonify(result=bttext()[3][0])

@app.route('/p2_off_ed' , methods = ['GET'])
def p_humi_off2():

  return jsonify(result=bttext()[3][1])

@app.route('/p3_on_ed' , methods = ['GET'])
def p_humi_on3():

  return jsonify(result=bttext()[4][0])

@app.route('/p3_off_ed' , methods = ['GET'])
def p_humi_off3():

  return jsonify(result=bttext()[4][1])

@app.route('/p4_on_ed' , methods = ['GET'])
def p_humi_on4():

  return jsonify(result=bttext()[5][0])

@app.route('/p4_off_ed' , methods = ['GET'])
def p_humi_off4():

  return jsonify(result=bttext()[5][1])

@app.route('/p5_on_ed' , methods = ['GET'])
def p_humi_on5():

  return jsonify(result=bttext()[6][0])

@app.route('/p5_off_ed' , methods = ['GET'])
def p_humi_off5():

  return jsonify(result=bttext()[6][1])

@app.route('/p6_on_ed' , methods = ['GET'])
def p_humi_on6():

  return jsonify(result=bttext()[7][0])

@app.route('/p6_off_ed' , methods = ['GET'])
def p_humi_off6():

  return jsonify(result=bttext()[7][1])

#?---------------------------------------

@app.route('/onplanthumi1')
def on_planthumi_1():
  global optimals
  global phumi1_buttons_text

  if int(optimals[2][0]) != 0 and int(optimals[2][0]) < get_Hb(1)[0]:
    watering(1 , 1)
    phumi1_buttons_text[0] = 'on ⬤'
    phumi1_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[2][0]) == 0:
    watering(1 , 1)
    phumi1_buttons_text[0] = 'on ⬤'
    phumi1_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[2][0]) != 0 and int(optimals[2][0]) > get_Hb(1)[0]:
    watering(1 , 0)    
    phumi1_buttons_text[1] = 'off ⬤'
    phumi1_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi1')
def off_planthumi_1():
  global optimals
  global fork_buttons_text

  if int(optimals[2][0]) != 0 and int(optimals[2][0]) > get_Hb(1)[0]:
    huming(0)
    phumi1_buttons_text[0] = 'on'
    phumi1_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[2][0]) == 0:
    huming(0)
    phumi1_buttons_text[0] = 'on'
    phumi1_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[2][0]) != 0 and int(optimals[2][0]) < get_Hb(1)[0]:
    huming(1)
    phumi1_buttons_text[0] = 'on ⬤'
    phumi1_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')


@app.route('/onplanthumi2')
def on_planthumi_2():
  global optimals
  global phumi1_buttons_text

  if int(optimals[3][0]) != 0 and int(optimals[3][0]) < get_Hb(2)[0]:
    watering(2 , 1)
    phumi2_buttons_text[0] = 'on ⬤'
    phumi2_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[3][0]) == 0:
    watering(2 , 1)
    phumi2_buttons_text[0] = 'on ⬤'
    phumi2_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[3][0]) != 0 and int(optimals[3][0]) > get_Hb(2)[0]:
    watering(2 , 0)    
    phumi2_buttons_text[1] = 'off ⬤'
    phumi2_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi2')
def off_planthumi_2():
  global optimals
  global fork_buttons_text

  if int(optimals[3][0]) != 0 and int(optimals[3][0]) > get_Hb(2)[0]:
    watering(2 , 0)
    phumi2_buttons_text[0] = 'on'
    phumi2_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[3][0]) == 0:
    watering(2 , 0)
    phumi2_buttons_text[0] = 'on'
    phumi2_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[3][0]) != 0 and int(optimals[3][0]) < get_Hb(2)[0]:
    watering(2 , 1)
    phumi2_buttons_text[0] = 'on ⬤'
    phumi2_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')

@app.route('/onplanthumi3')
def on_planthumi_3():
  global optimals
  global phumi1_buttons_text

  if int(optimals[4][0]) != 0 and int(optimals[4][0]) < get_Hb(3)[0]:
    watering(3 , 1)
    phumi3_buttons_text[0] = 'on ⬤'
    phumi3_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[4][0]) == 0:
    watering(3 , 1)
    phumi3_buttons_text[0] = 'on ⬤'
    phumi3_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[4][0]) != 0 and int(optimals[4][0]) > get_Hb(3)[0]:
    watering(3 , 0)    
    phumi3_buttons_text[1] = 'off ⬤'
    phumi3_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi3')
def off_planthumi_3():
  global optimals
  global fork_buttons_text

  if int(optimals[4][0]) != 0 and int(optimals[4][0]) > get_Hb(3)[0]:
    watering(3 , 0)
    phumi3_buttons_text[0] = 'on'
    phumi3_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[4][0]) == 0:
    watering(3 , 0)
    phumi3_buttons_text[0] = 'on'
    phumi3_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[4][0]) != 0 and int(optimals[4][0]) < get_Hb(3)[0]:
    watering(3 , 1)
    phumi3_buttons_text[0] = 'on ⬤'
    phumi3_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')

@app.route('/onplanthumi4')
def on_planthumi_4():
  global optimals
  global phumi1_buttons_text

  if int(optimals[5][0]) != 0 and int(optimals[5][0]) < get_Hb(4)[0]:
    watering(4 , 1)
    phumi4_buttons_text[0] = 'on ⬤'
    phumi4_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[5][0]) == 0:
    watering(4 , 1)
    phumi4_buttons_text[0] = 'on ⬤'
    phumi4_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[5][0]) != 0 and int(optimals[5][0]) > get_Hb(4)[0]:
    watering(4 , 0)    
    phumi4_buttons_text[1] = 'off ⬤'
    phumi4_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi4')
def off_planthumi_4():
  global optimals
  global fork_buttons_text

  if int(optimals[5][0]) != 0 and int(optimals[5][0]) > get_Hb(4)[0]:
    watering(4 , 0)
    phumi4_buttons_text[0] = 'on'
    phumi4_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[5][0]) == 0:
    watering(4 , 0)
    phumi4_buttons_text[0] = 'on'
    phumi4_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[5][0]) != 0 and int(optimals[5][0]) < get_Hb(4)[0]:
    watering(4 , 1)
    phumi4_buttons_text[0] = 'on ⬤'
    phumi4_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')

@app.route('/onplanthumi5')
def on_planthumi_5():
  global optimals
  global phumi1_buttons_text

  if int(optimals[6][0]) != 0 and int(optimals[6][0]) < get_Hb(5)[0]:
    watering(5 , 1)
    phumi5_buttons_text[0] = 'on ⬤'
    phumi5_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[6][0]) == 0:
    watering(5 , 1)
    phumi5_buttons_text[0] = 'on ⬤'
    phumi5_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[6][0]) != 0 and int(optimals[6][0]) > get_Hb(5)[0]:
    watering(5 , 0)    
    phumi5_buttons_text[1] = 'off ⬤'
    phumi5_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi5')
def off_planthumi_5():
  global optimals
  global fork_buttons_text

  if int(optimals[6][0]) != 0 and int(optimals[6][0]) > get_Hb(5)[0]:
    watering(5 , 0)
    phumi5_buttons_text[0] = 'on'
    phumi5_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[6][0]) == 0:
    watering(5 , 0)
    phumi5_buttons_text[0] = 'on'
    phumi5_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[6][0]) != 0 and int(optimals[6][0]) < get_Hb(5)[0]:
    watering(5 , 1)
    phumi5_buttons_text[0] = 'on ⬤'
    phumi5_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')

@app.route('/onplanthumi6')
def on_planthumi_6():
  global optimals
  global phumi1_buttons_text

  if int(optimals[6][0]) != 0 and int(optimals[6][0]) < get_Hb(6)[0]:
    watering(6 , 1)
    phumi6_buttons_text[0] = 'on ⬤'
    phumi6_buttons_text[1] = 'off'
    print('Fork was open' , watering(1 , 1))
  elif int(optimals[6][0]) == 0:
    watering(6 , 1)
    phumi6_buttons_text[0] = 'on ⬤'
    phumi6_buttons_text[1] = 'off'
    print('Fork was open', watering(1 , 1))  # if optimals[0][0]!=0 and optima
  elif int(optimals[6][0]) != 0 and int(optimals[6][0]) > get_Hb(6)[0]:
    watering(6 , 0)    
    phumi6_buttons_text[1] = 'off ⬤'
    phumi6_buttons_text[0] = 'on'
    print('You cant on watering 1')


  return ('nothing')

@app.route('/offplanthumi6')
def off_planthumi_6():
  global optimals
  global fork_buttons_text

  if int(optimals[7][0]) != 0 and int(optimals[7][0]) > get_Hb(6)[0]:
    watering(6 , 0)
    phumi6_buttons_text[0] = 'on'
    phumi6_buttons_text[1] = 'off ⬤'
    print('Fork was closed' , huming(0))
  elif int(optimals[7][0]) == 0:
    watering(6 , 0)
    phumi6_buttons_text[0] = 'on'
    phumi6_buttons_text[1] = 'off ⬤'
    print('Fork was closed', huming(0))  # if optimals[0][0]!=0 and optima
  elif int(optimals[7][0]) != 0 and int(optimals[7][0]) < get_Hb(6)[0]:
    watering(6 , 1)
    phumi6_buttons_text[0] = 'on ⬤'
    phumi6_buttons_text[1] = 'off'
    print('You cant close fork')


  return ('nothing')

if __name__ == '__main__':
  app.run(debug=True)