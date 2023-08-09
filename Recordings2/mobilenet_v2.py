import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import os

# datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
# train_it = datagen.flow_from_directory('ground_truth', class_mode='binary', batch_size=16, target_size=(224, 224))
# size = 320
# datagen = ImageDataGenerator(rescale=1.0 / 255.0,)
# print(os.listdir('./dataset/'))
# train_it = datagen.flow_from_directory('./dataset/train', class_mode='binary', batch_size=16, target_size=(size, size),)
# valid_it = datagen.flow_from_directory('./dataset/test', class_mode='binary', batch_size=16, target_size=(size, size),)

datagen = ImageDataGenerator(rescale=1.0 / 255.0,
                             rotation_range=20, shear_range=0.1,
                             zoom_range=0.2, channel_shift_range=0.1, vertical_flip=True, width_shift_range=0.1,
                             height_shift_range=0.1,
                             validation_split=0.1
                             )
target_size = 224
# train_it = datagen.flow_from_directory('./dataset/train', class_mode='binary', batch_size=4,
#                                        target_size=(target_size, target_size), )
# valid_it = datagen.flow_from_directory('./dataset/test', class_mode='binary', batch_size=4,
#                                        target_size=(target_size, target_size), )

train_it = datagen.flow_from_directory('ground_truth_small/train', class_mode='binary', batch_size=4, target_size=(target_size, target_size), subset='training')
valid_it = datagen.flow_from_directory('ground_truth_small/train', class_mode='binary', batch_size=4, target_size=(target_size, target_size), subset='validation')
test_it = datagen.flow_from_directory('ground_truth_small/test', class_mode='binary', batch_size=4, target_size=(target_size, target_size))


model = tf.keras.applications.MobileNetV2(
    input_shape=(target_size, target_size, 3),
    alpha=.6,
    include_top=True,
    weights=None,
    input_tensor=None,
    pooling=True,
    classes=1,
    classifier_activation="sigmoid",
)

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])

print(model.summary())
# model.fit(train_it, validation_data=valid_it, epochs=40)
model.evaluate(test_it)
model.save('models/clasiffication_mobilenetv2_224.h5')
