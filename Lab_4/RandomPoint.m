function [x, y] = RandomPoint(a, b, N, maxy, miny)
x = a + (b-a)*rand(1,N);
y = miny + (maxy-miny)*rand(1,N);
end

