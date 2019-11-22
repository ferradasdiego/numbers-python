from pymep.realParser import parse
from pymep.realParser import eval
from pymep.exception import CalculatorException


#Real Expresion parser
fx="cos(10)"
print(parse(fx))

p=5
fx = "1 + x"
print(eval(fx, xi))

var = {"x":"1+1", "Z":1}
eval(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var)
