# import the necessary packages
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization, LayerNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D, MaxPool2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input, InputLayer
from tensorflow.keras.models import Model
from tensorflow import keras


def down_block(x, filters, kernel_size=(3, 3), padding="same", strides=1):
    c = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(x)
    c = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(c)
    p = keras.layers.MaxPool2D((2, 2), (2, 2))(c)
    return c, p


def up_block(x, skip, filters, kernel_size=(3, 3), padding="same", strides=1):
    us = keras.layers.UpSampling2D((2, 2))(x)
    if skip.shape[1] != us.shape[1]:
        us = tf.pad(us, paddings=tf.constant([[0,0],[0,skip.shape[1]-us.shape[1]],[0,0],[0,0]]),mode="SYMMETRIC")
    concat = keras.layers.Concatenate()([us, skip])
    c = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(concat)
    c = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(c)
    return c


def bottleneck(x, filters, kernel_size=(3, 3), padding="same", strides=1):
    c1 = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(x)
    c2 = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(c1)
    return c1, c2


def create_UNet(height, width, depth, filters=(32, 64, 128, 256)):
    inputShape = (height, width, depth)

    chanDim = -1
    # define the model input
    inputs = Input(shape=inputShape)
    
    p0 = inputs
    c1, p1 = down_block(p0, filters[0]) 
    c2, p2 = down_block(p1, filters[1]) 
    c3, p3 = down_block(p2, filters[2]) 
    
    bn1, bn2 = bottleneck(p3, filters[3])
    
    u1 = up_block(bn2, c3, filters[2]) 
    u2 = up_block(u1, c2, filters[1])
    u3 = up_block(u2, c1, filters[0])


    # flatten the volume, then FC => RELU => BN => DROPOUT
    x = Flatten()(bn1)
    x = Dense(256)(x)
    x = Activation("relu")(x)
    x = BatchNormalization(axis=chanDim)(x)
    x = Dropout(0.5)(x)

    # apply another FC layer, this one to match the number of nodes
    # coming out of the MLP
    fc = Dense(128, activation='relu')(x)

    x_vis = Dense(1, activation='sigmoid', name='visibility')(fc)

    x_regress = Dense(63, activation="linear", name='regression')(fc)
    
    x_depth = Conv2D(1, (1, 1), padding="same", name='regression_depth')(u3)
    
    model = Model(inputs=inputs, outputs=[ x_regress, x_vis, x_depth])
    return model
