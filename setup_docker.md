# Docker Setup

## Build docker image
Under `ds-env/`, run
```bash
docker build --file docker/dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```
## Add shortcuts 
In `.bash_profile`, add
```bash
# For docker start
alias dcf='declare -F'

# run python in docker
python_dk() {
  docker run -v ~/git:/tmp -w=/tmp  --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; python "$@"'
}
# run ipython in docker
ipython_dk() {
  docker run -v ~/git:/tmp -w=/tmp --rm  -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; ipython'
}
# run jupyter notebook in docker
jn_dk() {
  docker run -v ~/git:/tmp -v ~/Storage:/tmp/storage -w=/tmp -p 8888:8888 --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; jupyter notebook --no-browser --ip="0.0.0.0" --notebook-dir=/tmp' 
}
# run bash in docker
dk_ds() {
  docker run --rm -v ~/git:/tmp -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; bash'
}

# For docker end
```
