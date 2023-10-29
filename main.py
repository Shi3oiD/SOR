history_plus = []
history_sub = []
history_div = []
history_mult = []

while True:
    x = float(input())
    y = float(input())
    z = str(input())
    res = "error"
    if z == "+":
        res = x + y
        history_plus.append(str(x) + str(z) + str(y) + " = " + str(res))
    if z == "*":
        res = x * y
        history_mult.append(str(x) + str(z) + str(y) + " = " + str(res))
    if z == "-":
        res = x - y
        history_sub.append(str(x) + str(z) + str(y) + " = " + str(res))
    if z == "/":
        if y != 0:
            res = x / y
            history_div.append(str(x) + str(z) + str(y) + " = " + str(res))
    print(res)
    print("+" + str(history_plus))
    print("-" + str(history_sub))
    print("*" + str(history_mult))
    print("/" + str(history_div))


