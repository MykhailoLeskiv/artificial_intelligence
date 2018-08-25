function [ val ] = AccurateValue(arr, point, N)
    val = 3 * sin (point + 0.5);
    disp('Accurate value: ')
    disp(val)
    disp(arr(point * 200))
    val = val - arr(point * 200);
end
