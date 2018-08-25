function [ av ] = WeightedMovingAverage(arr, period, N)
    n = int32(200 * period + 1);
    depth = 5;
    i = n - depth;
    if i < 1
        i = 1;
    end
    if (n == 1) || (n == N)
        av = arr(i);
    else
        av = arr(i);
        j = 1;
        while i < n + depth
            av = av + j * arr(i);
            i = i + 1;
            j = j + 1;
            if i > n
                break;
            end
        end
        av = 2 * av / ((depth + 2) * (depth + 1));
    end
end

