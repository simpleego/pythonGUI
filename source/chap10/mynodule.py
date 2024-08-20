import fibo 


print(fibo.fib(1000))
print(fibo.fib2(100))

print(fibo.__name__)

from fibo import fib
print(fib(1000))

from fibo import fib, fib2
print(fib(500))

from fibo import *
print(fib(500))


