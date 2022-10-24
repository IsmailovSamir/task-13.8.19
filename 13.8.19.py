ticket = int(input('Сколько билетов вам нужно '))
age = [int(input('Сколько вам лет ')) for i in range(ticket)]
c=0
for i in range(len(age)):
    if age [i]<=18-1:
        c=0
    elif 18-1<= age [i] <= 25:
        c=c+990
    else:
        c=c+1390
print("Общая сумма",c)
if (ticket>=3):
    diskont = c * 0.10
    c = c - diskont
print("Общая сумма со скидкой",c)
