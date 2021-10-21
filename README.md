# autocomplete 
The autocomplete library provides functionality to run a server that allows for queries of user-generated text strings (prefixes) and returns up to five autocompletions. Ranking of autocompletions is based on the frequency of agent-generated message instances in a corpus of chat messages. The chat message data is not available in this repo.

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


## Tests
To run tests, cd to the `autocomplete` directory, and issue: <br />
```
pytest
```

