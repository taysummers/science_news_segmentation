from flask import Flask, render_template, request
import pickle
import pandas as pd
from model import SegmentModel
app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# home page
@app.route('/')
def index():
    return render_template('template.html')

@app.route('/seg0')
def profile_0():
    return render_template('segment0.html')

@app.route('/seg1')
def profile_1():
    return render_template('segment1.html')

@app.route('/seg2')
def profile_2():
    return render_template('segment2.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/results', methods = ['POST'])
def results():
    gender = int(request.form['GenderRadio'])
    age = int(request.form['AgeRadio'])
    edu = int(request.form['EduRadio'])
    busnews = float(request.form['NewsInt1'])
    scinews = float(request.form['NewsInt2'])
    govnews = float(request.form['NewsInt3'])
    sciwhy = float(request.form['SciWhyRadio'])
    list1 = float(request.form['List1b'])
    source1 = float(request.form['Source1'])


    d = {'PPGENDER': [gender], 'TOPICINT_e': [scinews],
        'ppagecat': [age], 'PPEDUCAT': [edu],
        'SCIWHY_e': [sciwhy], 'TOPICINT_d': [busnews],
        'LIST1_b': [list1], 'TOPICINT_a': [govnews], 'SOURCE1': [source1]}

    X_new = pd.DataFrame(data = d)
    prediction = model.predict(X_new)

    if prediction == [0]:
        return render_template('segment0.html')

    elif prediction ==[1]:
        return render_template('segment1.html')

    elif prediction == [2]:
        return render_template('segment2.html')

    else:
        return render_template('results.html',
        predict = 'There Seems To Be an Error')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084, debug=True)
