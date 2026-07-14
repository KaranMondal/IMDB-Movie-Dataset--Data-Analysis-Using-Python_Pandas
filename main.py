import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('IMDB-Movie-Data.csv')
print(data.head(10)) #Check first 10 rows of the dataset
print('******************************************************************')
print(data.tail(10)) #Check last 10 rows of the dataset
print('******************************************************************')
print('Number of rows:',data.shape[0],'\nNumber of Columns: ',data.shape[1]) #Find the shape i.e. number of rows and columns in the dataset
print('******************************************************************')
a= data.info() #Get information about the dataset
print('Information about the dataset: \n',a)
print('******************************************************************')
b = data.isnull() #Check for null values in the dataset
print('Null values in the dataset:\n',b.sum())
sns.heatmap(b, annot=True) 
plt.savefig('1. Heatmap of Null Values in the dataset.png', dpi=300, bbox_inches='tight')
print('******************************************************************')
c= data.dropna() #Drop null values from the dataset
print(c.isnull().sum())
print('******************************************************************')
print('Any duplicates: ',c.duplicated().sum()) #Check for duplicate values in the dataset
print('******************************************************************')
print(c.describe(include='all')) #Get statistical summary of the dataset
print('******************************************************************')
d = data[data['Runtime (Minutes)'] >= 180] #Filter the dataset for movies with runtime greater than or equal to 180 minutes
print('Movies with runtime >= 180 minutes: \n',d['Title']) 
print('******************************************************************')
e = data.groupby('Year')['Votes'].mean().sort_values(ascending=False)
print('Highest votes: \n',e.head(10)) #Get the top 10 movies with the highest number of votes
plt.bar(data['Year'], data['Votes'])
plt.xlabel('Year')
plt.ylabel('Votes')
plt.title('Total Votes as per year')
plt.savefig('2. Total Votes as per year.JPEG', dpi=300, bbox_inches='tight')
print('******************************************************************')
f = data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
print('Highest revenue: \n',f.head(10)) #Get the top 10 movies with the highest revenue
plt.bar(data['Year'], data['Revenue (Millions)'])
plt.xlabel('Year')
plt.ylabel('Revenue (Millions)')
plt.title('Total Revenue as per year')
plt.savefig('3. Total Revenue as per year.JPEG', dpi=300, bbox_inches='tight')
print('******************************************************************')
g = data.groupby('Director')['Rating'].mean().sort_values(ascending=False)
print('Highest rated directors: \n',g.head(10)) #Get the highest rated directors
plt.pie(g.head(10), labels=g.head(10).index, autopct='%1.1f%%')
plt.title('Top 10 Highest Rated Directors')
plt.savefig('4. Top 10 Highest Rated Directors.JPEG', dpi=300, bbox_inches='tight')
print('******************************************************************')
h=data.groupby('Year')['Title'].count().sort_values(ascending=False)
print('Movies released per year: \n',h) #Get the number of movies released
print('******************************************************************')
i=data.groupby('Title')['Revenue (Millions)'].sum().sort_values(ascending=False)
print('TOP MOVIES by revenue in millions: \n',i.head(10)) #Get the top 10 movies with the highest revenue
print('******************************************************************')