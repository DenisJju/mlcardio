import torch
import joblib
import os
import numpy as np
from .dqn_model import DQN

# Define the exact paths
MODEL_PATH = r"C:\Users\USER\Desktop\django\predictor\ml_model\dqn_cardiac_model.pth"
SCALER_PATH = r"C:\Users\USER\Desktop\django\predictor\ml_model\scaler.pkl"

# Load scaler
scaler = joblib.load(SCALER_PATH)

# Load model
input_dim = 19  # Make sure this matches the number of features
output_dim = 3  # Number of actions
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = DQN(input_dim=input_dim, output_dim=output_dim).to(device)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()

def predict_action(input_data):
    """
    input_data: a list or numpy array with 19 elements
    """
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    input_tensor = torch.FloatTensor(input_scaled).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        action = torch.argmax(output).item()

    return action
