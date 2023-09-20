from lib.music_library import *
import pytest

def test_add_track():
    music_lib = MusicLibrary()
    track = "Bohemian Rhapsody"
    music_lib.add_track(track)
    assert music_lib.tracks == {"Bohemian Rhapsody"}
def test_list_tracks():
    music_lib = MusicLibrary()
    music_lib.add_track("Sonata in D")
    music_lib.add_track("Sonata in C")
    assert music_lib.list_tracks() == f"Sonata in D\n" + f"Sonata in C"
