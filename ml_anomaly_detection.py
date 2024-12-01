import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

def build_autoencoder(input_dim):
    model = Sequential([
        Dense(32, activation="relu", input_dim=input_dim),
        Dense(16, activation="relu"),
        Dense(8, activation="relu"),
        Dense(16, activation="relu"),
        Dense(32, activation="relu"),
        Dense(input_dim, activation="linear")
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

def train_autoencoder(data):
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    X_train, X_test = train_test_split(data_scaled, test_size=0.2, random_state=42)
    
    model = build_autoencoder(X_train.shape[1])
    model.fit(X_train, X_train, epochs=20, batch_size=32, validation_data=(X_test, X_test))
    
    reconstruction_error = model.evaluate(X_test, X_test, verbose=0)
    print(f"Reconstruction Error: {reconstruction_error}")
    return model, scaler

if __name__ == "__main__":
    csv_file = "csv_files/preprocessed_packets.csv"
    data = load_data(csv_file)
    numeric_data = data[["protocol", "length"]]
    
    model, scaler = train_autoencoder(numeric_data)
