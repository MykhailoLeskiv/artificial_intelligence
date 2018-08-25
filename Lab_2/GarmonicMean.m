function [av] = GarmonicMean(arr)
    av = 0;
    i = 1;
    while i <= length(arr)
        av = av + (1 / arr(i));
        i = i + 1;
    end
    av = length(arr) / av;
end