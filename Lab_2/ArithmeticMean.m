function [av] = ArithmeticMean(arr)
    av = 0;
    i = 1;
    while i <= length(arr)
        av = av + arr(i);
        i = i + 1;
    end
    av = av / length(arr);
end