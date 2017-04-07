# Jupyter Setup

## Jupyter notebook autosave to python file and html file
Saving notebook into python files for easier version control. Save [`jupyter_notebook_config.py`](https://github.com/yang-zhang/ds-env/blob/master/jupyter_notebook_config.py) as `~/.jupyter/jupyter_notebook_config.py`. For jupyter in docker, see [here](https://github.com/yang-zhang/ds-env/blob/master/docker/dockerfiles/yang-zhang-ds.docker#L8). 
Reference [here](http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html)


## Jupyter notebook extensions
Install [Jupyter notebook extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) and [Jupyter Nbextensions Configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator) using the conda option.
- Expand and collapse Sections: At home page, in "Nbextensions" tab select "Collapsible Headings".
- Table to contents: At home page, in "Nbextensions" tab select "Table of Contents".
Note! Installing extensions will break nbconvert (for slideshow): see [here](http://stackoverflow.com/questions/38723801/typeerror-when-executing-jupyter-nbconvert); need to run conda update conda to fix.

## Display all variables in the same cell
### Permenant
If you want to set this behaviour for all instances of Jupyter (Notebook and Console), simply create a file `~/.ipython/profile_default/ipython_config.py` with the lines below.
```
c = get_config()
# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"
```
### Temperary
In notebook, run:
```
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
