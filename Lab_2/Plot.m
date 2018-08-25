function [ ] = Plot(arr, N)
    aer = [];
    x = 0;
    for i = 1:N
        aer(end + 1) = x;
        x = x + 0.005;
    end
    plot(aer,arr)
end

