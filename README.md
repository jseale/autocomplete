[![Maintainability](https://api.codeclimate.com/v1/badges/a032938fea133db21c0d/maintainability)](https://codeclimate.com/repos/5beb899a714428026d005548/maintainability)

# asapp_autocomplete 
The asapp_autocomplete library runs a server which takes in a user-generated text string (a prefix) and returns up to five autocompletions. Ranking of autocompletions is based on the frequency of customer service representative-generated message instances in a corpus of chat messages with customers.

## Motivation 
This library exists as something of a 'Hello ASAPP' from Jen Seale. It is a response to the coding challenge provided as part of the hiring process for the position of [Machine Learning Engineer](https://jobs.lever.co/asapp-2/20112e96-2c3b-41e7-a602-61edb8e998b7).

## Dependencies 
Conda 4.5.11<br />

_Conda will be used to install further dependencies, including Python 3.7.1. See Installation section.<br />
For more information on Conda, see: https://conda.io/docs/_

## Installation 
```
git clone https://github.com/jseale/asapp_autocomplete.git
```
Create the `autocomplete` environment and install dependencies into it by issuing: <br /> 
```
cd asapp_autocomplete
conda env create -f environment.yml
```

To activate the environment:<br />
```
conda activate autocomplete
```

## Usage 
To run the server, in an activated environment issue: 

```
ipython autocomplete_server.py
```
`autcomplete_server.py` is found in `asapp_autocomplete/library/server`.

To query the server, issue curl commands such as: 
```
curl localhost:5000/autocomplete?q=what+is+your
```

## Documentation

The challenge writeup is found in: <br/>
```
asapp_autocomplete/docs
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
To run tests, cd to the `asapp_autocomplete` directory, and issue: <br />
```
pytest
```

