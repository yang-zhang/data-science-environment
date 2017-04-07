
# coding: utf-8

# ## Configurations

# In[ ]:

pd.options.display.max_columns = None


# In[ ]:

from IPython.core.pylabtools import figsize
figsize(11, 9)


# In[ ]:

# Set numpy display precision
np.set_printoptions(precision=4, linewidth=100)


# In[1]:

get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.auto_scroll_threshold = 9999;')


# ## Download file (useful when running jupyter on remote machine)

# In[22]:

from IPython.display import FileLink
FileLink('README.md')


# ## IPython Magics

# ### %who: List all variables of global scope.

# In[3]:

a=1; b=2; c='hi'


# In[4]:

get_ipython().magic('who')


# In[5]:

get_ipython().magic('who str')


# ### Timing

# In[19]:

get_ipython().run_cell_magic('time', '', 'for i in range(int(10e5)):\n    pass')


# ## Pass variables to bash

# In[21]:

a = '~'; b = 'git'
get_ipython().system('ls $a | grep $b')


# ## Suppress the output of a final function
# By adding a semicolon at the end, the output is suppressed.
# 

# In[3]:

def print_and_return(a):
    print(a)
    return 1


# In[6]:

print_and_return('a')


# In[7]:

print_and_return('a');


# ## Display image file

# In[9]:

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2],[2,4])
fig.savefig('_.png')


# In[10]:

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

# In[11]:

get_ipython().run_cell_magic('latex', '', 'As code: $P(A \\mid B) = \\frac{P(B \\mid A) \\, P(A)}{P(B)}$')


# ## References
# - https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
