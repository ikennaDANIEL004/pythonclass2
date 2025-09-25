# this is a code to check the operation and call the appropriate function



# logicModule.py
import functionModule   

def checkOp(op, num1, num2):
    if op == "add":
       return   functionModule.add(num1, num2)
    elif op == "sub":
        return functionModule.sub(num1, num2)
    elif op == "mult":
        return functionModule.mult(num1, num2)
    elif op == "div":
        return functionModule.div(num1, num2)
    else:
        return "Invalid operation!"
