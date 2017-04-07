## Deep Learning
For [fast.ai](http://www.fast.ai/), use py27 virtual env.
Modules to install
- bcolz
- theano
- keras
  - [Issue](https://github.com/fchollet/keras/issues/5870) with new keras version 2.0.1. Instead use
  ```
  conda install -c conda-forge keras=1.2.2
  ```

##Set Keras backend
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
