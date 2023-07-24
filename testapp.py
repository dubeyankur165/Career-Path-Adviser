from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def career():
    return render_template("index.html")

@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      res = result.to_dict(flat=True)
      arr1 = res.values()
      arr = ([int(value) for value in arr1])
      data = np.array(arr)
      data = data.reshape(1,-1)
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))

      predictions = loaded_model.predict(data)
      
      pred = loaded_model.predict_proba(data)
      newpred  = pred

      pred = pred >= 0
      output={}
      i=0
      j=0
      outputNames = {}
      jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}
      
      while j<17:
        if pred[i,j]:
            output[j]=newpred[i,j]
        j += 1
      for key, values in output.items():
          outputNames[key] = jobs_dict[key]
      k=0
      finalOutput = {}
      finalArr=[]
      for key, values in outputNames.items():
          finalOutput[values]  = output[key]
          finalArr.append([values,output[key]])
      finalArr = sorted(finalArr,key=lambda l:l[1], reverse=True)
      return render_template("testafter.html",job1 = finalArr[0][0],job2 = finalArr[1][0],job3 = finalArr[2][0],val1 = round(finalArr[0][1]*100,2),val2 = round(finalArr[1][1]*100,2),val3 = round(finalArr[2][1]*100,2))
          
   else:
      return "Hello"


if __name__ == '__main__':
   app.run(debug = True)
