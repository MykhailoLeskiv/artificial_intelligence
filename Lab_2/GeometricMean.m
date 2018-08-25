function [av] = GeometricMean(arr)
    av = 0;
    i = 1;
    while i <= length(arr)
        av = av * arr(i);
        i = i + 1;
    end
    av = av ^ (1 / length(arr));
end