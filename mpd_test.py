from mpd import MPDClient



def formatDuration(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

client = MPDClient()
client.connect("localhost", 6600)
#print(client.mpd_version)
#print(client.find("any","Rammstein"))

#for song in client.find("any","Rammstein"):
    #print(song)
#    client.add(song['file'])

#print(client.status())
#print(client.playlist())
#print(client.playlistinfo())
#client.save("test_playlist")



for artist in client.list("Artist", "Genre", "Audiobook"):
    print(artist)
    for album in client.list("Album", "Artist", artist):

        album_sum = 0;
        for track in client.find("album", album):
            #print("\t" +"\t" + str(track))
            album_sum = album_sum + int(track['time'])

        #print("\t" + formatDuration(album_sum))
        print("\t" + album + " " + formatDuration(album_sum))


print(client.status())

client.close()
client.disconnect()


