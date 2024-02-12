from flask import Flask as fsk 
app = fsk(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to my youtube channel</h1>'
@app.route('/sukh')
def sukh():
    return '<h1>Welcome Sukhmeet Singh </h1>'

if __name__=='__main__':
    app.run(debug=True)