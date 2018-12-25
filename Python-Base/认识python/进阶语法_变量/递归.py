def sum_number(num):
    print(num)

    if num==1:
        return   #递归必须具备出口

    sum_number(num-1)


sum_number(3)
#####################
def sum_numbers(num): #1+2+...+num

    if num==1:
        return 1

    temp=sum_numbers(num-1)

    return temp+num

result=sum_numbers(100)
print(result)