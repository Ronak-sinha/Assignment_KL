def calculate(inputCal):
    val=inputCal.split()
    try:
        if val[1]=='+':
            res=float(val[0])+float(val[2]) 
        elif val[1]=='-':
            res=float(val[0])-float(val[2]) 
        elif val[1]=='*':
            res=float(val[0])*float(val[2])
        elif val[1]=='%':
            res=float(val[0])%float(val[2])
        elif val[1]=='/':
            res=float(val[0])/float(val[2])
        return res
    except Exception as e:
        print(e) 

input_string = input("entre the value: ")
result=calculate(input_string)
print(result)