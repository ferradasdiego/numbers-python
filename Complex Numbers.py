from pymep.complexParser import parse
from pymep.complexParser import eval
from pymep.complex import Complex
from pymep.exception import CalculatorException

#Operation with complex numbers
a = Complex(1,2)
print(a.__radd__(10).__complex__())
print(Complex.radd(10, a).__complex__())


#Complex Expresion parser
fx="cos(10+2j)"
print(parse(fx).__complex__())

xi=5
fx = "1 +j+x"
print(eval(fx, xi).__complex__())

var={"x":"1+2j", "Y":complex(2,1)}
f_x = "x-y"
eval(f_x,var).__complex__()