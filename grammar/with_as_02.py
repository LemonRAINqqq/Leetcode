class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print ("type:", type)
        print ("value:", value)
        print ("trace:", trace)

    def do_something(self):
        bar = 1
        print( bar + 10)
with Sample() as sample:
    sample.do_something()
    
'''
output:
11
type: None
value: None
trace: None
'''
#修改
    def do_something(self):
        bar = 1/0
        print( bar + 10)
''' 
output：
type: <class 'ZeroDivisionError'>
value: division by zero
trace: <traceback object at 0x0000020E6BD77588>
Traceback (most recent call last): 
ZeroDivisionError: division by zero
'''

#在with后面的代码块抛出任何异常时，__exit__()方法被执行。
#正如例子所示，异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来了
