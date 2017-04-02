from audio_subsystem import AudioCollection
from audio_subsystem import AudioControll
from mpd import  MPDClient
from mpd import ConnectionError
from mutagen import File
from constants import *
import pygame

"""
TODO Learn how to decorate connect and disconnect to every call!
"""

class MPDAudioSubsystem(AudioCollection, AudioControll):

    def __init__(self):
        self.client = MPDClient()
        self.client.timeout = 10

    def connect(self):
        try:
            self.client.connect("localhost", 6600)
            print("Reconnect success")
        except ConnectionError:
            print("already connected")
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
            val= self.client.list("Artist", "Genre", "Audiobook")
        else:
            val = self.client.list("Artist")
        self.client.disconnect()
        return val

    def get_album_for_artist(self, artist):
        self.connect()
        val = self.client.list("Album", "Artist", artist)
        self.client.disconnect()
        return val


    def get_first_track_of_album(self, album):
        self.connect()
        val =  self.client.find("album", album)[0]
        self.client.disconnect()
        return val

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
            self.client.disconnect()
            return foo

        self.client.disconnect()
        return None

    def start(self):
        self.connect()
        self.client.play()
        self.client.disconnect()

    def stop(self):
        self.connect()
        self.client.stop()
        self.client.disconnect()

    def play_pause(self):
        self.connect()
        status = self.client.status()
        if status['state'] == 'play':
            self.client.pause(1)
        else:
            self.client.pause(0)

        self.client.disconnect()

    def next(self):
        self.connect()
        self.client.next()
        self.client.disconnect()

    def prev(self):
        self.connect()
        self.client.previous()
        self.client.disconnect()

    def clear_list_and_load_album(self, album):
        self.connect()
        self.client.clear()
        self.client.findadd("Album", album )
        self.client.disconnect()

    def currentsong(self):
        self.connect()
        val = self.client.currentsong()
        self.client.disconnect()
        return val

    def playback_status(self):
        self.connect()
        val = self.client.status()
        self.client.disconnect()
        return val

