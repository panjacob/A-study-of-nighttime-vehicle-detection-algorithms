from keras.preprocessing.image import ImageDataGenerator
from keras.applications import MobileNetV3Small

datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
train_it = datagen.flow_from_directory('ground_truth', class_mode='binary', batch_size=16, target_size=(224, 224))

model2 = MobileNetV3Small(
    input_shape=(224, 224, 3),
    alpha=1.0,
    minimalistic=False,
    include_top=True,
    weights=None,
    input_tensor=None,
    classes=1,
    pooling=None,
    dropout_rate=0.2,
    classifier_activation="sigmoid",
    include_preprocessing=True,
)
model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model2.fit(train_it, epochs=10)
# 138s 38ms/step - loss: 0.5545 - accuracy: 0.6163
