
# coding: utf-8

# ## Which python am I using

# In[2]:

get_ipython().system('which python')


# In[1]:

import sys; sys.executable


# ## Add path to top of `PYTHONPATH` to override other namespaces
# 
# Instead of: 
# ```
# sys.path.append('path/to/new/library')
# ```
# Use:
# ```
# sys.path.insert(1, 'path/to/new/library')
# ```
