class AudioCollection:

    def get_artist_for_genre(self, genre):
        pass

    def get_album_for_artist(self, artist):
        pass

    def get_first_track_of_album(self, album):
        pass

    """
        Returns a pygame image or None
    """
    def get_album_coverart(self, album, size):
        pass



class AudioControll:

    def start(self):
        raise Exception("Not implemented")

    def stop(self):
        raise Exception("Not implemented")

    def clear_list_and_load_album(self, album):
        raise Exception("Not implemented")

    def play_pause(self):
        raise Exception("Not implemented")

    def next(self):
        raise Exception("Not implemented")

    def prev(self):
        raise Exception("Not implemented")

    def playback_status(self):
        raise Exception("Not implemented")

    def currentsong(self):
        raise Exception("Not implemented")