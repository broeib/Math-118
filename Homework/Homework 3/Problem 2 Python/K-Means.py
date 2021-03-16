from pandas import DataFrame
from sklearn.cluster import KMeans

Data = {'x': [-0.82, -1.33, -3.63, -1.62, -2.95, 0.95, 0.53, 1.79, 0.95, 2.28]}
df = DataFrame(Data, columns=['x'])
kmeans = KMeans(n_clusters=2).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)