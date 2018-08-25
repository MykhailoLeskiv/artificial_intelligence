clear, clc
% ���������� ������
testFunc = @(x) x.^2;
mainFunc = @(x) exp(x.^3);
f1 = mainFunc;
% ������� �������������� 
a = -1; b = 1;
disp('����� �������� ����������� ���������: ')
adt = AccurateIntegralValue(f1, a, b);
disp(adt)
disp('����� �������� � �����: ')
disp(AccuratePointValue(f1, 0.5))
% ������� �������
x = linspace(a,b,500);
y1 = f1(x);
 
N = 2000;
[x, y] = RandomPoint(a, b, N, max(y1), 0);
L1 = f1(x)<=y;
n1 = sum( L1 ); % ���-�� ����� ��� ������ ������
L2 = 0<=y; % ���������� ������: ���� ����� ���� ������ ������, �� 1
n2 = sum( L2 ); % ���-�� ����� ��� ������ ������
m = abs(n1-n2); % ���-�� ����� ����� �������
I = m/N*((b-a)*(max(y1)-0)); % �������� ���������
disp('�������� ��������� �� ���������� �����-�����: ')
disp(I)
disp('��������� �������: ')
disp(abs(adt - I))
disp('³������ �������: ')
disp(abs(adt - I)*100 / adt)
 
% ���������� �����
x1 = x(L1); y1 = y(L1);
x2 = x(L2); y2 = y(L2);
plot(x2,y2,'b.');
hold on;
plot(x1,y1,'r.');
 
% ���������� ������� �������
hold on;
%f = inline(f1);
x3 = a:0.01:b;
y3 = f1(x3);
plot(x3,y3)