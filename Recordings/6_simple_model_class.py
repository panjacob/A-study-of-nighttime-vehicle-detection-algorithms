from keras import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.client import device_lib

datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
train_it = datagen.flow_from_directory('ground_truth', class_mode='binary', batch_size=16, target_size=(320, 320))

print(device_lib.list_local_devices())

model = Sequential()
model.add(Conv2D(32, (5, 5), activation='relu', input_shape=(320, 320, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_it, epochs=10)
model.save('simple_model')
# 3635/3635 [==============================] - 213s 59ms/step - loss: 0.5463 - accuracy: 0.6193
