# Mall Customer Clustering 

This is a beginner-friendly unsupervised machine learning project using **KMeans Clustering** to group mall customers based on their **age** and **spending habits**.

The goal is to identify natural customer segments, such as low-spending young adults or high-spending middle-aged shoppers — without any labeled data.

---

## What It Does

- Uses a mini dataset of 10 customers
- Applies **KMeans** to group them into 3 clusters
- Visualizes the customer segments with color-coded scatter plots
- Demonstrates the concept of **unsupervised learning** in a simple, visual way

---

## Key Concepts

- **Unsupervised Learning**: Clustering with no known labels
- **KMeans Algorithm**: Groups data by similarity based on distance to centroids
- **`fit_predict()`**: Learns the groupings and assigns cluster labels
- **Visualization**: Matplotlib shows customer segments clearly

---

## How to Run

1. Clone this repo  
2. (Optional) Create and activate a virtual environment  
3. Install required packages:
   ```bash
   pip install pandas matplotlib scikit-learn
