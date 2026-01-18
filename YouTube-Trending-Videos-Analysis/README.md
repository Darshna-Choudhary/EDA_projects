# YouTube Trending Video Analysis (EDA)

### Project Overview
This project performs Exploratory Data Analysis (EDA) on YouTube trending video data to understand how views, likes, comments, and engagement vary across categories.
The goal is to identify content performance patterns and user engagement behavior on YouTube.

### Dataset Information
- Dataset Name: Trending YouTube Video Statistics
- Region: India
- Source: Kaggle
- Format: CSV + JSON (category mapping)

### Data Source Link:
https://www.kaggle.com/datasets/datasnaek/youtube-new

The dataset contains daily trending video statistics including views, likes, dislikes, comments, category IDs, and metadata.

### Key Analyses Performed
- Relationship between views and likes
- Relationship between views and comments
- View distribution and skewness analysis
- Category-wise average likes per view
- Category-wise average comments per view
- Engagement comparison across different content categories
- Log-scale visualizations were used where required to handle extreme skewness.

### Key Insights
- Views and likes show a strong positive correlation
- Comment activity increases with views but varies by content type
- View distribution is highly right-skewed (few viral videos dominate)
- Educational and informational categories show higher engagement per view
- Engagement metrics are more meaningful than raw view counts

### Tools & Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

### Conclusion
This project demonstrates how normalized engagement metrics (likes/comments per view) provide deeper insights than raw popularity. It highlights how different content categories drive different types of audience interaction on YouTube.