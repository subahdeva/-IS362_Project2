#!/usr/bin/env python
# coding: utf-8

# In[338]:


import numpy as np
import pandas as pd
import re

# FBI Data of Offenses in California by County
# 1) Which counties have the highest number of violent crimes?
# 2) Which counties have the lowest number of violent crimes?
# 3) Which counties have the highest number of murder and nonnegligent manslaughter (manm)?


#Load CSV file and read all rows
df = pd.read_csv("ca_offenses_by_county_untidy.csv", index_col = False,)

#Clean up county names by removing any digits within each word
df['county'] = df['county'].str.replace('\d+', '')

#Create a custom clean header with Proper wording for each column to clearly distinguish each column of data
csv_header = ['County Type', 'County', 'Violent Crimes', 'Rape', 'Robbery', 'Murder and Non-Negligent Manslaughter', 
              'Aggravated Assault', 'Property crime', 'Burglaries', 'Larceny-theft', 'Motor Vehicle Theft', 'Arson'] 

#Write to new csv with the clean-up
df.to_csv('ca_offenses_by_county_tidy.csv', header=csv_header, index=False, mode= 'w')

#Reload CSV file and to read new csv
df = pd.read_csv('ca_offenses_by_county_tidy.csv',na_filter= False, skipinitialspace=True)

#uncomment out to check what columns are objects or integers
#df.info()

#display sorted csv
df.head(60)


# In[339]:


# 1) Los Angeles, Sacramento, Kern, and San Diego are some of the top counties in California 
# with the highest numbers in violent crime
df[['County', 'Violent Crimes']].sort_values('Violent Crimes', ascending=False).head(10)


# In[342]:


# 2) Sierra, Alpine, and Mono are the top 3 counties in California with the lowest number of violent crimes

df[['County', 'Violent Crimes']].sort_values('Violent Crimes', ascending=True).head(10)



# In[344]:


# 3) Los Angeles, Sacramento, and Kern are the top 3 counties in California with the highest number of murder and nonnegligent manslaughter 
df[['County', 'Murder and Non-Negligent Manslaughter']].sort_values('Murder and Non-Negligent Manslaughter', ascending=False).head(10)


# In[ ]:





# In[ ]:




