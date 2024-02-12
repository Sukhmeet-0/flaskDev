#adding html to flask 
from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')

## result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science =float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['C'])
        ds = float(request.form['ds'])
        total_score = (science + maths + c + ds)/4
    res =''
    if total_score >=50:
        res ='success'
    else:
        res='fail' 
    return redirect(url_for(res,score=total_score))




@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person failed, marks are: "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='success'
    # return result
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug=True)
