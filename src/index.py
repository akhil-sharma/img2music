from PIL import Image
from numpy import asarray

def processImage(file_path : str, new_height : str = 500) -> dict:
    """Resize the image while maintaining aspect ratio."""
    loaded_image = Image.open(file_path)
    image_width, image_height =  loaded_image.size
    new_width = int(new_height * (image_width / image_height))

    loaded_image = loaded_image.resize((new_width, new_height), Image.ANTIALIAS)
    return loaded_image

def readColumnsLeftToRight(image_file: dict):
    """loop through the columns of the image."""
    data = asarray(image_file)
    print(type(data))
    print(data.shape)

    for column_index in range(data.shape[1]):
        column_vector = data[:, column_index, :]
        # Do what ever we want with it.
        # column_vector has rbg values. 
        print(column_vector)
        break

if __name__ == '__main__':
    file_path = 'resources\image_two.jpg'
    image_file = processImage(file_path)
    data = readColumnsLeftToRight(image_file)

