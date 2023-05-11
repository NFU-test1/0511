from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_python():
    return "<p>Hello, python!</p>"

@app.route("/name/<name>")
def name(name):
    print('Type:',type(name))
    return name

@app.route("/number/<int:number>")
def number(number):
    x = [i for i in range(number)]
    print('Type:',type(number))
    return f"{x}"

@app.route("/page")
def page():
    x = '1234'
    dict1 = {'abc':1324,'name':'tom'}
    return render_template("page.html",testx=x,dict1=dict1)

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('account')
        password = request.form.get('password')
        if name == 'admin' and password == '1234':
            type = '成功'
            return render_template("page2.html",id=name,ps=password,type=type)
        else:
            type = '登入失敗'
            return render_template("login.html",type=type)
    else:
        return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)