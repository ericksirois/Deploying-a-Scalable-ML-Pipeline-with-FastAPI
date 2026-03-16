import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model, inference

def test_compute_model_metrics():
    """
    Test that the compute_model_metrics function calculates
    and returns three float values: precision, recall, and f1 score.
    """
    # Create fake arrays of known labels and predictions
    y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0])
    
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)


def test_train_model():
    """
    Test that the train_model function trains and 
    returns a RandomForestClassifier object.
    """
    # Create tiny fake training dataset
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    
    model = train_model(X_train, y_train)
    
    # Verify the returned model is a Random Forest
    assert isinstance(model, RandomForestClassifier)


def test_inference():
    """
    Test that the inference function returns a numpy array of predictions
    that matches the length of the input test data.
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    model = train_model(X_train, y_train)
    
    # Create tiny fake testing dataset
    X_test = np.array([[1, 2], [5, 6]])
    preds = inference(model, X_test)
    
    # Verify the predictions are a numpy array and match the length of the test data
    assert isinstance(preds, np.ndarray)
    assert len(preds) == len(X_test)