# Uses python3
import sys

def get_change(m):
    x = m//10
    y = (m-10*x)//5
    z = m-10*x-5*y
    return x+y+z

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
