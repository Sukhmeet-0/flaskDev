#building url dyanamically 
# variable rules and url building
from flask import Flask as fsk 
from flask import redirect,url_for
app = fsk(__name__)
@app.route('/')
def welcome():
    return '<h1> Welcome Sukhmeet Singh</h1>'
@app.route('/success/<int:score>')
def success(score):
    return "The person passed, marks are: "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person failed, marks are: "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<33:
        result='fail'
    else:
        result='success'
    # return result
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run(debug=True)