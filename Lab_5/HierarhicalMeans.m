function [] = HierarhicalMeans(X, k)
figure;
Z = linkage(X,'ward','euclidean','savememory','on');
c = cluster(Z,'maxclust',k);
disp("Sum of distances: ")
disp(MeasureDistanceCacl(X, c, k))
scatter(X(:,1),X(:,2),12,c, 'filled')
end

