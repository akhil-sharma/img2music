from PIL import Image
from numpy import asarray, ndarray
from music import Music

def processImage(file_path : str, new_height : str = 25) -> ndarray:
    """Resize the image while maintaining aspect ratio."""
    loaded_image = Image.open(file_path)
    image_width, image_height =  loaded_image.size
    print(F"Original image dims: {image_height} x {image_width}")
    
    new_width = int(new_height * (image_width / image_height))
    loaded_image = loaded_image.resize((new_width, new_height), Image.ANTIALIAS)
    print(F"Resized image dims: {new_height} x {new_width}")

    return asarray(loaded_image)

def main():
    file_path = 'resources\stars_image.jpg'
    data = processImage(file_path)

    musicObj = Music(data)
    musicObj.generateSongTuple()
    musicObj.generateMusic()

if __name__ == '__main__':
    main()

