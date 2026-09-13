import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

#load csv file
df=pd.read_csv(r"C:\Users\ADMIN\Desktop\python-projects\DataAnalysisProject\Diwali Sales Data.csv",encoding='unicode_escape')
#return no of rows and columns
print(df.shape)
#return 1st 5 rows
print(df.head())
#for  all information
print(df.info)
#drop blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)
#check null values
pd.isnull(df).sum()
#drop null values
df.dropna(inplace=True)
#change datatype of amount column float to int
df['Amount']=df['Amount'].astype('int')
#show all columns
print(df.columns)
#rename column
df.rename(columns={'Marital_Status':'Married'},inplace=True)
#describe() method returns description of data in dataframe
print(df[['Age','Orders','Amount']].describe())

#exploratory data analysis
 
plt.figure(1)
ax=sns.countplot(x='Gender',data=df,hue='Gender',palette=['pink','blue'])
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("Gender Count")
plt.savefig('gender_count.png')


plt.figure(2)
sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen,hue='Gender',palette=['pink','blue'])
plt.title("total amount of purchase based on Gender")
plt.savefig('purchase_based_on_gender.png')


plt.figure(3)

ax=sns.countplot(data=df,x='Age Group',hue='Gender',palette=['pink','blue'])
for bars in ax.containers:
    ax.bar_label(bars)
plt.title("sales based on Age Group")
plt.savefig('sales_based_on_age_group.png')


plt.figure(4)
sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_age,hue='Age Group',palette='Set3')
plt.title("Total_Amount_VS Age Group")
plt.savefig('total_amount_vs_age_group.png')


plt.figure(5)
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
plt.figure(figsize=(13,5))
sns.barplot(x='State',y='Orders',data=sales_state,hue='State',palette='Set3')
plt.title("Total no of orders from top 10 state")
plt.savefig('top_10_state.png')


#total amount/sales from top 10 state
plt.figure(6)
sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
plt.figure(figsize=(13,5))
sns.barplot(x='State',y='Amount',data=sales_state,hue='State',palette='Set3')
plt.title("total amount of salesof top 10 state")
plt.savefig('top_10_state_amount.png')






