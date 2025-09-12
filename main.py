def summa(*args):
    if len(args) != 2:
        return None
    num = args[0]
    target = args[1]
    if type(target) != int:
        return None
    if type(num) != list:
        return None
    if len(num) == 1 or len(num) == 0:
        return None
    if all(isinstance(x,float)for x in num):
        return None
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
    return None
