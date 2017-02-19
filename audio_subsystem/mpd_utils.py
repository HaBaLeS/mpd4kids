from audio_subsystem import AudioCollection
from audio_subsystem import AudioControll
from mpd import  MPDClient
from mpd import ConnectionError
from mutagen import File
from constants import *
import pygame

"""
TODO Learn how to decorate connect and sisconnect to every call!
"""

class MPDAudioSubsystem(AudioCollection, AudioControll):

    def __init__(self):
        self.client = MPDClient()

    def connect(self):
        try:
            self.client.connect("localhost", 6600)
        except ConnectionError:
            pass
        except ConnectionRefusedError:
            import sys
            print("mpd not Running? Could not connect to client: ConnectionRefusedError")
            sys.exit(1)
        except ConnectionResetError:
            import sys
            print("mpd not Running? Could not connect to client: ConnectionRefusedError")
            sys.exit(1)

    def get_artist_for_genre(self, genre):
        self.connect()
        if(genre):
            return self.client.list("Artist", "Genre", "Audiobook")
        return self.client.list("Artist")

    def get_album_for_artist(self, artist):
        self.connect()
        return self.client.list("Album", "Artist", artist)


    def get_first_track_of_album(self, album):
        self.connect()
        return self.client.find("album", album)[0]

    def get_album_coverart(self, album, size = (200,200)):
        self.connect()
        track = self.get_first_track_of_album(album);
        file = File(CONFIG_mpd_library_path + track['file'])  # mutagen can automatically detect format and type of tags

        if "APIC:" in file.tags.keys():
            artwork = file.tags['APIC:'].data  # access APIC frame and grab the image
            with open('tmp_album_cover.jpg', 'wb') as img:
                img.write(artwork)  # write artwork to new image
            album_cover = pygame.image.load("tmp_album_cover.jpg")
            foo = pygame.transform.scale(album_cover, size)
            return foo

        return None

    def start(self):
        self.connect()
        self.client.play()

    def stop(self):
        self.connect()
        self.client.stop()

    def play_pause(self):
        self.connect()
        status = self.client.status()
        if status['state'] == 'play':
            self.client.pause(1)
        else:
            self.client.pause(0)

    def next(self):
        self.connect()
        self.client.next()

    def prev(self):
        self.connect()
        self.client.previous()

    def clear_list_and_load_album(self, album):
        self.connect()
        self.client.clear()
        self.client.findadd("Album", album )

    def currentsong(self):
        self.connect()
        return self.client.currentsong()

    def playback_status(self):
        self.connect()
        return self.client.status()

