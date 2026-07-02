# 🛍️ Customer Segmentation Using K-Means Clustering

## 📌 Project Overview

Understanding customer behavior is one of the most important aspects of modern retail businesses. In this project, I used the **K-Means Clustering Algorithm** to segment customers based on their **Annual Income** and **Spending Score**.

The objective was to identify different groups of customers with similar purchasing patterns, enabling businesses to make smarter marketing decisions and improve customer engagement.

---

## 🎯 Objectives

* Analyze customer purchasing behavior.
* Apply K-Means Clustering for customer segmentation.
* Determine the optimal number of clusters using the Elbow Method.
* Visualize customer groups for better business insights.
* Interpret the characteristics of each customer segment.

---

## 📊 Dataset Information

The project uses the **Mall Customer Dataset**, which contains:

| Feature                | Description                                  |
| ---------------------- | -------------------------------------------- |
| CustomerID             | Unique customer identifier                   |
| Gender                 | Customer gender                              |
| Age                    | Customer age                                 |
| Annual Income (k$)     | Annual income of the customer                |
| Spending Score (1–100) | Spending behavior score assigned by the mall |

For clustering, the following features were selected:

* Annual Income (k$)
* Spending Score (1–100)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 🚀 Project Workflow

### 1. Data Collection

Loaded the Mall Customer Dataset and inspected the available features.

### 2. Data Preprocessing

Selected relevant attributes and prepared the data for clustering.

### 3. Feature Scaling

Standardized the dataset using StandardScaler to improve clustering performance.

### 4. Finding Optimal Clusters

Used the Elbow Method to determine the most suitable number of clusters.

### 5. Model Training

Applied the K-Means algorithm to segment customers into distinct groups.

### 6. Data Visualization

Created scatter plots and centroid visualizations to understand customer distributions.

### 7. Cluster Analysis

Analyzed the characteristics of each segment and their business significance.

---

## 📈 Results

The model successfully identified different customer categories such as:

💎 High Income – High Spending Customers

🎯 High Income – Low Spending Customers

🛒 Low Income – High Spending Customers

💰 Low Income – Low Spending Customers

📊 Average Customers

These insights can help businesses design personalized marketing campaigns and improve customer retention strategies.

---

## 📷 Sample Output

* Elbow Method Graph
* Customer Segmentation Scatter Plot
* Cluster Centroid Visualization

---

## 📚 Key Learnings

Throughout this project, I gained practical experience in:

✅ Unsupervised Machine Learning

✅ K-Means Clustering

✅ Data Preprocessing

✅ Feature Scaling

✅ Data Visualization

✅ Customer Segmentation Techniques

✅ Business-Oriented Data Analysis

---

## 💡 Business Impact

Customer segmentation helps organizations:

* Improve targeted marketing campaigns
* Increase customer satisfaction
* Enhance customer retention
* Identify high-value customers
* Optimize promotional strategies

---

## 🔮 Future Improvements

* Implement 3D Customer Segmentation using Age, Income, and Spending Score.
* Compare K-Means with Hierarchical Clustering.
* Build an interactive dashboard using Power BI or Tableau.
* Deploy the model as a web application.

---

## 🏆 Conclusion

This project demonstrates how machine learning can transform raw customer data into meaningful business insights. By leveraging K-Means Clustering, retailers can better understand customer behavior and make data-driven decisions that contribute to business growth and customer satisfaction.

⭐ If you found this project helpful, feel free to star the repository and connect with me on LinkedIn.
