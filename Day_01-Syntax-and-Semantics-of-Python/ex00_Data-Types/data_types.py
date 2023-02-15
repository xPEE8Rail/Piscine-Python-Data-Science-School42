def data_types():
    a = 1
    b = "Hello World!"
    c = 3.14
    d = False
    e = [1, "12"]
    f = {"Spain": "Real"}
    g = ("AkBars", "Rubin")
    h = {1, 6, 3, 4}
    lst = [a, b, c, d, e, f, g, h]
    str1 = "["
    for i in range(len(lst)):
        lst[i] = type(lst[i]).__name__
    str1 += ", ".join(lst) + "]"
    print(str1)


if __name__ == '__main__':
    data_types()
