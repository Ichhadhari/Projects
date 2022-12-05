# Medical Insurance US Charges Prediction

Scrutinized [Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) and analysis important things.In this project I will apply regression techniques of supervised learning to predict the medical insurance charges. According to Data analysis work on model building.

### key attributes that I worked in this project


#### EDA📊📝
Dataset consists of 1338 records. Each record contains the below data for specific person.

- age – Age of the person
- sex – Sex of the person
- bmi – Body Mass Index(BMI) of the person
- children – Number of children for the person
- smoker – Smoking status of the person
- region – Region of the person in US
- charges – Medical Insurance costs per year for the person

From the above data we can observe below

- Input data contains an even distribution of male and female samples
- Majority of them are non-smokers with 1064 samples
- A major sample of input data contains persons with no children with 574.
- The data is evenly distributed across 4 regions with the region of southeast having slightly more samples.

From the above data we can do analusis on below questions:

- Q.1) Avg charges of southwest and northwest people medical insorance
- Q.2) make catagories of age like kid, teenage, adult,old
- Q.3) See male and female avg. as per catagories
- Q.4) See male and female count by catagories
- Q.5) See adult and old age peoples bmi of smokers only
- Q.6) See people whose charges less than 20000 those are doing smoking daily

#### Model Building📱
 #### -Training and Testing
- Splitting the data set into training and testing subsets helps to assess the performance of the model over an independent data set. Typlically, we train the model using training data subset and then evaluate the model's performance using the testing data subset, which is independent of the training data subset.

- Splitting the data set also helps in having a check on model's overfitting.

#### Evaluation⚖️
As part of evaluation, I considered multiple regression algorithms like decision trees, Support Vector Machines for regression, etc. Based on the metrics, I choose to use decision tree technique for this project

The goal of decision tree is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
#### Using Model in backend💻

I use this train model on person website, So anyone can test it.
#### Deployment ☁️

For use this model by anyone, I make it online throug cloud deployment. you can test it in demo section.



## Dataset available on kaggle
[Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

## My model demo available online
[DEMO](https://vaibhav-rokde-portfolio.herokuapp.com/medical-insurance-us-model/)
