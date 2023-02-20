from flask import Flask, render_template , url_for , request , jsonify
from flask_sqlalchemy import SQLAlchemy

import asyncio
import time

from get_data import get_H , get_Hb , get_T



app = Flask(__name__)


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








@app.route('/controlpanel' , methods=['GET' , "POST"])  
@app.route('/', methods=['GET' , 'POST'])
def index(): 
  


  data = [65, 59, 80, 81, 56, 55, 40]

  if request.method == 'POST':
    OptimalAirHum = request.form.get("OptimalAirHumiINP")
    OptimalAirTemp = request.form.get("OptimalAirTempINP")
    OptimalPlanthumi1 = request.form.get("OptimalPlantHumiINP1")    
    OptimalPlanthumi2 = request.form.get("OptimalPlantHumiINP2")
    OptimalPlanthumi3 = request.form.get("OptimalPlantHumiINP3")
    OptimalPlanthumi4 = request.form.get("OptimalPlantHumiINP4")
    OptimalPlanthumi5 = request.form.get("OptimalPlantHumiINP5")
    OptimalPlanthumi6 = request.form.get("OptimalPlantHumiINP6")    



    print(OptimalAirHum ,OptimalAirTemp , OptimalPlanthumi1 , OptimalPlanthumi2)
    return ('', 204 )  
  
  else:   
    return render_template("index.html" , data=data)

@app.route('/atcntrl' , methods=['GET' , "POST"])  
def atcntrl(): 

  return render_template("airtemp.html")
                                   



if __name__ == '__main__':
  app.run(debug=True)