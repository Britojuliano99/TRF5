import re
# filtrar mensagens de warning
import warnings
from dataclasses import dataclass

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import pdftotext
import seaborn as sns
from pandas.core.common import random_state
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score, roc_curve)
from sklearn.model_selection import (KFold, StratifiedKFold, cross_val_score,
                                     train_test_split)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import label_binarize
from sklearn.svm import SVC

warnings.filterwarnings('ignore')


