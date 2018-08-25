function value = AccuratePointValue(f, point)
syms x
value = double(subs(int(f, x), point));
end

