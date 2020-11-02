
def add():
    print("这是加法函数")


def shot(func):
    def wraper(*args,**kwargs):
        print("这是装饰器！！")
        func(*args,**kwargs)
        print("这也是装饰器")
    return  wraper

@shot
def add():
    print("这是jian法函数")


if __name__ == '__main__':

    add()