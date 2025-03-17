# Source: https://github.com/mwaskom/seaborn-data/blob/master/mpg.csv
import seaborn as sns
import torch
import numpy as np
import pandas as pd

dataset = sns.load_dataset("mpg")
relevant_dataset = dataset[["mpg", "weight", "horsepower"]]
cleaned_relevant_dataset = relevant_dataset.dropna()
cleaned_mpg = cleaned_relevant_dataset["mpg"]
cleaned_weight = cleaned_relevant_dataset["weight"]
cleaned_horsepower = cleaned_relevant_dataset["horsepower"]

weight_tensor = torch.tensor(cleaned_weight.values)
horsepower_tensor = torch.tensor(cleaned_horsepower.values)
x_double = torch.stack((weight_tensor, horsepower_tensor), dim=-1)
y_double = torch.tensor(cleaned_mpg.values).unsqueeze(1)

x = x_double.to(torch.float32)
y = y_double.to(torch.float32)

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy()