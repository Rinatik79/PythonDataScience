import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mode

import warnings
warnings.filterwarnings('ignore')

DATASET_PATH = './creditcard.csv'
df = pd.read_csv(DATASET_PATH, sep=',')

print(df.head(4))
print(df.tail(4))

print(df["Class"].value_counts())

df["Class"].value_counts().plot(kind="bar")
plt.show()

df["Class"].value_counts().plot(kind="bar", logy=True)
plt.show()

true_transactions = df[(df["Class"] == 0)]
fraud_transactions = df[(df["Class"] == 1)]

print("\nV1 min and max for true transaction:")
print(true_transactions["V1"].min())
print(true_transactions["V1"].max())

print("\nV1 min and max for fraud transaction:")
print(fraud_transactions["V1"].min())
print(fraud_transactions["V1"].max())

plt.hist(true_transactions["V1"], bins=20, density=True, color="grey", alpha=.5, label='Class 0')
plt.hist(fraud_transactions["V1"], bins=20, density=True, color="red", alpha=.5, label='Class 1')
plt.xlabel("V1")
plt.legend()
plt.show()
