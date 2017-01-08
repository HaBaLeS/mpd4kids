from audio_subsystem import AudioCollection
from audio_subsystem import AudioControll
from mpd import  MPDClient
from mutagen import File
from constants import *
import pygame


class MPDAudioSubsystem(AudioCollection, AudioControll):

    def __init__(self):
        self.client = MPDClient()
        self.client.connect("localhost", 6600)


    def get_artist_for_genre(self, genre):
        if(genre):
            return self.client.list("Artist", "Genre", "Audiobook")
        return self.client.list("Artist")

    def get_album_for_artist(self, artist):
        print("List albums for Artist: " + artist)
        return self.client.list("Album", "Artist", artist)

    def get_first_track_of_album(self, album):
        return self.client.find("album", album)[0]

    def get_album_coverart(self, album):
        track = self.get_first_track_of_album(album);
        file = File(CONFIG_mpd_library_path + track['file'])  # mutagen can automatically detect format and type of tags

        if "APIC:" in file.tags.keys():
            artwork = file.tags['APIC:'].data  # access APIC frame and grab the image
            with open('tmp_album_cover.jpg', 'wb') as img:
                img.write(artwork)  # write artwork to new image
            album_cover = pygame.image.load("tmp_album_cover.jpg")
            foo = pygame.transform.scale(album_cover, (200, 200))
            return foo

        return None