
# coding: utf-8

# ## Jupyter TODO
# http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html

# ## Frequent imports and configurations

# In[17]:

get_ipython().magic('matplotlib inline')
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt


# In[ ]:

# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# pd.options.display.max_columns = None

# from IPython.core.pylabtools import figsize
# figsize(11, 9)

# Set numpy display precision
# np.set_printoptions(precision=4, linewidth=100)


# In[1]:

get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.auto_scroll_threshold = 9999;')


# ## IPython Magics

# ### %who: List all variables of global scope.

# In[18]:

a=1; b=2; c='hi'
get_ipython().magic('who')
get_ipython().magic('who str')


# ### Timing

# In[19]:

get_ipython().run_cell_magic('time', '', 'for i in range(int(10e5)):\n    pass')


# ## Pass variables to bash

# In[21]:

a = '~'; b = 'git'
get_ipython().system('ls $a | grep $b')


# ## Download file from remote machine

# In[22]:

from IPython.display import FileLink
FileLink('README.md')


# ## Suppress the output of a final function
# By adding a semicolon at the end, the output is suppressed.
# 

# In[10]:

plt.plot([1,2], [2,4])


# In[11]:

plt.plot([1,2], [2,4]);


# ## Display image file

# In[14]:

fig, ax = plt.subplots()
ax.plot([1,2],[2,4])
fig.savefig('_.png')


# In[15]:

from IPython.display import Image 
Image("_.png")


# ## Latex
# 
# To show:
# $
# p(t|x, \textbf{x}, \textbf{t}) 
# = \int p(t|x, \textbf{w}) 
# p(\textbf{w}| \textbf{x}, \textbf{t}) d\textbf{w}
# $
# 
# Note that:
# $$
# p(t|x, \textbf{x}, \textbf{t}) 
# = \int p(t|x, \textbf{w}) 
# p(\textbf{w}| \textbf{x}, \textbf{t}) d\textbf{w}
# $$

# In[24]:

get_ipython().run_cell_magic('latex', '', 'As code: $P(A \\mid B) = \\frac{P(B \\mid A) \\, P(A)}{P(B)}$')


# ## References
# - https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
