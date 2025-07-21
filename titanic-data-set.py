import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# Use 'x' for the main category ('class') and 'hue' for the stacking variable ('survived')
sns.histplot(titanic, x='class', hue='survived', multiple='stack', shrink=0.8, palette='Set1')
plt.title('Titanic: Survival by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Passenger Count')
plt.legend(['Did Not Survive', 'Survived'], loc='upper left')
plt.show()
# 2. Pie Chart of Passengers by Gender
count_by_gender = titanic.groupby('sex').size()
labels=['Man','Woman']
colors = ['skyblue','lightgreen']
plt.figure(figsize=(8,8))
plt.pie(count_by_gender,labels=labels,colors=colors,autopct='%1.1f%%') 
plt.title('Titanic data by gender count')
count_by_gender
sns.piechart
titanic.columns
# 3. Histogram of Passenger Ages
sns.histplot(titanic, x='age', multiple='stack', shrink=0.8,color='green', palette='Set2',bins=10)


# 4. Scatter Plot of Passenger Age and Fare Paid
scatter =sns.scatterplot(titanic,x='age',y='fare',hue='survived')

# 5. Bar Chart of Survivors by Age Range
plot=sns.histplot(titanic, x='age', hue='survived', multiple='stack', shrink=0.8, palette='Set1',hue_order=[1,0])
handles,_=plot.get_legend_handles_labels()
plt.legend(labels=['Survived','Did Not Survive'], loc='upper left')
