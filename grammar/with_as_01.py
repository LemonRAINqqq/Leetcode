class Sample:
    def __enter__(self):
        print ("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print ("In __exit__()")


def get_sample():
    return Sample()


with get_sample() as sample:
    print ("sample:", sample)

'''输出：
In __enter__()
sample: Foo
In __exit__()
'''
#有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的with语句提供了一种非常方便的处理方式。
#with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
#紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
#当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
