# started by following this tutorial:
# https://medium.com/analytics-vidhya/how-to-scrape-song-lyrics-a-gentle-python-tutorial-5b1d4ab351d2
# eventually had to start doing my own thing since the genius html updated

import re  # Search and manipulate strings
from lyricsgenius import Genius  # thanks Janekx @ https://stackoverflow.com/a/68027362
import json
import random
from config import *

genius = Genius(genius_api_key)
genius.response_format = 'plain'

def get_lyrics():
    artist = genius.search_artist('Yuno Miles')
    artist.save_lyrics()

def random_song_bar(data):
    song = random.choice(data['songs'])
    year = song["release_date_components"]["year"]
    title = song['title']
    lyrics = song['lyrics']
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    lyrics = lyrics.split("\n")
    lyrics.pop(0)
    lyrics[-1] = lyrics[-1].replace('Embed', '')
    while "" in lyrics:
        lyrics.remove("")
    lyrics[-1] = lyrics[-1].replace('You might also like1', '')
    while "" in lyrics:
        lyrics.remove("")
    lyrics[-1] = lyrics[-1].replace('You might also like', '')
    while "" in lyrics:
        lyrics.remove("")

    bar = random.choice(lyrics)

    return bar, title, year


def chosen_song_bar(data, user_input):
    for song in data['songs']:
        if song['title'].lower() == user_input.lower():
            song = song
            break
    title = song['title']
    year = song["release_date_components"]["year"]
    lyrics = song['lyrics']
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    lyrics = lyrics.split("\n")
    lyrics.pop(0)
    lyrics[-1] = lyrics[-1].replace('Embed', '')
    while "" in lyrics:
        lyrics.remove("")
    lyrics[-1] = lyrics[-1].replace('You might also like1', '')
    while "" in lyrics:
        lyrics.remove("")
    lyrics[-1] = lyrics[-1].replace('You might also like', '')
    while "" in lyrics:
        lyrics.remove("")

    bar = random.choice(lyrics)

    return bar, title, year


if __name__ == '__main__':
    f = open('Lyrics_YunoMiles.json')
    data = json.load(f)

    while True:
        user_input = input("Type 'r' for a random bar from a random song.\n"
                           "Type 'c' for a random bar from a specific song.\n"
                           "Type 'q' to quit.\n")
        print()
        while user_input.lower() != 'q':
            # if user_input.lower() == 'g':
            #     get_lyrics()
            #     user_input = 'q'
            if user_input.lower() == 'r':
                bar, title, year = random_song_bar(data)
                print(bar)
                print(title)
                print()
            if user_input.lower() == 'c':
                user_input = input("Please choose a song.\n")
                print()
                bar, title, year = chosen_song_bar(data, user_input)
                print(bar)
                print(title)
                print()
            break

        if user_input == 'q': break

    f.close()
