from flask import Flask, render_template,Response, request, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import Bisection_Method_Lib
import stringhandling
from sympy import *
import numpy as np
import io
from fractions import Fraction
app = Flask(__name__)
#global Var
@app.route('/')
def home():
    # if os.path.isfile('./templates/solArr.txt'):
    #     os.remove('./templates/solArr.txt')
    # if os.path.isfile('./templates/errArr.txt'):
    #     os.remove('./templates/errArr.txt')
    #hoạt động nhập xuất file để kết nối flask và javascripts
    #thông qua promise fs vô cùng thiếu ổn định
    #  nên em đã sử dụng build in của flask
    return render_template("index.html")


@app.route('/plot_png')


def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    #Response này có kiểu dữ liệu trả về html không đọc 
    # được nên em dẫn link trực tiếp đến hình ảnh
    img =  Response(output.getvalue(), mimetype='image/png')
    return render_template("plot_png.html", img )
def create_figure():
    global f_input,a,b
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x = symbols('x')
    t = symbols('t')
    f = lambda x : eval (f_input)
    X = np.linspace(a,b,int((b-a)/3*101))
    Y = [f(x) for x in X]
    axis.plot(X, Y)
    return fig

@app.route('/calc' , methods=['POST' , 'GET'])
def calc():
    global f_input,n,a,b, solArr, errArr,pp, f_latex,pp
    f_input = request.form['f(x)']
    f_input = stringhandling.stringhandling(f_input)
    n = int(request.form['n_input'])
    txt = request.form['ab_input']
    pp = str(request.form['choosen'])
    strs = txt.split (',')
    a , b = eval ( strs [0]) , eval ( strs [1])
    a , b = float(a), float(b)
    x = symbols('x')
    f1 = eval(f_input)
    f_latex = latex(f1)
    if(Bisection_Method_Lib.checkCondition(f_input,a,b,n,pp)):
        if(pp == "chia đôi"):
            solArr , errArr = Bisection_Method_Lib.bisection (  f_input, a , b , n )
        if(pp == "newton"):
            solArr , errArr = Bisection_Method_Lib.newton(f_input , a , b , n)
        if(pp == "newton cải biên"):
            solArr , errArr = Bisection_Method_Lib.newtonExplain(  f_input , a , b , n)
        if(pp == "lặp điểm bất động"):
            solArr , errArr = Bisection_Method_Lib.repeatFixedPoint(  f_input , a , b , n)
    if(Bisection_Method_Lib.checkCondition(f_input , a , b , n,pp) == False):
        return render_template("result1.html", f = f_input, n = n,a=a,b=b, pp = pp, f_latex = f_latex)
    sol = solArr[-1]
    err = errArr[-1]
    return render_template('result.html', f = f_input, n = n, sol = sol, err = err,a=a,b=b, pp = pp, f_latex= f_latex)


@app.route('/table', methods = ['GET', 'POST'])
def table():
    global f_input,n,a,b, solArr, errArr,pp
    # with open("./templates/solArr.txt", "w") as fo:
    #     for _ in range (len(solArr)):
    #         fo.write( str(solArr[_])+ ",")
    # with open("./templates/errArr.txt", "w") as fo:
    #     for _ in range (len(errArr)):
    #         fo.write( str(errArr[_])+ ",")
    return render_template("table.html", f = f_input, a= a, b=b, n=n, solArr = solArr, errArr = errArr)

if __name__ == '__main__':
    app.run() #dùng khi build web
    # init_gui(app) #dùng khi muốn build ra ứng dụng