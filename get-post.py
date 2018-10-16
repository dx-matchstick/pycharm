#encoding: utf-8
from flask import Flask,render_template,request
app = Flask(__name__)

#jump to url define in index.html
@app.route('/')
def index():
    return render_template('index.html')

#get value after /search/
@app.route('/search/')
def search():
    print (request.args)
    return 'search'

# post
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
       return render_template('login.html')
    else :
        return 'post'

# choose port = 9000
if __name__ == '__main__':
    app.run(port=9000,debug = True)

