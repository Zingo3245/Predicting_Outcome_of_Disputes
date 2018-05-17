# Predicting the Outcome of Disputes between Countries
When a dispute between countries breaks out, there are no shortage of pundits who believe they have all the answers. Unfortunately bias can often lead predictions to be way off. Using the [Militarized Interstate Disputes(MID)](http://cow.dss.ucdavis.edu/data-sets/MIDs) dataset, I built a model to predict the outcome of different disputes from 1816 to 2010.

[Link to the presentation is here.](https://docs.google.com/presentation/d/1j4Gu6SuJyGn68_YcNFo4NaEHzooQBHnvtJcA2OjVJ_k/edit?usp=sharing)
## Tools used
* SKLearn
* Flask
* PSQL(through Amazon EC2)
## Installation
```bash
pip install -r requirements.txt 
python3 viz.py 
```
## Deployment
* Open Jupyter notebook through the anaconda navigator and select Cleaned_McNulty
* Open the notebook and select Run All Cells
* Run app viz.py
* Navigate to 127.0.0.1:5000 to see some examples

## Structure
* Data: Files that contain both the raw and processed data used in the analysis
* Flask_app: Files related to running the Flask app
* IPython_notebooks: Contains the notebooks used to code in Python
* Presentation: Contains a pdf version of the presentation