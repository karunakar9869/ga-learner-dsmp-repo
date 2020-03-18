# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here


#Code ends here
data=pd.read_csv(path)

#Plotting histogram of Rating
data['Rating'].plot(kind='hist')

plt.show()


#Subsetting the dataframe based on `Rating` column
data=data[data['Rating']<=5]

#Plotting histogram of Rating
data['Rating'].plot(kind='hist')   





# --------------
# code starts here


# code ends here

total_null=data.isnull().sum()
total_null

k=[]
for i in range (0,len(total_null)):
    s=(total_null[i]/len(data))*100
    k.append(s)
k   
percent_null=pd.Series(k,total_null.index)
percent_null
missing_data=pd.DataFrame({'Total':total_null,'Percent':percent_null})
missing_data
data=data.dropna()
total_null_1=data.isnull().sum()
total_null_1
r=[]
for i in range (0,len(total_null_1)):
    t=(total_null_1[i]/len(data))*100
    r.append(t)
r  
percent_null_1=pd.Series(r,total_null_1.index)
percent_null_1
missing_data_1=pd.DataFrame({'Total':total_null_1,'Percent':percent_null_1})
missing_data_1
































# --------------

#Code starts here



#Code ends here
g=sns.catplot(x="Category",y="Rating",data=data, kind="box", height=10)
g.set_xticklabels(rotation=90)
g.set_titles('Rating vs Category [BoxPlot]')



# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here




#Code ends here
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here










# --------------
#Code starts here



#Code ends here
data['Price'].value_counts()
data['Price']=data['Price'].str.replace('$','').astype(float)
sns.regplot(x='Price',y='Rating',data=data)
plt.figure(figsize=(10,10))
plt.title('Rating vs Price [RegPlot]',size=20)











# --------------

#Code starts here




#Code ends here
print( len(data['Genres'].unique()) , "genres")

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))







# --------------

#Code starts here




#Code ends here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

#Creating new column having `Last Updated` in days
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 

#Setting the size of the figure
plt.figure(figsize = (10,10))

#Plotting a regression plot between `Rating` and `Last Updated Days`
sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)

#Code ends here


