# Вычислить число пи, (использовать Ряд Нилаканта или любой другой вариант 
# расчета числа Пи примеры расчетов можно посмотреть
# по ссылке ==> http://www.swsys.ru/files/2018-2/409-413.pdf ) c заданной точностью d

# Program Nilacant;
# var n,i:int64; S1:real; z:integer;
# begin
# write('Введите число слагаемых: ');
# readln(n);
# S1:=3; z:=1; i:=2;
# While i<=n do
# begin
# S1:=S1+4*z/(i*(i+1)*(i+2)); i:=i+2; z:=-z;
# end;
# writeln(s1:12:10);
# ReadLn;
# end.

n = int(input('Введите число слагаемых:'))
S1 = 3
z = 1
i = 2

while i<=n*2:
    S1 = S1 + (4*z)/(i*(i+1)*(i+2))
    i+=2
    z*=-1

print(S1)
