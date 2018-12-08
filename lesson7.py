"""
[1,2,3] - iterable
i = iter([1,2,3])
i - iterator
"""
it = iter([1,2,3])
next(it)
#1
next(it)
#2
next(it)
#3
next(it)
"""
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    next(it)
StopIteration
"""
import dis
dis.dis("[i for i in range(10)]")
"""
 1           0 LOAD_CONST               0 (<code object <listcomp> at 0x010D7860, file "<dis>", line 1>)
              2 LOAD_CONST               1 ('<listcomp>')
              4 MAKE_FUNCTION            0
              6 LOAD_NAME                0 (range)
              8 LOAD_CONST               2 (10)
             10 CALL_FUNCTION            1
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 RETURN_VALUE
"""

#yield - продолжает работать, в отличие от return

def g():
	c = 0
	while True:
		yield c
		c += 1

		
gen = g()
next(gen)
#0
next(gen)
#1


def g():
	c = 0
	while True:
		res = yield c
		c += 1
		if res is not None:
			c = res

			
gen = g()
gen.send(4)
"""
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    gen.send(4)
TypeError: can't send non-None value to a just-started generator
"""
next(gen)
#0
gen.send('boo')
#'boo'
next(gen)
"""
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    next(gen)
  File "<pyshell#27>", line 5, in g
    c += 1
TypeError: can only concatenate str (not "int") to str
"""
gen = g()
next(gen)
#0
gen.send(5)
#5
next(gen)
#6
