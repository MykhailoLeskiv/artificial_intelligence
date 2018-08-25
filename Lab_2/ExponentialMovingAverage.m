function [ av ] = ExponentialMovingAverage(arr, period, N)
    n = int32(200 * period + 1);
    depth = 5;
    alpha = 2 / (depth + 2);
    i = n - depth;
    if i < 1
        i = 1;
    end
    if (n == 1) || (n == N)
        av = arr(i);
    else
        av = arr(i);
        while i < n + depth
            av = av * (1 - alpha) + alpha * arr(i);
            i = i + 1;
            if i > n
                break;
            end
        end
    end
end

