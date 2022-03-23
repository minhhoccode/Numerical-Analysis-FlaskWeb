from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt
import array as arr

def checkCondition(f_input , a , b , n, pp):
    # Kiểm Tra điều kiện thực hiện phương pháp


    x = symbols('x')
    t = symbols('t')
    f = lambda x : eval (f_input)
    X = np.linspace(a,b,int((b-a)/3*101))
    Y = [f(x) for x in X]
    df = lambda x : f(t).diff(t,1).subs(t,x)
    ddf = lambda x: f(t).diff(t,2).subs(t,x)
    dY = [df(x) for x in X]
    ddY = [ddf(x) for x in X]


    if pp=="chia đôi":
        if(min(dY)*max(dY)>0): # Giả sử hàm số liên tục thì tồn tại nghiệm x khi và chỉ khi min max trái dấu
            return False
        if(f(a)*f(b)>0):
            return False
        return True

    if(pp == "newton"):
        if min(dY)*max(dY)<0:
            return False
        if min(ddY)*max(ddY)<0:
            return False
        if f(a)*f(b) > 0:
            return False
        return True
        
    if(pp == "newton cải biên"):
        if min(dY)*max(dY)<0:
            return False
        if min(ddY)*max(ddY)<0:
            return False
        if f(a)*f(b) > 0:
            return False
        return True


    if(pp == "lặp điểm bất động"):
        x = symbols ('x')
        t = symbols ('t')
        g = lambda x: eval(f_input)
        X = np.linspace(a,b,int((b-a)/3*101))
        Y = [g(x) for x in X]
        if(max(Y)>b or min(Y) < a):
            return False
        dg = lambda x: g(t).diff().subs(t,x)
        dY = [dg(x) for x in X]
        if(max(dY)>=1):
            return False
        return True


def bisection ( f_input , a , b , n):
    sol, err = arr.array('d'),arr.array('d')
    f = lambda x : eval (f_input)
    for _ in range ( n ):
        c = ( a + b ) / 2
        if f ( a ) * f ( c ) < 0:
            b = c
        else :
            a = c
        sol.append(a)
        err.append(b-a)
        print(_+1, sol[_], err[_])
    return sol, err


def newton(f_input, a, b, n):
    sol, err = arr.array('d'),arr.array('d')
    x = symbols('x')
    t = symbols('t')
    f = lambda x : eval (f_input)
    df = lambda x : f(t).diff().subs(t,x)
    ddf = lambda x: f(t).diff(t,2).subs(t,x)
    X = np.linspace(a,b,int((b-a)/3*101))
    dY = [df(x) for x in X]
    ddY = [ddf(x) for x in X]
    #df, ddf không đổi dấu 
    # b) Phương pháp newton sau 3 bước lặp
    # c) tìm sai số của câu b
    #chọn x0 sao cho f(x0)*ddf>0 (chọn 1 trong 2 cận a,b )
    if(f(a)*ddf(a)>=0):
        x0 = a
    if(f(b)*ddf(a)>=0):
        x0 = b
    M = max(ddY)
    m = min( abs(df(a)),abs(df(b)))


    for _ in range (n):
        x = x0 - f(x0)/df(x0)
        ss = ( M / (2*m) ) * (x - x0)**2
        x0 = x
        print(_+1,x,ss)
        sol.append(x)
        err.append(ss)
    return sol, err

def newtonExplain(f_input, a, b, n):


    sol, err = arr.array('d'),arr.array('d')
    x = symbols('x')
    t = symbols('t')
    f = lambda x : eval (f_input)
    df = lambda x : f(t).diff().subs(t,x)
    ddf = lambda x: f(t).diff(t,2).subs(t,x)
    X = np.linspace(a,b,int((b-a)/3*101))
    dY = [df(x) for x in X]
    ddY = [ddf(x) for x in X]
    if(f(a)*ddf(a)>0):
        x0 = a
    if(f(b)*ddf(a)>0):
        x0 = b
    M = max(ddY)
    m = min( abs(df(a)), abs(df(b)) )
    for _ in range (n):
        x = x0 - f(x0)/df(b)
        ss = ( M / (2*m) ) * (x - x0)**2
        x0 = x
        sol.append(x)
        err.append(ss)
    return sol, err

def repeatFixedPoint(f_input , a , b , n):
    sol, err = arr.array('d'),arr.array('d')
    x = symbols ('x')
    t = symbols ('t')
    g = lambda x: eval(f_input)
    X = np.linspace(a,b,int((b-a)/3*101))
    Y = [g(x) for x in X]
    dg = lambda x: g(t).diff().subs(t,x)
    dY = [dg(x) for x in X]
    q = max(dY)
    x0 = (a + b)/2
    for _ in range (n):
        x = x0
        x = g(x)
        ss = q/(1-q)*abs(x-x0)
        x0 = x 
        sol.append(x)
        err.append(ss)
        print(_+1, x, ss)
    return sol, err