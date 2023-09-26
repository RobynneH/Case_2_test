#!/usr/bin/env python
# coding: utf-8

# # Case 2 Streamlit

# In[1]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
# import kaggle
import zipfile
import streamlit as st
from PIL import Image


# In[2]:


# !kaggle datasets download -d teejmahal20/airline-passenger-satisfaction


# In[3]:


# zf = zipfile.ZipFile(r"C:\Users\robyn\OneDrive\Documents\HHS\Minor HvA Data Science\Case 2\airline-passenger-satisfaction.zip") 
# train = pd.read_csv(zf.open("train.csv"), index_col = 0)


# In[4]:


train = pd.read_csv("train.csv", index_col = 0)


# In[5]:


st.title("Passenger Satisfaction")


# In[11]:


image = Image.open('dataset-cover.jpeg')
st.image(image)


# In[7]:


train.columns = train.columns.str.replace(' ', '_')


# ## Show information data

# In[8]:


head = train.head()
st.write('First rows of dataframe: ', head)
information = train.describe()
st.write('Information of the dataset: ', information)
describe = train.describe()
st.write('Describe the dataset: ', describe)
nas = train.isna().sum()
st.write('Nonavailable values in the dataset: ', nas)


# In[9]:


crosstabGender = pd.crosstab(train.Gender, train.satisfaction).reset_index()
crosstabClass = pd.crosstab(train.Class, train.satisfaction).reset_index()
crosstabCustomer = pd.crosstab(train.Customer_Type, train.satisfaction).reset_index()
crosstabTravel = pd.crosstab(train.Type_of_Travel, train.satisfaction).reset_index()
crosstabAge = pd.crosstab(train.Age, train.satisfaction).reset_index()


# In[10]:


fig = go.Figure()
crosstablist = [crosstabGender, crosstabClass, crosstabCustomer,crosstabTravel]

for crosstab in crosstablist:
    column_names = list(crosstab.columns.values)
    fig.add_trace(go.Bar(x = crosstab.iloc[:,0],
                         y = crosstab.iloc[:,1],
                         offsetgroup = 0,
                         name = column_names[1],
                         marker_color = "#e377c2"))
    fig.add_trace(go.Bar(x = crosstab.iloc[:,0], 
                         y = crosstab.iloc[:,2], 
                         offsetgroup = 0, 
                         name = column_names[2],
                         base = crosstab.iloc[:,1],
                         marker_color = "#17becf"))

dropdown_buttons = [{'label':'ALL', 'method':'update','args': [{'visible':[True,True,True,True,True,True,True,True]}, 
                                                               {'title':'All'}]},
                    {'label':'Gender', 'method':'update', 'args': [{'visible':[True,True,False,False,False,False,False,False]},
                                                                {'title':'Gender'}]},
                    {'label':'Class','method': 'update','args':[{'visible':[False, False, True, True,False,False,False,False]},
                                                               {'title': 'Class'}]},
                    {'label':'Type of Customer','method': 'update','args':[{'visible':[False, False, False, False,True,True,False,False]},
                                                               {'title': 'Type of Customer'}]},
                    {'label':'Type of Travel','method': 'update','args':[{'visible':[False, False, False, False,False,False,True,True]},
                                                               {'title': 'Type of Travel'}]}]

fig.update_layout({'updatemenus':[{'active': 0 , 'buttons':dropdown_buttons}]})
fig.show()
st.plotly_chart(fig)


# In[ ]:




