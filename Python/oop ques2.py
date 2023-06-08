class calulator:
    def __init__(self,operand1,operand2):
        self.operand1 = float(operand1)
        self.operand2 = float(operand2)
    def add(self):
        return self.operand1+self.operand2
    def sub(self):
        return self.operand1-self.operand2
    def mul(self):
        return self.operand1*self.operand2
    def div(self):
        return self.operand1/self.operand2
    def mod(self):
        return self.operand1%self.operand2

input_string = input("entre the value: ")
val=input_string.split()
obj1=calulator(val[0],val[2])
try:
    if val[1]=='+':
        res=obj1.add() 
    elif val[1]=='-':
        res=obj1.sub() 
    elif val[1]=='*':
        res=obj1.mul()
    elif val[1]=='%':
        res=obj1.mod()
    elif val[1]=='/':
        res=obj1.div()
    print(res)
except Exception as e:
    print(e)