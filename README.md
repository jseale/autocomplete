# autocomplete 
The autocomplete library provides functionality to run a server that allows for queries of user-generated text strings (prefixes) and returns up to five autocompletions. Ranking of autocompletions is based on the frequency of agent-generated message instances in a corpus of chat messages. The chat message data and the server code are not available in this repo.

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
After activating the environment, were the server available, you would issue the following commmand: 
```
ipython autocomplete_server.py
```
to activate the server. 

You would then query the server with curl commands such as this: 
```curl localhost:5000/autocomplete?q=what+is+your```


## Tests
To run tests, you would cd to the `autocomplete` directory, and issue: <br />
```
pytest
```

