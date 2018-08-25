function [] = KMeans(X, k)
figure;
plot(X(:,1),X(:,2),'.');
title 'Randomly Generated Data';
[idx,C] = kmeans(X,k);
disp("Sum of distances: ")
disp(MeasureDistanceCacl(X, idx, k))
figure;
dv = cell(1,k + 1);
for i = 1:k
    dv{i} = strcat('Cluster', num2str(i));
    plot(X(idx==i,1),X(idx==i,2),'Marker','.','LineStyle','none','MarkerSize',12)
    hold on
end
dv{k + 1} = 'Centroid';
plot(C(:,1),C(:,2),'kx',...
     'MarkerSize',15,'LineWidth',3)
legend(dv,'Location','NW')
title 'Cluster Assignments and Centroids'
hold off
end

