[![Maintainability](https://api.codeclimate.com/v1/badges/a032938fea133db21c0d/maintainability)](https://codeclimate.com/repos/5beb899a714428026d005548/maintainability)

# autocomplete 
The autocomplete library provides functionality to run a server that allows for queries of user-generated text strings (prefixes) and returns up to five autocompletions. Ranking of autocompletions is based on the frequency of agent-generated message instances in a corpus of chat messages.

## Motivation 
This library exists as a response to a coding challenge.

## Dependencies 
Conda 4.5.11<br />

_Conda will be used to install further dependencies, including Python 3.7.1. See Installation section.<br />
For more information on Conda, see: https://conda.io/docs/_

## Installation 
```
git clone https://github.com/jseale/autocomplete.git
```
Create the `autocomplete` environment and install dependencies into it by issuing: <br /> 
```
cd autocomplete
conda env create -f environment.yml
```

To activate the environment:<br />
```
conda activate autocomplete
```

## Usage 
After activating the environment, issue: 
```
ipython autocomplete_server.py
```
to activate the server. `autocomplete_server.py` is found in `autocomplete/library/server`.

Query the server with curl commands such as this: 
```curl localhost:5000/autocomplete?q=what+is+your```

Or enter your query in cell 21 of `challenge_writeup.ipynb`.

## Documentation
The challenge writeup is found in: <br/>
```
autocomplete/docs
```
To view the challenge writeup, cd to `docs`, issue the following, 
and view `challenge_writeup.ipynb` in your browser. <br />
```
jupyter notebook
```
The above works if you are running this code locally. If the code is on a remote host, 
port forwarding will allow you to view the notebook. 

### challenge_writeup.ipynb
Choose the `autocomplete` kernel to run code in the notebook.

If the autocomplete environment does not appear as a kernel in the notebook, issue the following
while the environment is activated:<br />
```
python -m ipykernel install --user --name autocomplete --display-name "autocomplete"
```

## Tests
To run tests, cd to the `autocomplete` directory, and issue: <br />
```
pytest
```

