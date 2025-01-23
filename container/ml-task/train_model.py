import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generating random data for training
X_train = np.random.rand(1000, 10)  # 1000 samples, 10 features
y_train = np.random.randint(2, size=(1000, 1))  # Binary classification

# Define a simple neural network model
model = Sequential([
    Dense(64, activation='relu', input_dim=10),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Save the trained model
model.save('trained_model.h5')
