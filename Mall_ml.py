import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Step 1: Create the dataset

data = {
    'Age': [19, 21, 20, 23, 31, 22, 35, 23, 64, 30],
    'Spending Score': [15, 25, 20, 40, 60, 45, 85, 65, 20, 55]
}

df = pd.DataFrame(data)

#Step 2: Apply Kmeans
Kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df['Cluster'] = Kmeans.fit_predict(df[['Age', 'Spending Score']])

#Step 3: Visualize the cluster
plt.scatter(df['Age'], df['Spending Score'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.show()