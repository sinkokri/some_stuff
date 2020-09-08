
import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns

df=pd.read_csv(r'/home/kristina/Study/VS/Students_perfomance_vis/datasets_74977_169835_StudentsPerformance.csv')

#scatterplot
sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='reading score', y='writing score', data=df)
#plt.show()

#regplot=regresion line  (scatter plot with dependency line)
sns.set(rc={'figure.figsize':(12,6)})
sns.regplot(x='reading score', y='writing score', data=df)
#plt.show()

####################################

#dataP=df.pivot("lunch", "writing score")
#Heat map - good for spotting large and small values quickly , sometimes requires data
#to be organized into a matrix using pivots 
#sns.heatmap(dataP, annot=False, fmt="d")
#annot - if we want numbers inside a heatmap 
#fmt = format(decimal)
#after running gives a mistake - needs correct format (matrix)
#creating pivots before the heatmap

#plt.show()

################################3

#Seaborn JointPlot Distribution
#Popular type of graph - good for looking at disctribution and data points at the same time 
#Has option to display different kind of graph - the parametr called kind.

sns.jointplot('reading score', 'writing score', data=df)
#plt.show()

sns.jointplot('reading score', 'writing score', data=df, kind='hex')
#plt.show()

#regression line
sns.jointplot('reading score', 'writing score', data=df, kind='reg')
plt.show()