#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests


# In[33]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[34]:


req
type(req)
dir(req)


# In[35]:


page = req.text
page


# In[38]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')


# In[39]:


type(page)
type(soup)


# In[40]:


print(soup.prettify())


# In[41]:


soup.p


# In[42]:


soup.title


# In[43]:


"title" in dir(soup)


# In[44]:


len(soup.find_all("p"))


# In[45]:


soup.table["class"]


# In[46]:


[t["class"] for t in soup.find_all("table") if t.get("class")]


# In[47]:


my_list = []
for t in soup.find_all("table"):
    if t.get("class"):
        my_list.append(t["class"])
my_list


# In[49]:


table_html = str(soup.findAll("table", "wikitable")[2])


# In[50]:


from IPython.core.display import HTML

HTML(table_html)


# In[51]:


rows = [row for row in soup.findAll("table", "wikitable")[2].find_all("tr")]
rows


# In[78]:


rem_nl = lambda s: s.replace("\n", "")


# In[28]:


def power(x, y):
    return x**y
power(2, 3)


# In[80]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns


# In[83]:


indexes = [rem_nl(row.find("th").get_text()) for row in rows[1:]]
indexes


# In[84]:


HTML(table_html)


# In[85]:


to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None


# In[86]:


values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
values


# In[87]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[88]:


HTML(table_html)


# In[90]:


def print_args(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
print_args(1, 2, 3)
print_args([1, 10], [2, 20], [3, 30])


# In[91]:


parameters = [100, 200, 300]
p1 = parameters[0]
p2 = parameters[1]
p3 = parameters[2]
print_args(p1, p2, p3)


# In[92]:


p4, p5, p6 = parameters
print_args(p4, p5, p6)


# In[93]:


print_args(*parameters)


# In[97]:


import pandas as pd
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df


# In[100]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts


# In[101]:


pd.DataFrame(data_dicts, index=indexes)


# In[102]:


df.dtypes


# In[103]:


df.dropna()


# In[104]:


df.dropna(axis=1)


# In[105]:


df_clean = df.fillna(0).astype(int)
df_clean


# In[106]:


df_clean.dtypes


# In[107]:


df_clean.describe()


# In[109]:


import numpy as np
df_clean.values


# In[112]:


type(df_clean.values)


# In[114]:


np.mean(df_clean.Undergrad)


# In[115]:


np.std(df_clean)


# In[124]:


df_clean["Undergrad"]


# In[125]:


df_clean.Undergrad


# In[126]:


df_clean.loc["Asian/Pacific Islander"]


# In[127]:


df_clean.iloc[0]


# In[128]:


df_clean.ix["Asian/Pacific Islander"]


# In[122]:


df_clean.ix[0]


# In[129]:


df_clean.loc["White/non-Hispanic", "Graduate"]


# In[131]:


df_clean.ix[3, "Graduate"]


# In[132]:


df_clean.iloc[3, 1]


# In[133]:


df_clean.ix[3, "Graduate"]


# In[134]:


df_flat = df_clean.stack().reset_index()
df_flat.columns = ["race", "source", "percentage"]
df_flat


# In[135]:


grouped = df_flat.groupby("race")
grouped.groups


# In[136]:


type(grouped)


# In[137]:


mean_percs = grouped.mean()
mean_percs


# In[138]:


type(mean_percs)


# In[139]:


for name, group in df_flat.groupby("source", sort=True):
    print(name)
    print (group)


# In[140]:


get_ipython().run_line_magic('matplotlib', 'inline')
mean_percs.plot(kind="bar");


# In[ ]:




