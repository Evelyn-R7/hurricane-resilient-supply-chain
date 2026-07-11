"""Risk-model construction, calibration, and probability metrics."""

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def expected_calibration_error(y_true, y_prob, n_bins: int = 10) -> float:
    y_true, y_prob = np.asarray(y_true), np.asarray(y_prob)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    bins = np.minimum(np.digitize(y_prob, edges[1:-1]), n_bins - 1)
    return float(sum(np.mean(bins == i) * abs(y_true[bins == i].mean() - y_prob[bins == i].mean())
                     for i in range(n_bins) if np.any(bins == i)))


def make_preprocessor(numeric_features, categorical_features):
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                            ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    return ColumnTransformer([("numeric", numeric, numeric_features),
                              ("categorical", categorical, categorical_features)])


def make_model_pool(random_state: int = 42):
    """Approved model families; experiment-specific hyperparameters remain in notebooks."""
    return {
        "Logistic Regression": LogisticRegression(max_iter=5000, class_weight="balanced", random_state=random_state),
        "Random Forest": RandomForestClassifier(class_weight="balanced", random_state=random_state, n_jobs=-1),
        "Gradient Boosting": GradientBoostingClassifier(random_state=random_state),
    }
