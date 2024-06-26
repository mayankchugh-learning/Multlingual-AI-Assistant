# Multlingual-AI-Assistant


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```
### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p multlingual python -y
```

```bash
source activate ./multlingual
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```


### Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- Google API
- Streamlit
- Google Gemini-Pro
- s2t
- t2s

# How to Deploy Streamlit app on EC2 instance

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```


```bash
git clone "Your-repository"
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```

```bash
#Temporary running
python3 -m streamlit run app.py
```

```bash
#Permanent running
nohup python3 -m streamlit run app.py
```

Note: Streamlit runs on this port: 8501