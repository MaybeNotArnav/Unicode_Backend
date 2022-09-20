

from django.http import HttpResponse


def task2(request, start, end):
    s = start
    n = end
    current = 0
    previous = 0
    dict = {}
    for x in range(s, n):
        bin1 = bin(x)
        for y in range(len(bin1)-1):
            current = bin1[y]
            previous = bin1[y+1]
            if current == "1" and previous == "1":
                dict[x] = True
                break
            else:
                dict[x] = False
    answer = str(dict)
    return HttpResponse(answer)
