from ytmusicapi import YTMusic
import requests
from bs4 import BeautifulSoup

ytmusic = YTMusic('headers_auth.json')

# Create playlist
ytmusicPlaylistID = ytmusic.create_playlist("BBC 6 Music Playlist","The BBC 6 Music playlist")

# Fetch bbc music playlist and put the song names in a list
request = requests.get('https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist')
soup = BeautifulSoup(request.text, 'html.parser')

all_p = soup.find_all('p')
filtered_p = []
for p in all_p:
    if " - " in p.get_text():
        filtered_p.append(p.get_text())

# Search for songs
songs = []

for song in filtered_p:
    result = ytmusic.search(song, "songs")[0]
    if result["title"] in song and result["artists"][0]["name"] in song:
        songs.append(result["videoId"])

# Add songs to youtube music playlist
ytmusic.add_playlist_items(ytmusicPlaylistID, songs)