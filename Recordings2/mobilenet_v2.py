import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
train_it = datagen.flow_from_directory('ground_truth', class_mode='binary', batch_size=16, target_size=(224, 224))

model2 = tf.keras.applications.MobileNetV2(
    input_shape=None,
    alpha=1.0,
    include_top=True,
    weights=None,
    input_tensor=None,
    pooling=None,
    classes=1,
    classifier_activation="sigmoid",
)
model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model2.fit(train_it, epochs=10, steps_per_epoch=1_000)
