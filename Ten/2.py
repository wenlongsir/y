#如何在一个函数内部修改全局变量
a=5
def fn():
    global a
    a=4
fn()
print(a)