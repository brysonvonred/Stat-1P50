# In[8]:

!pip install pandas
import pandas as pd

#Key value remains the same, but the column form a list for the value terms
myDict = {}
myDict['a'] = "1", "2", "2", "1"#double quotation
myDict['b'] = '3.1', '4.2', '1.5', '6.3'#single quotation? So they mean the same thing..
myDict['c'] = '800', '150', '400', '210'
#here's the proof
print(myDict)

#set df as panda.dataframe function to create the data frame and fill with the myDict
df = pd.DataFrame(myDict)
print(df)
