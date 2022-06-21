#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 
# # Workshop home
# 
# **Intro to Python: Pandas for Metadata Transformation and Cleanup**<br>
# Hosted by [Northeast Institutional Repository Day (NIRD)](https://escholarship.umassmed.edu/neirug/)<br>
# March 2022<br>
# 
# ## Introductions
# 
# Hi all, I'm Michelle Janowiecki (she/her). Since 2019, I've worked as metadata librarian at [Johns Hopkins University Sheridan Libraries](https://www.library.jhu.edu/). I currently live in Baltimore with my dog and my husband.
# 
# Feel free to connect with me online: [![icons8-github-50](img/icons8-github-50.png)](https://github.com/mjanowiecki) [![icons8-gitlab-50](img/icons8-gitlab-50.png)](https://gitlab.com/mjanowiecki) [![icons8-twitter-50](img/icons8-twitter-50.png)](https://twitter.com/michellejano)
# 
# Please feel introduce yourself in the chat if you feel comfortable! Share:
# - Your name and pronouns
# - Where you are zooming from
# - What you are hoping to learn
# - Your favorite animal
# 
# My favorite animals are manatees!
# 
# ## Overview of pandas
# 
# This workshop covers some basics of the [pandas](https://pandas.pydata.org/) library. The pandas library is an open-source Python library that is very popular for data manipulation and analytics acrosss a wide array of displicines. Here are some tasks that pandas is great at:
# 
# - Reading and writing data between different formats (CSV, JSON, XML, Excel, SQL, and more)
# - Merging and joining data
# - Reshaping and pivoting data
# - Handling missing data
# - Getting quick overviews of data values
# - Literally anything data analysis and visualization!
# 
# ## Workshop details
# 
# ### Schedule
# 
# **Introductions and overview**<br> 
#      *10 minutes*
# 
# [**1. Basics of Series and DataFrames**](basics-df)<br>
#    *20 minutes*<br>
# 
# ````{panels}
# :body: text-left
# :header: text-left
# 
# *Concepts covered:*
# ^^^
#    + What is a DataFrame?
#    + What is a Series?
#    + How to create a DataFrame from a CSV
#    + How to use of indexes and labels to evaluate and find data
# ---
# 
# *Methods covered:*
# ^^^
#    + `read_csv()`
#    + `head()` and `tail()`
#    + `column()`
#    + `shape()`
#    + `empty()`
#    + `loc` and `iloc`
#    + `at` and `iat`
#    + `unique()` and `value_counts()`
# 
# ````
# 
# [**2. How to clean data**](clean-up)<br>
#    *20 minutes*<br>
#    
# ````{panels}
# :body: text-left
# :header: text-left
# 
# *Concepts covered:*
# ^^^
#    + Missing values ('na')
#    + Duplicates
#    + String handling
#    + How to write a CSV from a DataFrame
#    
# ---
# 
# *Methods covered:*
# ^^^
#    + `isna()` and `notna()`
#    + `duplicate()`
#    + `dropna()` and `drop_duplicates()`
#    + `iterrows()`
#    + `apply()`, `str.rstrip()`, `str.zfill()`, and `str.strip()`
# 
# ````
# 
# [**3. How to merge data by identifiers or strings**](merging-pd)<br>
#    *20 minutes*<br>  
# ````{panels}
# :body: text-left
# :header: text-left
# 
# *Concepts covered:*
# ^^^
#    + Merging two DataFrames 
#    + Types of merges (left, right, inner, outer)
# ---
# 
# *Methods covered:*
# ^^^
#    + `merge()`
# ````
# 
# [**4. How to reshape data**](reshape-pd)<br> 
#    *25 minutes*<br>
# ````{panels}
# :body: text-left
# :header: text-left
# 
# *Concepts covered:*
# ^^^
#    + Exploding
#    + Pivoting
#    + Melting
#    + Aggregating values
# ---
# 
# *Methods covered:*
# ^^^
#    + `explode`
#    + `pivot()`
#    + `pivot_table()`
#    + `lambda`
#    + `melt()`
#  ````
#  
# **Additional resources and final questions**<br>
# *10 minutes*
# 
# ---
# 
# ### Workshop tips
# 
# 1. If you are lost, other people are lost, and your questions will help us all get less lost! Please ask away by typing in the chat. I'll periodically pause to answer questions that come up.
# 2. Please keep yourself muted unless talking to help us all hear.
# 3. Take care of yourself. Whether that's drinking lots of tea ☕, taking little breaks 💤, or turning off your camera for focusing purposes 💭, I'm totally cool with it. 
# 
# ### Workshop tools and data
# 
# #### Tools
# 
# **Versions**
# 
# Python and pandas are continuously updated, so it's important to know what version you need for your script to work. We are using the following versions for this workshop.
# 
# - [Python version: 3.8+](https://www.python.org/doc/versions/)
# - [pandas version: 1.3.4+](https://pandas.pydata.org/docs/whatsnew/index.html)
# 
# **Jupyter Notebook Setup**
# 
# This workshop is being run on [Jupyter Notebook](https://docs.jupyter.org/en/latest/start/index.html) which is a open-source tool that lets you store and run Python code alongside text, images, and other types of documentation. You can download and run Jupyter Notebook on your own computer, but this instance is hosted on [binder](https://jupyter.org/binder), which allows us to run Python 3 scripts directly in a browser. This setup was chosen for its minimal setup and teaching possiblities, but you don't have to use Jupyter Notebook to use Python. 
# 
# **Alternative Python set-up**
# 
# If you don't want to use Jupyter Notebook for your future Python projects, check out this [basic setup](https://gitlab.com/mjanowiecki/python-lessons-for-librarians/-/wikis/Setting-up-Python) using Anaconda and Atom. 
# 
# #### Data
# 
# I'm using slightly altered data for this workshop from [Johns Hopkins University's Electronic Thesis and Dissertations](https://jscholarship.library.jhu.edu/handle/1774.2/836). Please re-use respectfully.
# 
# #### Supplemental files
# 
# Supplemental files
# 
# - {Download}`Python scripts as .py files<./scripts.zip>`
# - {Download}`Raw CSV data<./csv.zip>`
# ---
# 
# ## Copyright
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

# In[ ]:




