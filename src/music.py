from numpy import ndarray
import tomita.legacy.pysynth_s as pss # a, b, e, and s variants available

class Music():
    def __init__(self, image_data : ndarray):
        self.image_data = image_data
        self.song = []

    def generateSongTuple(self):
        """loop through the columns of the image."""
        for column_index in range(self.image_data.shape[0]):
            column_vector = self.image_data[column_index, :, :]
            for pixel in column_vector:
                note = self.pixel2Note(pixel[0])
                duration = 2
                self.song.append((note, duration))
    
    def generateMusic(self):
        assert(len(self.song) > 0)
        pss.make_wav(self.song, fn='saved\out.wav')

    def pixel2Note(self, pixel_value):
        note_dict = {
            1: 'a',
            2: 'b',
            3: 'c',
            4: 'd',
            5: 'e',
            6: 'f',
            7: 'g',
        }
        return note_dict[(pixel_value // 36.57) + 1]