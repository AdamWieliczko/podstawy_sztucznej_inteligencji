def function(list):
    sum = list[0] or 0
    div = list[0] or 0
    mult = list[0] or 0

    for i in list:
        sum += i
        div -= i
        mult *= i

    return sum, div, mult


print(function([5, 3, 3, 2]))