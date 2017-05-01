# Using Docker

## Get image and run
```
docker pull julia
docker run -it --rm julia
```

## Get inside a running container
```
docker ps
sudo docker exec -it gallant_fermat bash
```
### Get inside the 
```
docker exec -it $(docker ps -l -q) bash
```

## Stop and delete all containers
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Build image
```
docker build --file dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```

## Map disk and run
```
docker run -it --rm -v "$PWD":/usr/myapp -w /usr/myapp julia julia test.jl
```

## Append to env variables
```
docker run --rm -v $PWD:/tmp -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils; bash' 
```
