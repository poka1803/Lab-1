WHITE= '\u001b[47m'
BLUE= '\u001b[44m'
BLACK='\u001b[40m'
END='\u001b[0m'
GREEN='\u001b[42m'
RED='\u001b[41m'

for i in range(6):
    if i<2:
        print(f'{WHITE}{" " * 5}{BLUE}{" " * 5}{WHITE}{" " * 10}{END}')
    elif i<4:
        print(f'{BLUE}{" " *20}{END}')
    else:
        print(f'{WHITE}{" " * 5}{BLUE}{" " * 5}{WHITE}{" " * 10}{END}')
print()  

for i in range (3):
    print(
        "\x1b[47;1m  " * 5,
        "\x1b[40;1m  " * 1,
        "\x1b[47;1m  " * 10,
        "\x1b[40;1m  " * 1,
        "\x1b[47;1m  " * 5,
        "\x1b[m",)
    print(
        "\x1b[47;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 8,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m  " * 2,
        "\x1b[m",)
    print(
        "\x1b[47;1m  ",
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m  ",
        "\x1b[m",)
    print(
        "\x1b[47;1m ",
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 5,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 5,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m ",
        "\x1b[m",)
    print(
        "\x1b[47;1m",
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 6,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m     ",
        "\x1b[40;1m  " * 6,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m",
        "\x1b[m",)
    print(
        "\x1b[47;1m ",
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 5,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 5,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m ",
        "\x1b[m",)
    print(
        "\x1b[47;1m  ",
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 4,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m  ",
        "\x1b[m",)
    print(
        "\x1b[47;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m " * 8,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[40;1m  " * 2,
        "\x1b[47;1m  " * 2,
        "\x1b[m",)
    print(
        "\x1b[47;1m  " * 4,
        "\x1b[40;1m  " * 3,
        "\x1b[47;1m  " * 8,
        "\x1b[40;1m  " * 3,
        "\x1b[47;1m  " * 4,
        "\x1b[m",)
print()

print('y')
for x in range(10,-2,-1):
    if 0 < x <= 10:
        print(f'{x/2}{" "}{ " " *2*(x-1)}{BLUE}{"  "}{END}{ " " * 2*(18-x)}' )
    elif x == 0:
        print(f'{"    "  + "  " * 20}{END}')
    else:
        print(f'{"     "}{"1 2 3 4 5 6 7 8 9 10  x "}')
print()

file = open('sequence.txt', 'r')
list1 = []
list2 = []
all=0
for number in file:
    if ( 5<= float(number) <= 10) :
        all+=1
        list1.append(float(number))
    if (-10 <= float(number) <= -5):
        all+=1
        list2.append(float(number))
file.close()
plus= 100*(len(list1)/ all)
minus=100*(len(list2)/all)
print(f'{GREEN}{" "}{END}{"(Числа от 5 до 10 ) "}{len(list1)}{" шт процентное соотношение:"}{plus}{"%"}{END}')
print(f'{RED}{" "}{END}{"(Числа от -10 до -5) "}{all-len(list1)}{" шт процентное соотношение:"}{minus}{"%"}{END}')
print(f'{RED}{" " * int(minus)}{GREEN}{" " * int(plus)}{END}')
print(f'{(minus)}{"%"}{" " * 30 }{plus}{"%"}')