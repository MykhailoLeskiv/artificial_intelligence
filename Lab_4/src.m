clear, clc
% определяем кривые
testFunc = @(x) x.^2;
mainFunc = @(x) exp(x.^3);
f1 = mainFunc;
% пределы интегрирования 
a = -1; b = 1;
disp('Точне значення визначеного інтеграла: ')
adt = AccurateIntegralValue(f1, a, b);
disp(adt)
disp('Точне значення в точці: ')
disp(AccuratePointValue(f1, 0.5))
% діапазон значень
x = linspace(a,b,500);
y1 = f1(x);
 
N = 2000;
[x, y] = RandomPoint(a, b, N, max(y1), 0);
L1 = f1(x)<=y;
n1 = sum( L1 ); % кол-во точек под первой кривой
L2 = 0<=y; % логический вектор: если точка ниже второй кривой, то 1
n2 = sum( L2 ); % кол-во точек под второй кривой
m = abs(n1-n2); % кол-во точек между кривыми
I = m/N*((b-a)*(max(y1)-0)); % значение интеграла
disp('Значення інтеграла за алгоритмом Монте-Карло: ')
disp(I)
disp('Абсолютна похибка: ')
disp(abs(adt - I))
disp('Відносна похибка: ')
disp(abs(adt - I)*100 / adt)
 
% Построение точек
x1 = x(L1); y1 = y(L1);
x2 = x(L2); y2 = y(L2);
plot(x2,y2,'b.');
hold on;
plot(x1,y1,'r.');
 
% Построение графика функции
hold on;
%f = inline(f1);
x3 = a:0.01:b;
y3 = f1(x3);
plot(x3,y3)