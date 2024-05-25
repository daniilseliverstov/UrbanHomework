import math
def divide(first, second):
    if second == 0:
       return math.inf
    else:
        res = first / second
        return res


res = divide(1,0)
if __name__ == "__main__":
    print(res)