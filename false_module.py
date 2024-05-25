
def divide(first, second):
    if second == 0:
        return 'Error'
    else:
        res = first / second
        return res
res = divide(5, 0)
if __name__ == "__main__":
    print(res)
