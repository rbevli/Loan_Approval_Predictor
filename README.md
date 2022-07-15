# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
- Automate Loan Eligibility Process based on customer details using classification models done via Pipelines
- Details: Gender, Marital Status, Education, Number of Dependents, Household Income, Loan Amount Requested, Credit History guidelines along with factors such as Property type etc.
- Loan Approval and judging these categories is often a cumbersome process, by this model we aim to automate and make the loan approval predictions easier


## Hypothesis
Explore and visualize certain possible contributing factors such as :
- Effect of Credit History on Loan Approval
    This can be a contributing factor as a person's credit history is always looked at to determine loan eligibility
- Income Level and Education Level on Loan Approval
    
- Property type and Location on Loan Approval

The aforementioned hypothesis will be looked at through data visualisation techniques along with
their affect on the final predicted value. The effect of these features will be looked at along with their contribution to the classification model.



## EDA 
During the EDA phase, many key findings were found that could be major contributing factors to the performance of the classification model. Credi History, Higher Loan Amount term, Higher Applicant and Coapplicant Income, Higher Loan Amount are factors that positively contribute to the Loan Application getting approved.

## Process
### Step 1: EDA

### Step 2: Categorical Variable Analysis
Pivot tables created to better understand the Categorical Variables and there relationship between each other.

### Step 3: Data Cleaning
Missing values imputed using fillna() with relevant sklearn metrics.

### Step 4: Log Transformation
Extreme values of Loan Amount and Income (Applicant and Coapplicant Income) were combatted by applying a Log Transformation. Applicant and Coapplicant Incomes were combined.

### Step 5: Label Transformation and Preprocessing
Nominal Features were Label Encoded Manually, Pipelines created with log transform functions, scaling using StandardScaler()

### Step 6: Modeling and Pipeline creation
XGB Classifier and Random Forest Classifier Pipelines created along with Column Transformations.
Cross Validation and Hyperparameter tuning performed using GridSearchCV.

## Results/Demo
Random Forest Classification and XGBoost Classification

Base Model (RFC)
	Accuracy – 0.62

Random Forest Classification after Parameter tuning
	Accuracy - 0.74

XGBoost Classification after Parameter tuning
	Accuracy - 0.74


## Challanges 
Featuring engineering was somewhat of an issue in terms of making sure the features were meaningful enough. Furthermore, Pipeline creation was also a slight challenge as after deploying certain functions such as log transform were not available in the pickled model file and had to be manually included in the Flask App.

## Future Goals
For future goals and recommendations, test the dataset with more models such as SVC. Furthermore, new features such as raw credit score, job contract length and wealth can be introduced as these indicators can contribute to the loan approval prediction as well.
