# -*- coding: utf-8 -*-
"""2c_dziri_bert.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0f-R7Is6cJxuuUR7xP90afD_4yiiRyl
"""

# Commented out IPython magic to ensure Python compatibility.
#!pip install autogluon

import numpy as np
import re
import sys, os, io

import warnings
import autogluon as ag
warnings.filterwarnings("ignore")
np.random.seed(123)
# %matplotlib inline

from autogluon.core import TabularDataset
from autogluon.multimodal import MultiModalPredictor

train_data_2c = TabularDataset("keras_train_pre_2c_trans_.txt")
test_data_2c = TabularDataset("keras_test_pre_2c_trans_.txt")

print(train_data_2c.head(10))


predictor = MultiModalPredictor(label='label')
predictor.fit(train_data_2c,
              hyperparameters={ 'model.hf_text.checkpoint_name': 'alger-ia/dziribert',"optimization.optim_type": "adamw",'optimization.max_epochs': 4})
                  
print("[INFO] Test Metrics are...")


predictor.evaluate(test_data_2c, metrics=["f1_macro", "accuracy","f1_micro"])