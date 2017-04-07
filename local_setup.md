# Software Setup
Setting up software environement for Data Science.
## Conda
Environment
If you have conda3, Install Python2.7 with everything that comes with anaconda
`conda create -n py27 python=2.7 anaconda`
If you have conda2, Install Python3.5 with everything that comes with anaconda
`conda create -n py35 python=3.5 anaconda`
Clone from existing env
```conda create -n new_env --clone root```

xgboost
Conda's version is old.
cd Downloads
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; cp make/minimum.mk ./config.mk; make -j4
cd python-package; sudo python setup.py install
.bash_profile
export PYTHONPATH="/Users/yangzhang/git/ds-utils:/Users/yangzhang/secrets:$PYTHONPATH"

alias jn='jupyter notebook'
alias sa='source activate'
alias sda='source deactivate'
secrets.py
In ~/secrets/secrets.py:
AWS_KEY='ABC123'
AWS_SECRET='ABCXYZ'

KAGGLE_USER='zhangyang'
KAGGLE_PW='123'
Imports
Add the following to the beginning of code for frequent modules and setups.
import ds_utils.imports; import imp; imp.reload(ds_utils.imports)
from ds_utils.imports import
https://github.com/yang-zhang/ds-utils/blob/master/ds_utils/imports.py
git
git setup for contributing to repo (http://kbroman.org/github_tutorial/pages/fork.html)
Fork the repo on github (e.g. https://github.com/dmlc/xgboost)
Clone your forked repo: git clone https://github.com/yang-zhang/xgboost
Add original owner’s repository: cd xgboost; git remote add dmlc https://github.com/dmlc/xgboost
Show remote repo: git remote -v
Add remote branch
git checkout --track origin/name_of_the_remote_branch
Jupyter
Jupyter notebook extensions
Install Jupyter notebook extensions and Jupyter Nbextensions Configurator using the conda option.
Expand and collapse Sections: At home page, in "Nbextensions" tab select "Collapsible Headings".
Table to contents: At home page, in "Nbextensions" tab select "Table of Contents".
Note! Installing extensions will break nbconvert (for slideshow): see (http://stackoverflow.com/questions/38723801/typeerror-when-executing-jupyter-nbconvert); need to run conda update conda to fix.
Configurations
In [8]:
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# pd.options.display.max_columns = None

# from IPython.core.pylabtools import figsize
# figsize(11, 9)

# # Set numpy display precision
# np.set_printoptions(precision=4, linewidth=100)
In [9]:
%%javascript
IPython.OutputArea.auto_scroll_threshold = 9999;
<IPython.core.display.Javascript object>
Display all variables in the same cell
In notebook, run:
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
If you want to set this behaviour for all instances of Jupyter (Notebook and Console), simply create a file ~/.ipython/profile_default/ipython_config.py with the lines below.
c = get_config()
# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"
In [10]:
a=1; b=2;
a
b
Out[10]:
1
Out[10]:
2
Slideshow using Jupyter
http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html
jupyter nbconvert my_notebook.ipynb --to slides --post serve
Deep Learning
For fast.ai, use py27 virtual env.
Modules to install
bcolz
theano
keras
Issue with new keras version 2.0.1. Instead use
conda install -c conda-forge keras=1.2.2
Set Keras backend
In ~/.keras/keras.json:
Theano backend
{
    "image_dim_ordering": "th", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "theano"
}
Tensorflow backend
{
    "image_dim_ordering": "tf", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "tensorflow"
}
In .bash_profile:
export KERAS_BACKEND="theano"
In code:
Set
os.environ["KERAS_BACKEND"] = "theano"
Make theano use cpu instead of gpu
Where is .theanorc? There is no such file but can be created by running (as instructed here)
echo -e "\n[global]\nfloatX=float32\n" >> ~/.theanorc
Then set ~/.theanorc to be
[global]
device=cpu
floatX=float32
Use Theano dim ordering
from keras import backend as K
K.set_image_dim_ordering('th')
See comments "get (None, -1, 26, 32) instead, what’s happening" here
R
Add R kernal:
conda install -c r r-essentials
Install package
In code:
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages(ro.StrVector(['entropy', 'psych', 'vcd']))
Run a R kernal in Jupyter and run
install.packages(c('entropy', 'psych', 'vcd'))
Misc
Python 2 to 3
2to3 -w example.py
Control video speed
Google YouTube Keyboard Shortcuts
Video Speed Controller - Chrome extension
Kaggle
!kg config -g -u $KAGGLE_USER -p $KAGGLE_PW -c $competition_name
!kg download
!kg submit $submit_file -u $KAGGLE_USER -p $KAGGLE_PW -m $model_description
top sort by memory usage
top -o MEM
