# Query.AI Script HUB

## Background
**Requirements (Global)**
1. Python 3.8+
2. pipenv - https://pypi.org/project/pipenv/

**Configuration Explained**
1. There is a sample environment variables file called .env_sample under the root folder of this project
2. You will clone this file and create one called .env where you actually input all of your secrets (API Keys + Access Key Pairs)

**Parameters - explainations of what you see in .env_sample**
1. PYTHONPATH - this is the path you clone this repo to + the repo root directory
2. org_name - name of your Query.AI Organizaton
3. jwt - your JWT token which can be found under your user profile



## Getting Started
1. Clone this repository
```
git clone https://github.com/tdiderich/queryai-scripts.git
```
2. Clone .env_sample to .env under the same directory
```
cp .env_sample .env
```
3. Update all of the secrets needed based on the script you'd like to run (NOTE: you need to rerun pipenv shell anytime you update these values to reload them)
```
# PYTHON - this should be the path you cloned this repo into + /queryai-scripts
PYTHONPATH=/path/to/queryai-scripts

# AUTHENTICATION INFO
org_name=<org_name>
jwt=<from_user_profile>
```
4. Create pip environment
```
pipenv --three
```
5. Install dependancies
```
pipenv install
```
6. Enter pipenv
```
pipenv shell
```
7. Run scripts
```
python3 foo/bar.py
```
