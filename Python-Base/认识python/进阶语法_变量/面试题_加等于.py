def demo(num, num_list):
    print("函数开始")

    num_list+=num_list #+=表示列表extend 不会改变列表引用
    num+=num


    print(num)
    print(num_list)
    print("函数完成")

gl_num=9
gl_list=[1,2,3]

demo(gl_num,gl_list)
print(gl_num,gl_list)