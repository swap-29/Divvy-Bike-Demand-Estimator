# Divvy-Bike-Demand-Estimator

Final project for the MBS course "Intro to Data Analytics and Discovery Informatics" at Rutgers University.

## Summary
This project estimates the demand of Divvy bikes in Chicago, taking weather conditions and whether the particular day is a holiday or not. The prediction is done based on regression models in the scikit-learn library; the models used were:

* Linear Regression
* Lasso and Ridge Regression
* Decision Tree Regression
* Random Forest Regression

The preprocessing notebook, __preprocessing.ipynb__, cleans the data and provides a cleaned dataset as well as the original merged data. 
__analysis.ipynb__ plots the graphs needed to analyze the data, for the exploratory data analysis, and __regression_techniques.ipynb__ runs the regression models and fits the models with the data.

## To Run the Project

* To run the project, download data from the official Divvy website: <https://divvy-tripdata.s3.amazonaws.com/index.html>
* Clone the repo and separate the datasets into separate folders. 
* Run the preprocessing notebook to get the cleaned dataset.
* Run regression_techniques.ipynb to get the models.

"# Divvy-Bike-Demand-Estimator" 
