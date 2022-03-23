import math

def stringhandling(f_input):
    num = ['0','1','2','3','4','5','6','7','8','9']
    f_input = f_input.replace("^","**")
    f_input = f_input.replace(" ","")
    # f_input = f_input.lower()
    for i in range(0, len(f_input)-1):
        for j in range (10):
            if f_input[i] == "x" and f_input[i+1] == num[j]:
                f_input = f_input.replace(f_input[i]+ num[j],"x*" + num[j])
            if f_input[i+1] == "x" and f_input[i] == num[j]:
                f_input = f_input.replace(num[j]+f_input[i+1], num[j]+"*x")
    print(f_input)
    return f_input