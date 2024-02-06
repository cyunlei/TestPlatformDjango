import tensorflow as tf

tf.compat.v1.disable_eager_execution()
# 定义文件模型路径
model_file = './data/mode.h5'
# model_file=''
keras = tf.keras
# 定义模型
def build_model(input_shape):
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same', input_shape=input_shape))
    model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same'))
    model.add(keras.layers.UpSampling2D(size=(2, 2)))
    model.add(keras.layers.Conv2D(16, kernel_size=3, activation='relu', padding='same'))
    model.add(keras.layers.UpSampling2D(size=(2, 2)))
    model.add(keras.layers.Conv2D(3, kernel_size=3, activation='relu', padding='same'))
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss='mse')
    return model


# 定义数据生成器
def data_generator(data_dir, batch_size):
    data_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
                                                                  rotation_range=20, width_shift_range=0.1,
                                                                  height_shift_range=0.1, horizontal_flip=True)

    train_flow = data_generator.flow_from_directory(
        data_dir,
        batch_size=batch_size,
        class_mode='categorical',
        target_size=(599, 680),
        classes=['mosaic', 'original'],
        subset='training',
        shuffle=False
    )
    valid_flow = data_generator.flow_from_directory(
        data_dir,
        batch_size=batch_size,
        class_mode='categorical',
        target_size=(599, 680),
        classes=['mosaic', 'original'],
        subset='validation',
        shuffle=False
    )
    return train_flow, valid_flow


# 训练模型
def train_model(data_dir, batch_size, epochs):
    # 获取数据生成器
    train_flow, valid_flow = data_generator(data_dir, batch_size)
    # 获取模型
    model = build_model(input_shape=(599, 680, 3))
    # 定义早期停止和模型保存回调函数
    early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, mode='auto', verbose=1,
                                                   restore_best_weights=True)

    model_check_point = keras.callbacks.ModelCheckpoint(model_file, monitor='val_loss', save_best_only=True, verbose=1)

    # 训练模型
    steps_per_epoch = train_flow.n // batch_size

    validation_steps = valid_flow.n // batch_size
    print('222222222222')
    history = model.fit(train_flow, steps_per_epoch=steps_per_epoch, epochs=epochs, validation_data=valid_flow,
                        validation_steps=validation_steps, callbacks=[early_stopping, model_check_point])
    print('22222222222211111111')
    return model, history


# 加载模型
def load_model():
    return tf.keras.models.load_model(model_file)


# 使用模型进行去除马赛克
def remove_mosaic(model, image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(599, 680))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image / 255.0
    image = tf.expand_dims(image, axis=0)
    result = model.predict(image)
    result = tf.keras.preprocessing.image.array_to_img(result[0])
    result.save(image_path)


# 训练模型
train_model('data', 128, 50)
# 加载模型并测试
model = load_model()
remove_mosaic(model, './data/original/12.jpg')
