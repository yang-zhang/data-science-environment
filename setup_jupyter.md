# Jupyter Setup and Tips

## Jupyter notebook extensions
Install [Jupyter notebook extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) and [Jupyter Nbextensions Configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator) using the conda option.
- Expand and collapse Sections: At home page, in "Nbextensions" tab select "Collapsible Headings".
- Table to contents: At home page, in "Nbextensions" tab select "Table of Contents".
Note! Installing extensions will break nbconvert (for slideshow): see [here](http://stackoverflow.com/questions/38723801/typeerror-when-executing-jupyter-nbconvert); need to run conda update conda to fix.

## Configurations
```
pd.options.display.max_columns = None

from IPython.core.pylabtools import figsize
figsize(11, 9)

Set numpy display precision
np.set_printoptions(precision=4, linewidth=100)

%%javascript
IPython.OutputArea.auto_scroll_threshold = 9999;
```

## Display all variables in the same cell
### In notebook, run:
```
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
### If you want to set this behaviour for all instances of Jupyter (Notebook and Console), simply create a file `~/.ipython/profile_default/ipython_config.py` with the lines below.
```
c = get_config()
# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"
```

## Slideshow using Jupyter
See [here](http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html):
```
jupyter nbconvert my_notebook.ipynb --to slides --post serve
```


