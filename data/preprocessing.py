import pip

pip.main(['install', 'scikit-learn'])
pip.main(['install', 'pandas'])
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


# Load data
df = pd.read_csv("C:\\Users\\Abhimantr Singh\\Downloads\\codecplus\\predictive-maintenance-system\\data\\raw\\predictive_maintenance.csv")

# Drop ID columns
df = df.drop(columns=["UDI", "Product ID"])

# Encode 'Type' and 'Failure Type'
le_type = LabelEncoder()
le_failure = LabelEncoder()
df["Type"] = le_type.fit_transform(df["Type"])
df["Failure Type"] = le_failure.fit_transform(df["Failure Type"])

# Separate features and label
X = df.drop(columns=["Target"])  # Features
y = df["Target"]                 # Label

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save processed data
processed_df = pd.DataFrame(X_scaled, columns=X.columns)
processed_df["Target"] = y
processed_df.to_csv("processed_data.csv", index=False)