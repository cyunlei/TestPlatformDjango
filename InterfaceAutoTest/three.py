import tensorflow as tf
# from tensorflow.python.preprocessing.image import load_img

img_path = './data/original/12.jpg'
img = tf.keras.preprocessing.image.load_img(img_path)
print(img.size)
print(img.format)
print(img.mode)