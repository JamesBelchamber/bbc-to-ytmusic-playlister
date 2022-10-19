# BBC to YouTube Music Playlister

# Setup

```
pip install requests ytmusicapi bs4
```

Then follow the [ytmusicapi setup instructions](https://ytmusicapi.readthedocs.io/en/stable/setup.html) to create the headers_auth.json file necessary to authenticate with YouTube Music.

# Run

```
python bbc-to-ytmusic-playlister.py
```

# Todo

- [ ] Create setup flow
- [ ] Update existing playlists
- [ ] Support all BBC Radio stations
- [ ] Smarter song searching (matching different ways of writing "feat", removing "Radio Edit" etc)