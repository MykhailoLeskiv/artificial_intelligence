function [ av ] = SimpleMovingAverage(arr, period, N)
    n = int32(200 * period + 1);
    depth = 20;
    i = n - depth;
    if i < 1
        i = 1;
    end
    if (n == 1) || (n == N)
        av = arr(i);
    else
        av = 0;
        while i < n + depth
            av = av + arr(i);
            i = i + 1;
            if i > n
                break;
            end
        end
        av = av / (depth + 1);
    end
end

