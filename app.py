from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('modelproyekrupiah.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')


@app.route('/')
def index():
    return render_template('index.html', Price=0)


@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''

    weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem, ram, RearCam, Front_Cam, battery = [
        x for x in request.form.values()]
    data = []

    data.append(float(weight))
    data.append(float(resoloution))
    data.append(int(ppi))
    data.append(int(cpu_core))
    data.append(float(cpu_freq))
    data.append(float(internal_mem))
    data.append(float(ram))
    data.append(float(RearCam))
    data.append(float(Front_Cam))
    data.append(int(battery))
    prediction = model.predict([data])
    output = round(float(prediction[0]), 2)
    return render_template('index.html', Price=output, weight=weight, resoloution=resoloution, ppi=ppi, cpu_core=cpu_core, cpu_freq=cpu_freq, internal_mem=internal_mem, ram=ram, RearCam=RearCam, Front_Cam=Front_Cam, battery=battery)


if __name__ == '__main__':
    app.run(debug=True)
