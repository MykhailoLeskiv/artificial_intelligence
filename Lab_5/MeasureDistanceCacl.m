function [ro] = MeasureDistanceCacl(X, c, k)
arr = zeros(k, 2);
for i = 1:length(X)
    arr(c(i), 1) = arr(c(i), 1) + X(i,1);
    arr(c(i), 2) = arr(c(i), 2) + X(i,2);
end
lteh = zeros(1,k);
for i = 1:length(c)
    lteh(c(i)) = lteh(c(i)) + 1;
end
for i = 1:k
    arr(i, 1) = arr(i, 1) / lteh(i);
    arr(i, 2) = arr(i, 2) / lteh(i);
end
hut = zeros(1,k);
for i = 1:length(X)
    hut(c(i)) = hut(c(i)) + sqrt((X(i,1) - arr(c(i), 1)).^2 + (X(i,2) - arr(c(i), 2)).^2);
end
ro = 0;
for i = 1:k
    ro = ro + hut(i);
end