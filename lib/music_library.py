
class MusicLibrary():
    def __init__(self):
        self.tracks = set()
    def add_track(self, track):
        self.tracks.add(track)
        
    def list_tracks(self):
        output = ""
        for t in self.tracks:
            output+=t + "\n"
        return output[:-1]
               
