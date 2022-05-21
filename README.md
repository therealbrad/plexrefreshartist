# plexrefreshartist

plexrefreshartist.py is a Python script to refresh the Metadata for Plex Music Artists.

I started collecting Music Videos for Artists in my Plex Music collection, but found that I had to Refresh Metadata for either the whole library or each Artist to get them to show up. This script does it for me.

## Installation

The script relies on [python-plexapi](https://github.com/pkkid/python-plexapi).

## Usage

### Help Text
```
$ python3 plexrefreshartist.py -h
-a    Artists to refresh (partial match) (optional)
-f    Parent folder of Artists (optional)
-s    Plex Server Base URL with protocol & port
-t    Plex Auth Token

If neither -f or -a are supplied, all Artists will be refreshed!
```
### Refresh a Single Artist
```
$ python3 plexrefreshartist.py -s http://<your_plex_server>:<port> -t <plex_token> -a "Fever Ray"
Refreshing: Fever Ray
```

### Refresh all Artists matching string
```
$ python3 plexrefreshartist.py -s http://<your_plex_server>:<port> -t <plex_token> -a "Mount"
Refreshing: Black Mountain
Refreshing: The Mountain Goats
Refreshing: Mountaineers
Refreshing: Mountains
Refreshing: Purple Mountains

```

### Refresh All Artists with New Videos
Specify your [Global Music Videos Folder](https://support.plex.tv/articles/205568377-adding-local-artist-and-music-videos/) to only refresh Artists with videos added since the last refresh.
```
$ python3 plexrefreshartist.py -s http://<your_plex_server>:<port> -t <plex_token> -f /Media/Library/music_videos/
```

## To Do
- [x] ~~Refresh only updated folders since the last time the script ran~~

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
