import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

##########################################
#Part 1: Load data into Python
#
#The first line uses internal tensorflow function to load the MNIST database.
#If another dataset is prefered, one just needs to create numpy arrays for data and labels
##########################################
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Shapes of training and test datasets are", x_train.shape, x_test.shape)
print("Shapes of training and test labels are",   y_train.shape, y_test.shape)

# Plot some examples
N_PLOT = 5
fig, ax = plt.subplots(ncols=N_PLOT, figsize=(4*N_PLOT, 4))
for i in range(N_PLOT):
    ax[i].imshow(x_train[i])         # Plot handwritten digit as an image
    ax[i].set_title(str(y_train[i])) # Use label as image title
plt.show()

############################################
# Part 2: Construct model
#
# Define layered structure
#   - First layer converts images into 1D arrays, because inputs to a network have to be 1D, not 2D like images
#   - The other 3 layers are used to actually predict the output
############################################
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Train and evaluate model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Final test accuracy is", test_accuracy)

############################################
# Part 3: Plot some examples
############################################
N_EXAMPLE = 5
pred = model.predict(x_test[:N_EXAMPLE])
pred_conf = np.max(pred,axis=1)
pred_ans  = np.argmax(pred,axis=1)   #

fig, ax = plt.subplots(ncols=N_PLOT, figsize=(4*N_PLOT, 4))
for i in range(N_PLOT):
    ax[i].imshow(x_test[i])
    ax[i].set_title("True="+str(y_test[i])+", pred="+str(pred_ans[i])+", conf="+str(pred_conf[i]))
plt.show()