import matplotlib.pyplot as plt
# Import necessary libraries
from google.colab import drive
import pandas as pd
import seaborn as sns
# Mount Google Drive
drive.mount('/content/drive')

# Define the file path (update the path if the file is within a folder)
file_path = '/content/drive/My Drive/Copy of Iris.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)
#2 Scatter plot of Petal width and petal length according to species

sns.scatterplot(data=df,x='PetalWidthCm',y='PetalLengthCm',hue='Species')
plt.title('Petal length and width by species')
plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
df.head(10)

#3 Bar plot of average sepal length of each species
mean_sepal_length= df.groupby('Species')['SepalLengthCm'].mean().reset_index()
sns.barplot(data=mean_sepal_length,x='Species',y='SepalLengthCm',palette='pastel')


#4 Box plot SepalWidth by species in the data
sns.boxplot(x='SepalWidthCm',hue='Species',data=df,palette='pastel')

#5 Pie chart showing number of each species in data set
size_species=df.groupby('Species').size().reset_index()
plt.pie(size_species[0],labels=size_species['Species'])
