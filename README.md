# 🎬 IMDb Movie Dataset - Data Analysis Using Python & Pandas

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the IMDb Movie Dataset using Python. The goal is to explore, clean, analyze, and visualize movie data to extract meaningful insights related to ratings, revenue, votes, runtime, directors, and movie releases over the years.

The analysis is performed using **Pandas** for data manipulation and **Matplotlib & Seaborn** for data visualization.

---

## 📂 Dataset

The dataset used in this project is:

`IMDB-Movie-Data.csv`

It contains information about **1,000 movies**, including:

- Rank
- Title
- Genre
- Description
- Director
- Actors
- Year
- Runtime (Minutes)
- Rating
- Votes
- Revenue (Millions)
- Metascore

---

## 🛠️ Technologies & Libraries Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📊 Analysis Performed

The following analysis was performed on the IMDb Movie Dataset:

### 1. Dataset Exploration
- Displayed the first 10 rows of the dataset
- Displayed the last 10 rows of the dataset
- Checked the number of rows and columns
- Examined dataset information and data types
- Generated a statistical summary of the dataset

### 2. Data Cleaning
- Checked for missing/null values
- Visualized missing values using a heatmap
- Removed rows containing null values
- Checked for duplicate records

### 3. Movie Runtime Analysis
- Identified movies with a runtime greater than or equal to **180 minutes**

### 4. Votes Analysis
- Calculated the average number of votes by year
- Identified the years with the highest average votes
- Visualized votes according to year

### 5. Revenue Analysis
- Calculated the average movie revenue by year
- Identified the years with the highest average revenue
- Visualized movie revenue according to year
- Identified the top 10 highest-grossing movies

### 6. Director Analysis
- Calculated the average movie rating for each director
- Identified the top 10 highest-rated directors
- Visualized the top-rated directors

### 7. Movie Release Analysis
- Calculated the number of movies released each year
- Identified the years with the highest number of movie releases

---

## 📈 Key Performance Indicators (KPIs)

| KPI | Value |
|---|---:|
| Total Movies | 1,000 |
| Total Directors | 644 |
| Average IMDb Rating | 6.72 / 10 |
| Highest IMDb Rating | 9.0 / 10 |
| Average Movie Runtime | 113.17 Minutes |
| Longest Movie Runtime | 191 Minutes |
| Movies with Runtime ≥ 180 Minutes | 7 |
| Total Votes | ~169.81 Million |
| Average Votes per Movie | ~169.81 Thousand |
| Total Revenue | ~$72.30 Billion |
| Average Movie Revenue | ~$82.96 Million |
| Highest-Grossing Movie | Star Wars: Episode VII - The Force Awakens |
| Highest Movie Revenue | $936.63 Million |
| Year with Highest Average Revenue | 2009 |
| Highest-Rated Director | Nitesh Tiwari |
| Highest Director Average Rating | 8.8 |
| Year with Most Movie Releases | 2016 |
| Movies Released in 2016 | 297 |
| Duplicate Records | 0 |

---

## 📊 Data Visualizations

### 🔹 Heatmap of Null Values

![Heatmap of Null Values](1.%20Heatmap%20of%20Null%20Values%20in%20the%20dataset.png)

This heatmap helps identify missing values present in different columns of the dataset.

---

### 🔹 Total Votes as per Year

![Total Votes as per Year](2.%20Total%20Votes%20as%20per%20year.JPEG)

This visualization shows the distribution of movie votes across different years.

---

### 🔹 Total Revenue as per Year

![Total Revenue as per Year](3.%20Total%20Revenue%20as%20per%20year.JPEG)

This visualization represents movie revenue across different years.

---

### 🔹 Top 10 Highest Rated Directors

![Top 10 Highest Rated Directors](4.%20Top%2010%20Highest%20Rated%20Directors.JPEG)

This visualization highlights the top 10 directors based on their average movie ratings.

---

## 📁 Project Structure

```text
IMDB-Movie-Dataset--Data-Analysis-Using-Python_Pandas/
│
├── 1. Heatmap of Null Values in the dataset.png
├── 2. Total Votes as per year.JPEG
├── 3. Total Revenue as per year.JPEG
├── 4. Top 10 Highest Rated Directors.JPEG
├── IMDB-Movie-Data.csv
├── KPI's.txt
├── main.py
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/KaranMondal/IMDB-Movie-Dataset--Data-Analysis-Using-Python_Pandas.git
```

### 2. Navigate to the Project Folder

```bash
cd IMDB-Movie-Dataset--Data-Analysis-Using-Python_Pandas
```

### 3. Install the Required Libraries

```bash
pip install pandas matplotlib seaborn
```

### 4. Run the Python Script

```bash
python main.py
```

---

## 💡 Key Insights

- The dataset contains **1,000 movies** released across different years.
- The average IMDb rating of movies in the dataset is approximately **6.72**.
- The highest IMDb rating in the dataset is **9.0**.
- The average movie runtime is approximately **113 minutes**.
- The longest movie has a runtime of **191 minutes**.
- **2016** recorded the highest number of movie releases in the dataset.
- Movie revenue and audience votes vary significantly across different years.
- Some columns contain missing values, particularly revenue and Metascore.
- The dataset contains **no duplicate records** after cleaning.

---

## 🎯 Project Objective

The objective of this project is to demonstrate practical skills in:

- Data Loading
- Data Exploration
- Data Cleaning
- Handling Missing Values
- Data Filtering
- GroupBy Operations
- Aggregation
- Exploratory Data Analysis (EDA)
- Data Visualization
- Extracting Business Insights

---

## 👨‍💻 Author

**Karan Mondal**

GitHub: [KaranMondal](https://github.com/KaranMondal)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
