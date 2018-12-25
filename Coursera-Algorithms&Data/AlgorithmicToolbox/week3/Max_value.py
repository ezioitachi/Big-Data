# Uses python3
import sys, operator

def get_optimal_value(capacity, weights, values):
    n = len(values)
    unit = {}
    for i in range(n):
    	unit[i] = values[i]/weights[i]
    unit = sorted(unit.items(),key=operator.itemgetter(1))
    value = 0
    while capacity > 0 and unit != []:
    	Max = unit.pop()
    	w = min(weights[Max[0]],capacity)
    	capacity -= w
    	value += Max[1]*w
    	

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
