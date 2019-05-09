
import math

def number1():
    a = 123
    b = 3.1415926
    print("int(b)=",int(b))
    print("float(a)=",float(a))
    print("complex(a)=",complex(a))
    print("complex(a,b)=",complex(a,b))


def numberFun():
    #求绝对值:abs(x)
    print("abs(-12)=",abs(-12))
    #向上取整:ceil(x)
    print("ceil(3.1415)=",math.ceil(3.1415))
    #向下取整:floor(x)
    print("floor(3.678)=",math.floor(3.678))
    #四舍五入:round(x)
    print("round(3.678)=",round(3.678))
    #乘方运算:pow(x,y),x的y次方
    print("pow(3,4)=",pow(3,4))
    #求平方根:sqrt(x)
    print("sqrt(144)=",math.sqrt(144))

def oprationList():
    testList = ['1','2','4']
    testList.append("3")

    print(testList)
    print(testList[1])

if __name__ == '__main__':
    numberFun()
    oprationList()