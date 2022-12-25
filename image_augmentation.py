from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


# Create an ImageDataGenerator object
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# Load the input image
image = load_img('non_periodontal_1.png')

# Convert the image to a Numpy array
image = img_to_array(image)

# Reshape the array so that it has a single channel (i.e. grayscale)
image = image.reshape((1, ) + image.shape)

# Generate and save modified versions of the input image
i = 0
for batch in datagen.flow(image, save_to_dir='preview', save_prefix='image', save_format='jpeg'):
    i += 1
    if i > 20:
        break


transform = A.Compose([
    A.RandomCrop(width=256, height=256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])