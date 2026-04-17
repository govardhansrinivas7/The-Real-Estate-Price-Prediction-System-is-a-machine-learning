# Real Estate Price Prediction Project

This project predicts house prices in Bengaluru based on parameters like square footage, location, BHK, and number of bathrooms.

## Prerequisites

- Python 3.8+
- Node.js & npm

## Setup Instructions

### 1. Backend Setup

1. Open a terminal in the project root.
2. Install Python dependencies:
   ```bash
   pip install flask flask-cors pandas scikit-learn numpy
   ```
3. Train the model (this will generate the `.pkl` and `.json` files in the `model/` folder):
   ```bash
   python train_model.py
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
   The backend will run on `http://127.0.0.1:5000`.

### 2. Frontend Setup

1. Open a new terminal in the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The frontend will typically run on `http://localhost:5173`.

## How to Use

1. Ensure both the backend (Flask) and frontend (Vite) servers are running.
2. Open the frontend URL in your browser.
3. Enter the details (Sqft, BHK, Bath, Location).
4. Click "Predict Price" to see the estimated value.
