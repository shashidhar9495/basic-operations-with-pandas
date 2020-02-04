#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[48]:


data_frames=pd.read_csv('pandas_data/pokemon_data.csv')


# ## reading top3 and tottom 3 files

# In[3]:


data_frames.head(3)
data_frames.tail(3)


# In[4]:


data_frames['Name'][1]


# # # accessing each elements

# In[5]:


data_frames.columns


# In[6]:


data_frames.iloc[0:3,1:5]  ## used for accesing particular location of element


# # # locating all elements by textual information 

# In[7]:


data_frames.loc[data_frames['Type 2']=='Poison'][0:6]


# # # describing all the information about data

# In[8]:


data_frames.describe()


# # # sorting the data according to our need

# In[9]:


data_frames.sort_values(['Name','HP'],ascending=[0,1])[0:4]


# ## performing some operations with columns

# In[10]:


data_frames['Total']=data_frames.iloc[:,4:10].sum(axis=1)
data_frames[0:3]


# In[12]:


colmns=list(data_frames.columns)
data_frames=data_frames[colmns[0:4]+[colmns[-1]]+colmns[4:12]]
data_frames[0:6]


# ## saving into new CSV file or text file

# In[ ]:


new_data.to_csv('pandas_data/new_poki.csv',index=False)
new_data.to_csv('pandas_data/new_poki.txt',index=False,sep='\t')


# ## Filtering

# In[ ]:


filtered_data=data_frames.loc[(data_frames['Type 1']=='Grass')&(data_frames['Type 2']=='Poison')]
filtered_data


# In[ ]:


filering_with_strings=data_frames.loc[data_frames['Name'].str.contains('Pi|Ba')]
filering_with_strings[0:3]


# ## conditional modification

# In[17]:


data_frames.loc[data_frames['Type 1']=='Grass',['Legendary','Type 2']]='a','b'
data_frames.loc[data_frames['Type 1']=='Grass','Type 1']='Grass'
data_frames


# ## grouping the things

# In[38]:


data_frames.groupby(['Type 1']).mean().sort_values('Sp. Atk',ascending=0)
data_frames.groupby(['Type 1']).sum().sort_values('Sp. Atk',ascending=0)
data_frames['count']=1
data_frames.groupby(['Type 1','Type 2']).count()['count'][0:6]


# ## working with large datasets

# In[44]:


for data in pd.read_csv('pandas_data/pokemon_data.csv',chunksize=10):
    print(data)


# In[54]:


new_df=pd.DataFrame(data_frames.columns)
for data in pd.read_csv('pandas_data/pokemon_data.csv',chunksize=10):
    res=data.groupby(['Type 1']).count()
    new_df=pd.concat([new_df,res])
    print(res)


# In[ ]:




