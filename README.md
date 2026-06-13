# ATM Cash Demand Predictor
```
Project Title: ATM Cash Demand Predictor
Author(s): Samyak Shambharkar
Affiliation: Suryodaya College Of Engineering and Technology
Date: June 2026
```

## Abstract
```
Automated Teller Machines (ATMs) are an essential part of modern banking services. Maintaining an optimal cash balance in ATMs is a challenging task for banks because understocking may lead to cash shortages while overstocking increases operational costs and security risks. This project presents an ATM Cash Demand Predictor that utilizes Machine Learning techniques to estimate the amount of cash required by an ATM for the next day. The system uses historical transaction data and operational factors such as withdrawals, deposits, location type, holidays, weather conditions, and previous cash levels to generate predictions. Multiple regression algorithms including Linear Regression, Decision Tree Regressor, Random Forest Regressor, and Gradient Boosting Regressor were evaluated. Linear Regression achieved the best overall performance with an R² score of approximately 87%. The trained model was deployed using Streamlit to provide an interactive user interface for prediction. The proposed system can assist banks in optimizing ATM cash replenishment decisions, reducing cash shortages, and improving operational efficiency. The project demonstrates the complete Machine Learning workflow, including data preprocessing, feature engineering, model training, evaluation, deployment, and future scalability toward a fully automated ATM management solution.
```

## Introduction
```
ATMs play a vital role in providing banking services to customers at any time and location. One of the major challenges faced by banks is determining the correct amount of cash to maintain in each ATM. Excess cash increases storage and transportation costs, while insufficient cash may lead to customer dissatisfaction due to cash unavailability.

The objective of this project is to develop a Machine Learning-based system capable of predicting future ATM cash demand using historical transaction data and environmental factors. By forecasting future cash requirements, banks can make informed decisions regarding ATM replenishment schedules and cash allocation strategies. This project aims to demonstrate how Machine Learning can be applied to solve real-world operational problems in the banking sector.
```
## Literature review
```
Several financial institutions use predictive analytics and demand forecasting techniques to optimize ATM operations. Traditional methods rely on historical averages and manual planning, which may not adapt well to changing customer behavior.

Research in demand forecasting highlights the effectiveness of Machine Learning algorithms such as Linear Regression, Random Forest, and Gradient Boosting for predicting financial and operational metrics. Studies have shown that factors such as transaction volume, location, holidays, and seasonal trends significantly influence ATM cash demand.

Recent advancements in predictive analytics and intelligent banking systems have encouraged the adoption of AI-driven solutions that automate cash management processes and improve operational efficiency.
```

## Methodology
```
The project follows a supervised Machine Learning approach for regression analysis. Historical ATM transaction data is collected and preprocessed to remove inconsistencies and prepare features for model training. Feature engineering techniques are applied to extract useful information such as month, day, and year from transaction dates. The dataset is divided into training and testing sets for model evaluation. Multiple regression algorithms including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting are trained and compared. Performance metrics such as MAE, RMSE, and R² Score are used for evaluation. The best-performing model is selected and deployed using Streamlit to provide an interactive prediction interface.
```


## Implementation
```
Programming Language
1.Python
2.Libraries and Frameworks
3.Pandas
4.NumPy
5.Scikit-learn
6.Pickle
7.Streamlit
8.Matplotlib
9.Seaborn

Tools Used
1.Google Colab
2.Jupyter Notebook
3.GitHub
4.Streamlit Cloud

Project Workflow
1.Data Collection
2.Data Cleaning and Preprocessing
3.Exploratory Data Analysis (EDA)
4.Feature Engineering
5.Train-Test Split
6.Model Training
7.Model Evaluation
8.Model Comparison
9.Model Selection
10.Streamlit Deployment
```

## Results and Discussion
```
Four Machine Learning models were evaluated and compared.
The Linear Regression model achieved the highest R² score of approximately 87.12%, indicating strong predictive performance. The model successfully captured relationships between ATM operational factors and future cash demand.

The deployed Streamlit application enables users to provide ATM-related inputs and instantly receive cash demand predictions. The project demonstrates the practical application of Machine Learning in banking operations and resource optimization.

```

## Limitation
```
1.The model depends on historical data quality and availability.
2.Some operational inputs such as withdrawals and deposits are manually entered in the current prototype.
3.Unexpected events and abnormal customer behavior may affect prediction accuracy.
4.The project uses simulated data and is not directly connected to a real banking database.
5.Real-world deployment would require integration with banking infrastructure and security protocols.
```

## Future Scope
```
1.Integrate the model directly with ATM transaction databases.
2.Automate data collection and prediction processes.
3.Develop a real-time ATM monitoring dashboard.
4.Predict refill requirements automatically for multiple ATMs.
5.Incorporate Deep Learning and Time-Series forecasting models.
6.Implement alert systems for low cash availability.
7.Extend the system to predict the number of days before an ATM runs out of cash.
8.Deploy the solution as a cloud-based banking analytics platform.

Example Future Workflow:

ATM Database → Automatic Data Collection → ML Model → Prediction Engine → Refill Recommendation Dashboard

This would eliminate manual data entry and provide fully automated cash management support.
```
## Conculusion  
```
This project successfully demonstrates the application of Machine Learning in ATM cash demand forecasting. By utilizing historical transaction data and operational factors, the developed model can estimate future cash requirements with good accuracy. Linear Regression emerged as the best-performing model with an R² score of approximately 87%. The Streamlit deployment provides an accessible interface for prediction and showcases the complete Machine Learning pipeline from data preprocessing to deployment. In the future, the project can be enhanced through database integration and real-time automation, making it a valuable solution for intelligent ATM cash management.
```
## References
```
[1] Géron, A. "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow." O'Reilly Media, 2022.
[2] Hastie, T., Tibshirani, R., and Friedman, J. "The Elements of Statistical Learning." Springer, 2017.
[3] Scikit-learn Documentation: https://scikit-learn.org
[4] Streamlit Documentation: https://streamlit.io
[5] Pandas Documentation: https://pandas.pydata.org
[6] NumPy Documentation: https://numpy.org
```
