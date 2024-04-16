# steps-to-deploy-locally-on-docker

## https://hub.docker.com/_/ubuntu


## install docker

```bash
	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

    docker --version
```

## download image

```bash
docker pull ubuntu
```

## Create and start docker container interactive and detach with code mapping for ubuntu image
```bash
docker run -dit -p 8501:8501 ubuntu /bin/bash
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
```

## update container
```bash
apt-get update -y
```
```bash
apt-get upgrade -y
```
## install mutliple softwares
```bash
apt install git curl unzip tar make sudo vim wget nano -y
```
# choose you region and country when prompt

apt install python3-pip

## install python      
```bash
apt-get install python3
```

## install pip      
```bash
apt-get install pip -y
```



## git clone
```bash
git clone https://github.com/entbappy/Multilingual-AI-Assistant.git
```

## change directory to clonned repository
```bash
cd Industry-Safety-Detection-using-Yolov7
```



sudo apt install portaudio19-dev
python3 -m  pip install PyAudio

## install all requirement
```bash
pip3 install -r requirements.txt
```



## execute application

# Temporary running
```bash
python3 -m streamlit run app.py
```

# Permanent running
```bash
nohup python3 -m streamlit run app.py
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
```

# docker image

https://docs.docker.com/engine/reference/commandline/image/#examples


## to list all images
```bash
docker image ls
```

# docker command line interface (cli)

```bash
https://docs.docker.com/engine/reference/commandline/


 AWS_ACCESS_KEY_ID=
 AWS_SECRET_ACCESS_KEY=
 AWS_DEFAULT_REGION=
```

## to stop all running container (reference only)
```bash
docker stop $(docker ps -a -q)
```

## to remove all stopped container (reference only)
```bash
docker rm $(docker ps -a -q)
```

## to remove all images
```bash
docker rmi $(docker images -a -q)
```

## to list all containers (reference only)
```bash
docker ps -a
```

## to list all images (reference only)
```bash
docker image ls
```

# docker-compose

https://docs.docker.com/compose/


# dockerfile

```bash
https://docs.docker.com/engine/reference/builder/#run
```


