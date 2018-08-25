N = 2000;
arr = (N);
x = 0;
for i = 1:N
    arr(i) = 3 * sin (x + 0.5) + ((3/20 + 3/20).*rand(1) - 3/20);
    x = x + 0.005;
end
disp(ArithmeticMean(arr))
disp(GeometricMean(arr))
disp(GarmonicMean(arr))
disp(SimpleMovingAverage(arr, 3, N))
arr2 = (N);
x = 0;
for i = 1:N
    arr2(i) = SimpleMovingAverage(arr, x, N);
    x = x + 0.005;
end
disp(WeightedMovingAverage(arr, 3, N))
disp(ExponentialMovingAverage(arr, 3, N))
disp(ModifiedMovingAverage(arr, 3, N))
plot(arr)
hold on;
plot(arr2)
hold on;
plot(smooth(arr))
legend('Input values','My smoothing', 'Smooth function')
hold off;
Comparison(arr, arr2, N)
Comparison(arr, smooth(arr), N)
disp(AccurateValue(arr, 4, N))
