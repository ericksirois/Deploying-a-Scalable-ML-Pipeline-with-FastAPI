# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
* **Developer:** Erick Sirois
* **Model Date:** March 2026
* **Model Version:** 1.0
* **Model Type:** Random Forest Classifier (using scikit-learn).
* **Description:** This model is a learning method for classification. It was trained to predict whether an someone's income is over $50K/yr based on demographic and employment data.

## Intended Use
* **Primary Use Case:** The model is intended for educational purposes as part of the Udacity/WGU Nanodegree. It demonstrates the deployment of a scalable machine learning pipeline with FastAPI.
* **Primary Users:** Reviewers at Udacity.
* **Out-of-Scope Use Cases:** This model should not be used in real-world situations as it is for educational purposes only and uses 30+ year old data.

## Training Data
* **Source:** The dataset used is the "Census Income" dataset from the UC Irvine Machine Learning Repository. The data was extracted by Barry Becker from the 1994 Census database.
* **Features:** The dataset contains 14 features such as workclass, education, marital-status, occupation, relationship, race, sex, and native-country. 
* **Split:** The data was split using an 80/20 train-test split. A fixed random state of 42 was used to make it easily reproducible. 

## Evaluation Data
* **Source:** The evaluation data is the 20% hold-out test set from the original Census dataset described above. 
* **Preprocessing:** Categorical features were processed using a OneHotEncoder, and the target label ("salary" / "income") was transformed using a LabelBinarizer. The test set was processed using the same encoders trained on the training set.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
* The model was evaluated using Precision, Recall, and F1 scores. The model's performance on the test set is as follows:
    * **Precision:** 0.7391
    * **Recall:** 0.6384
    * **F1 Score:** 0.6851
* **Slice Performance:** Performance metrics were also calculated across distinct values of categorical features to ensure fairness and identify potential biases. These results are saved in the `slice_output.txt` file.

## Ethical Considerations
* This dataset contains sensitive personal attributes, such as race, sex, and national origin. Because the data is from 1994, it contains the biases of that time. Because of this, the model may perform differently across various demographic slices.

## Caveats and Recommendations
* The data is over 30 years old- it comes from 1994. Income distribution and society demographics have changed significantly since then. It would be wise to retrain the model on modern data if it were ever to be used for current applications.
