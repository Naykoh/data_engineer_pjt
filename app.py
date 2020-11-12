from flask import Flask, request, render_template
from src.process_and_predict import process_and_predict


app = Flask(__name__)

def predict(sentence):
    status='success'
    try:
        prediction = process_and_predict.predict(sentence)
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
            prediction = predict(details['sentence'])
            if (prediction =='prediction : positive'):   
                img_path = 'sourire.png'
            elif (prediction =='prediction : neutral'):
                img_path = 'neutral.png'
            else:
                img_path ='triste.png'

            return render_template('index.html',result=prediction,face=img_path)


    return render_template('index.html',result='submit a sentence to predict',face='neutral.png')

if __name__== '__main__':
    app.run(host='0.0.0.0')
