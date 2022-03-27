from sympy import latex

def stringhandling(f_input):
    num = ['0','1','2','3','4','5','6','7','8','9']
    f_input = f_input.replace("^","**")
    f_input = f_input.replace(" ","")
    for i in range(0, len(f_input)-1):
        for j in range (10):
            if f_input[i] == "x" and f_input[i+1] == num[j]:
                f_input = f_input.replace(f_input[i]+ num[j],"x*" + num[j])
            if f_input[i+1] == "x" and f_input[i] == num[j]:
                f_input = f_input.replace(num[j]+f_input[i+1], num[j]+"*x")
            if f_input[i+1] == "e" and f_input[i] == num[j]:
                f_input = f_input.replace(num[j]+f_input[i+1], num[j]+"*")
    # print(f_input)
    
    return f_input
def handleFloat(STRING):
    check = False
    STRING = str(STRING)
    for i in range (len(STRING)):
        if STRING[i] == "e":
            check = True
    if check == True:
        STRING = STRING.replace("e","*10**(")
        STRING = STRING + ")"
        STRING = STRING.replace("-0", "-")
        STRING = eval(STRING)
        STRING = latex(STRING)
    return STRING
def handleArr(arr):
    s = []
    for i in range(len(arr)):
        s.append( str(handleFloat(arr[i])))
    return s
