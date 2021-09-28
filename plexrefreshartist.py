import os, time, getopt, sys, json
argumentList = sys.argv[1:]
options = "hf::a::s:t:"
long_options = ["Help", "Artist"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print ("-a    Artists to refresh (partial match) (optional)")
            print ("-f    Parent folder of Artists (optional)")
            print ("-s    Plex Server Base URL with protocol & port")
            print ("-t    Plex Auth Token")
            print ("\nIf neither -f or -a are supplied, all Artists will be refreshed!")
            sys.exit()

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
CACHE_FILE = "./.cache"
AUDIO_SECTION = 'Music'

music = plex.library.section(AUDIO_SECTION)
artists = {}
cache_artists = {}

if 'AUDIO_ARTIST' in locals():
    artists.append(AUDIO_ARTIST)

if 'ARTIST_FOLDER' in locals():
    # Check if a cache exists from last run
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as json_file:
            cache_artists = json.load(json_file)
    for artist in os.scandir(ARTIST_FOLDER):
        if artist.is_dir():
            lastMod = max(os.path.getmtime(root) for root,_,_ in os.walk(artist.path))
            #print('Found %s %s' % (artist.name,lastMod))
            if cache_artists.get(artist.name):
                if lastMod > cache_artists.get(artist.name):
                    artists[artist.name] = lastMod
                    cache_artists[artist.name] = lastMod
                #else:
                #    print('Skipping %s because %s is not greater than %s' % (artist.name,lastMod,cache_artists[artist.name]))
            else:
                artists[artist.name] = lastMod
                cache_artists[artist.name] = lastMod

for each_artist in artists:
    for artist in music.search(each_artist):
        try:
            print('Refreshing: %s' % (artist.title))
            #result = artist.refresh()
        except:
            print("WARN: Refresh taking too long. Moving onto the next Artist.")
#write out new cache
#print(cache_artists)
with open(CACHE_FILE, 'w') as outfile:
    json.dump(cache_artists, outfile)

