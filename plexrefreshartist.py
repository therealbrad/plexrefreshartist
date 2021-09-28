import os, getopt, sys
argumentList = sys.argv[1:]
options = "hf::a::s:t:"
long_options = ["Help", "Artist"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print ("Refreshes Plex Music Artist Metadata.")
            print ("-a    Artists to refresh (partial match) (optional)")
            print ("-f    Parent folder of Artists (optional)")
            print ("-s    Plex Server Base URL with protocol & port")
            print ("-t    Plex Auth Token")
            print ("Either use -a OR -f to provide a list of Artists to refresh.")
            print ("\nIf neither -f or -a are supplied, all Artists will be refreshed!")
            exit

        elif currentArgument in ("-a", "--Artist"):
            AUDIO_ARTIST = currentValue

        elif currentArgument in ("-f", "--Folder"):
            ARTIST_FOLDER = currentValue

        elif currentArgument in ("-s", "--Server"):
            PLEX_SERVER = currentValue

        elif currentArgument in ("-t", "--Plex Auth Token"):
            PLEX_TOKEN = currentValue

except getopt.error as err:
    print (str(err))

from plexapi.server import PlexServer
plex = PlexServer(PLEX_SERVER, PLEX_TOKEN)
AUDIO_SECTION = 'Music'

music = plex.library.section(AUDIO_SECTION)
artists = []

if 'AUDIO_ARTIST' in locals():
    artists.append(AUDIO_ARTIST)

if 'ARTIST_FOLDER' in locals():
    for artist in os.scandir(ARTIST_FOLDER):
        if artist.is_dir():
            artists.append(artist.name)

for each_artist in artists:
    for artist in music.search(each_artist):
        print('Refreshing: %s' % (artist.title))
        try:
            result = artist.refresh()
        except:
            print("WARN: Refresh taking too long. Moving onto the next Artist.")

