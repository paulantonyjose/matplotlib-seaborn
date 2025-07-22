from sklearn.datasets import load_breast_cancer
import pandas as pd
data = load_breast_cancer()
#Load the dataset into a dataframe
df=pd.DataFrame(data.data,columns=data.feature_names)
df['diagnosis']=data.target


#1)Pie chart showing mean radius by diagnosis
mean=df.groupby('diagnosis')['mean radius'].mean()
plt.pie(mean)
plt.pie(x=mean['mean radius'],labels=['Malignant','Benign'],colors=['red','blue'],autopct='%1.1f%%') 
plt.legend()
mean.plot(kind='bar',color=['red','green'])
plt.show()
print(mean)


#2)heatmap showing correlations with various numerical columns
sns.heatmap(df[['mean radius','mean perimeter','mean smoothness','mean concavity','radius error']].corr(),cmap ='viridis')


#3show distribution of mean radius
import numpy as np

df['labelled_diagnosis']=np.where(df['diagnosis'] ==0, 'Malignant', 'Benign')
box=sns.boxplot(data=df,y='mean radius',hue='labelled_diagnosis',palette='Set2')
plt.legend(loc='upper right')


#4. Histogram of the distribution of the mean texture values of malignant and benign diagnosis

# 4. Plot with seaborn.histplot
palette = {'malignant': '#E74C3C', 'benign': '#2ECC71'}
sns.histplot(x='mean texture',hue='labelled_diagnosis',data=df ,bins=20, kde=True,palette=palette ,  multiple='stack',    )
# plt.title('Distribution of Age')
plt.xlabel('mean texture values')
plt.show()
