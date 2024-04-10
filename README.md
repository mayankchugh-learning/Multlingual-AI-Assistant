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
conda create -p multlingual python=3.8 -y
```

```bash
conda activate multlingual
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
- PaLM2
- s2t
- t2s
