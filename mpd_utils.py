from mpd import  MPDClient

class MpdPlayer():

    def __init__(self):
        self.client = MPDClient()
        self.client.connect("localhost", 6600)


    def getAudioBookArtists(self):
        return self.client.list("Artist", "Genre", "Audiobook")

    def get_album_for_artist(self, artist):
        print("List albums for Artist: " + artist)
        return self.client.list("Album", "Artist", artist)

    def get_first_track_of_album(self, album):
        return self.client.find("album", album)[0]