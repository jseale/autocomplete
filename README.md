# asapp_autocomplete 

## Motivation 
This library exists as something of a 'Hello ASAPP' from Jen Seale. It is a response to the coding challenge provided as part of the hiring process for the position of [Machine Learning Engineer](https://jobs.lever.co/asapp-2/20112e96-2c3b-41e7-a602-61edb8e998b7).

## Dependencies 
Python 3.7.1<br />
Conda<br />

## Installation 
```
git clone https://github.com/jseale/asapp_autocomplete.git
```

Create the environment with dependencies installed by issuing: <br /> 
```
cd autocomplete
conda env create -f environment.yml
```

To activate the environment:<br />
```
conda activate autocomplete
```

## Usage 

## Documentation
The challenge writeup is found in: <br/>
```
```

To view the challenge writeup, issue the following and view `writeup.ipynb` in your browser.
```
cd autocomplete\documents
jupyter notebook
```

If the autocomplete environment does not appear as a kernal in the notebook, issue the following
while the environment is activated:<br/>
```
python -m ipykernel install --user --name autocomplete --display-name "autocomplete"
```

## Tests
To run tests: 
```
cd autocomplete
pytest
```

