function [ av ] = ModifiedMovingAverage(arr, period, N)
    n = int32(200 * period + 1);
    depth = 5;
    i = n - depth;
    if i < 1
        i = 1;
    end
    if (n == 1) || (n == (N / 10))
        av = arr(i);
    else
        av = arr(i);
        while i < n + depth
            av = (av * depth + arr(i)) / (depth + 1);
            i = i + 1;
            if i > n
                break;
            end
        end
    end
end

