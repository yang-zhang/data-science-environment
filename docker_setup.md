### Build docker image
Under `data-science-environment/docker/`, run
```
docker build --file dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```
### Add shortcuts 
In `.bash_profile`, add
```
# For docker start
alias dcf='declare -F'

python_dk() {
  docker run -v ~/git:/tmp -w=/tmp  --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; python "$@"'
}
ipython_dk() {
  docker run -v ~/git:/tmp -w=/tmp --rm  -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; ipython'
}
jn_dk() {
  docker run -v ~/git:/tmp -w=/tmp -p 8888:8888 --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; jupyter notebook --no-browser --ip="0.0.0.0" --notebook-dir=/tmp' 
}
dk_ds() {
  docker run --rm -v ~/git:/tmp -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; bash'
}
# For docker end
```
