def demo(num, *args, **person):

    print(num)
    print(args)
    print(person)

demo(1,2,3,4,5,name="小明",age=18)

######################
def sum_numbers(*args):

    num=0

    print(args)

    for n in args:
        num+=n
    return num

result=sum_numbers(1,2,3,4,5)

print(result)
#####################
