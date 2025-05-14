import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris

# Set seaborn style for better visualization
sns.set_style("whitegrid")

# Task 1: Load and Explore Dataset
def load_and_explore_data():
    try:
        # Load Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\nDataset Info:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        # Since Iris dataset typically has no missing values, we'll verify
        if df.isnull().sum().sum() > 0:
            df = df.fillna(df.mean(numeric_only=True))
            print("Missing values filled with column means")
        
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        return None

# Task 2: Basic Data Analysis
def analyze_data(df):
    try:
        # Basic statistics
        print("\nBasic Statistics:")
        print(df.describe())
        
        # Group by species and compute mean for numerical columns
        print("\nMean values by species:")
        group_means = df.groupby('species').mean()
        print(group_means)
        
        # Insights
        print("\nAnalysis Insights:")
        print("1. Different species show distinct measurements in sepal and petal dimensions.")
        print("2. Virginica tends to have the largest measurements on average.")
        print("3. Setosa typically has the smallest measurements, especially in petal length.")
        
        return group_means
    
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        return None

# Task 3: Data Visualization
def create_visualizations(df):
    try:
        # Create a figure with subplots
        plt.figure(figsize=(15, 10))
        
        # 1. Line Plot (cumulative mean of sepal length by index)
        plt.subplot(2, 2, 1)
        df['sepal length (cm)'].cumsum().div(range(1, len(df) + 1)).plot()
        plt.title('Cumulative Mean of Sepal Length')
        plt.xlabel('Index')
        plt.ylabel('Mean Sepal Length (cm)')
        
        # 2. Bar Plot (mean petal length by species)
        plt.subplot(2, 2, 2)
        sns.barplot(x='species',