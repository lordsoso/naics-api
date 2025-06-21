#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install flask pandas openpyxl')


# In[8]:


from flask import Flask, jsonify
import pandas as pd


# In[9]:


# Load Excel data
df = pd.read_excel("Final_Merged_NAICS_Intelligence_File.xlsx")
df.fillna("", inplace=True)


# In[10]:


# Initialize Flask app
app = Flask(__name__)

@app.route("/api/data")
def get_all_data():
    return jsonify(df.to_dict(orient="records"))

@app.route("/api/naics/<code>")
def get_by_naics(code):
    filtered = df[df["NAICS Code"] == code]
    return jsonify(filtered.to_dict(orient="records"))

@app.route("/api/keyword/<keyword>")
def search_keyword(keyword):
    mask = df["Industry Term / Keyword"].str.contains(keyword, case=False) | df["Notes"].str.contains(keyword, case=False)
    filtered = df[mask]
    return jsonify(filtered.to_dict(orient="records"))


# In[ ]:


# ✅ This is what Render needs to start your app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


# In[ ]:





# In[ ]:




