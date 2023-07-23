import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import os

# datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
# train_it = datagen.flow_from_directory('ground_truth', class_mode='binary', batch_size=16, target_size=(224, 224))
size = 320
datagen = ImageDataGenerator(rescale=1.0 / 255.0,
                             # rotation_range=20, shear_range=0.1,
                             # zoom_range=0.2, channel_shift_range=0.1, vertical_flip=True, width_shift_range=0.1,
                             # height_shift_range=0.1,
                             # validation_split=0.2
                             )
# datagen_val = ImageDataGenerator(rescale=1.0 / 255.0)
# train_it = datagen.flow_from_directory('ground_truth_small', class_mode='binary', batch_size=16, target_size=(640, 640), subset='training')
# valid_it = datagen.flow_from_directory('ground_truth_small', class_mode='binary', batch_size=16, target_size=(640, 640), subset='validation')
print(os.listdir('./dataset/'))
train_it = datagen.flow_from_directory('./dataset/train', class_mode='binary', batch_size=16, target_size=(size, size),
                                       )
valid_it = datagen.flow_from_directory('./dataset/test', class_mode='binary', batch_size=16, target_size=(size, size),
                                       )
# valid_it = datagen_val.flow_from_directory('./ground_truth_small/test', class_mode='binary', batch_size=16,
#                                            target_size=(size, size))

model = tf.keras.applications.MobileNetV2(
    input_shape=(size, size, 3),
    alpha=.6,
    include_top=True,
    weights=None,
    input_tensor=None,
    pooling=True,
    classes=1,
    classifier_activation="sigmoid",
)
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])

# model.fit(train_it,, epochs=10)
model.fit(train_it, validation_data=valid_it, epochs=10)

model.save('models/clasiffication_mobilenetv2_320.h5')
