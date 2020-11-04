from flask import Flask, request, render_template
import json
from src.process_and_predict import process_and_predict

app = Flask(__name__)

def predict(sentence):
    status=''
    try:
        processed_sentence=process_and_predict.process(sentence)
        prediction = process_and_predict.predict(processed_sentence)
    except:
        status='fail'

    if status is not 'fail':
        status='prediction : {}'.format(prediction)
    
    return status

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        details=request.form

        if details['form_type'] == 'predict':
            return predict(details['sentence'])
   
    return render_template('index.html')

if __name__== '__main__':
	app.run(host='0.0.0.0')
