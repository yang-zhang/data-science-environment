# Deep Learning Setup


## Modules to install
- bcolz
- theano
- keras
  - [Issue](https://github.com/fchollet/keras/issues/5870) with new keras version 2.0.1. Instead use
  ```
  conda install -c conda-forge keras=1.2.2
  ```

## Set Keras backend
Show what backend is being used in code:
```
keras.backend.backend()
```
### In code
```
os.environ["KERAS_BACKEND"] = "theano"
```

### In `~/.keras/keras.json`

#### Use Theano backend:
```
{
    "image_dim_ordering": "th", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "theano"
}
```

#### Use Tensorflow backend:
```
{
    "image_dim_ordering": "tf", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "tensorflow"
}
```

### In `.bash_profile`
```
export KERAS_BACKEND="theano"
```

## Make theano use cpu instead of gpu
Where is `.theanorc`? There is no such file but can be created by running (as instructed [here](http://stackoverflow.com/questions/21608025/how-to-set-up-theano-config))
```
echo -e "\n[global]\nfloatX=float32\n" >> ~/.theanorc
```
Then set `~/.theanorc` to be
```
[global]
device=cpu
floatX=float32
```
## Use Theano dim ordering
```
from keras import backend as K
K.set_image_dim_ordering('th')
```
See comments "get (None, -1, 26, 32) instead, what’s happening" [here](https://elitedatascience.com/keras-tutorial-deep-learning-in-python)

## For [fast.ai](http://www.fast.ai/), use py27 virtual env.
