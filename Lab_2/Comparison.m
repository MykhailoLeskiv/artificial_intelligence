function [] = Comparison ( arr, avarr, N )
    max = 0;
    min = 110;
    Vmax = 0;
    Vmin = 110;
    for i = 1:N
        temp = abs(arr(i) - avarr(i));
        if temp > max
            max = temp;
        end
        if temp < min
            min = temp;
        end
    end
    for i = 1:N
        temp = abs((arr(i) - avarr(i)) / arr(i));
        if temp > Vmax
            Vmax = temp;
        end
        if temp < Vmin
            Vmin = temp;
        end
    end
    disp('Absolute minimum')
    disp(min)
    disp('Absolute maximum')
    disp(max)
    disp('Comparative minimum')
    disp(Vmin)
    disp('Comparative maximum')
    disp(Vmax)
end

