from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, render_template,Response, request, url_for
from matplotlib.figure import Figure
import Bisection_Method_Lib
import stringhandling
from sympy import *
import numpy as np
import io

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")

# @app.route('/GiaiBaiTap')
# def GiaiBaiTap():
#     return render_template("GiaiBaiTapNewTon.html", n = n, sol = sol, err = err,a=a,b=b, pp = pp, f_latex= f_latex, sll = sll,  min_df = min_df, max_df = max_df, min_ddf = min_ddf, max_ddf = max_ddf, f_a = f_a, f_b = f_b)


@app.route('/plot_png')

def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    #Response này có kiểu dữ liệu trả về html không đọc 
    # được nên em dẫn link trực tiếp đến hình ảnh
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
    global f_input,n,a,b, solArr, errArr,pp, f_latex,n_choose, sllArr, min_df, max_df, min_ddf, max_ddf, f_a , f_b, sol, err, sll,x0
    f_input = request.form['f(x)']
    f_input = stringhandling.stringhandling(f_input)
    n_choose  = str(request.form['n_choose'])
    n = str(request.form['n_input'])
    n = stringhandling.stringhandling(n)
    n = eval(n)
    txt = request.form['ab_input']
    pp = str(request.form['choosen'])
    strs = txt.split (',')
    a , b = eval ( strs [0]) , eval ( strs [1])
    a , b = float(a), float(b)
    x = symbols('x')
    t = symbols('t')
    f1 = eval(f_input)
    f_latex = latex(f1)
    f = lambda x : eval (f_input)
    df = lambda x : f(t).diff(t,1).subs(t,x)
    ddf = lambda x: f(t).diff(t,2).subs(t,x)
    if(b - a <=0 ):
        a, b = b ,a
    if(Bisection_Method_Lib.checkCondition(f_input,a,b,pp)):
        if(pp == "chia đôi"):
            solArr , errArr, sllArr = Bisection_Method_Lib.bisection (  f_input, a , b , n, n_choose )
        if(pp == "Newton"):
            solArr , errArr, sllArr,min_df, max_df, min_ddf, max_ddf, f_a , f_b, x0, M,m = Bisection_Method_Lib.Newton(f_input , a , b , n, n_choose )
        if(pp == "Newton cải biên"):
            solArr , errArr, sllArr,min_df, max_df, min_ddf, max_ddf, f_a , f_b, x0, M,m= Bisection_Method_Lib.NewtonExplain(  f_input , a , b , n, n_choose )
        if(pp == "lặp điểm bất động"):
            solArr , errArr, sllArr = Bisection_Method_Lib.repeatFixedPoint(  f_input , a , b , n, n_choose )
    if(Bisection_Method_Lib.checkCondition(f_input , a , b , pp) == False):
        return render_template("result1.html", f = f_input,a=a,b=b, pp = pp, f_latex = f_latex)
    sol = str(solArr[-1])
    err = str(errArr[-1])
    sll = sllArr[-1]
    err = stringhandling.handleFloat(err)
    sol = stringhandling.handleFloat(sol)
    if(pp == "Newton" or pp == "Newton cải biên"):
        x_n = symbols('x_n')
        minmax_df = min_df * max_df 
        minmax_ddf = min_ddf * max_ddf
        f_ab = f_a * f_b
        max_ddf = "{:.2f}".format(max_ddf)
        min_ddf = "{:.2f}".format(min_ddf)
        max_df = "{:.2f}".format(max_df)
        min_df = "{:.2f}".format(min_df)
        minmax_ddf = "{:.2f}".format(minmax_ddf)
        minmax_df = "{:.2f}".format(minmax_df)
        M = "{:.2f}".format(M)
        m = "{:.2f}".format(m)
        f1 = str(df(x))
        f1 = eval(f1)
        df_latex = latex(f1)
        f1 = str(ddf(x))
        f1 = eval(f1)
        ddf_latex = latex(f1)
        f1 = str(f(x_n))
        f1 = eval(f1)
        fx_n_latex = latex(f1)
        if(pp == "Newton"):
            f1 = str(df(x_n))
            f1 = eval(f1)
            dfx_n_latex = latex(f1)
            return render_template("GiaiBaiTapNewton.html",dfx_n_latex = dfx_n_latex,fx_n_latex = fx_n_latex,  M=M, m=m,x0 = x0, f_ab = f_ab, minmax_ddf = minmax_ddf ,minmax_df=minmax_df,ddf_latex = ddf_latex,df_latex = df_latex, n = n, sol = sol, err = err,a=a,b=b, pp = pp, f_latex= f_latex, sll = sll,  min_df = min_df, max_df = max_df, min_ddf = min_ddf, max_ddf = max_ddf, f_a = f_a, f_b = f_b)
        if(pp == "Newton cải biên"):
            f_x0 = f(x0) 
            f_x0 = "{:.2f}".format(f_x0)
            return render_template("GiaiBaiTapNewtonMoRong.html",f_x0 = f_x0,fx_n_latex = fx_n_latex,  M=M, m=m,x0 = x0, f_ab = f_ab, minmax_ddf = minmax_ddf ,minmax_df=minmax_df,ddf_latex = ddf_latex,df_latex = df_latex, n = n, sol = sol, err = err,a=a,b=b, pp = pp, f_latex= f_latex, sll = sll,  min_df = min_df, max_df = max_df, min_ddf = min_ddf, max_ddf = max_ddf, f_a = f_a, f_b = f_b)
    return render_template('result.html', n = n, sol = sol, err = err,a=a,b=b, pp = pp, f_latex= f_latex, sll = sll)




@app.route('/table', methods = ['GET', 'POST'])

def table():
    global f_input,n,a,b, solArr, errArr,pp
    return render_template("table.html", f = f_input, a= a, b=b, n=n, solArr = solArr, errArr = errArr)

# from routes import *
# from pyfladesk import init_gui #dùng khi build ứng dụng
if __name__ == '__main__':
    app.run()       #dùng khi build web
    # init_gui(app) #dùng khi muốn build ra ứng dụng