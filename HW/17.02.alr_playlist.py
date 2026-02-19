import random

class Playlist:
    def __init__(self):
        self.songs = []
        self.index = 0
    
    def add_song(self, title, artist):
        self.songs.append([title, artist])
    
    def remove_song(self, title):
        for i in range(len(self.songs)):
            if self.songs[i][0] == title:
                self.songs.pop(i)
                break
    
    def shuffle(self):
        random.shuffle(self.songs)
        self.index = 0
    
    def next(self):
        self.index = (self.index + 1) % len(self.songs)
    
    def previous(self):
        self.index = (self.index - 1) % len(self.songs)
    
    def current_song(self):
        return self.songs[self.index][0]
    
    def current_artist(self):
        return self.songs[self.index][1]
    
playlist = Playlist()
playlist.add_song("Bohemian Rhapsody", "Queen")
playlist.add_song("Imagine", "John Lennon")
playlist.add_song("Shape of You", "Ed Sheeran")

print(playlist.current_song())
print(playlist.current_artist())

playlist.next()
print(playlist.current_song())

playlist.previous()
print(playlist.current_song())

playlist.remove_song("Imagine")
playlist.next()
print(playlist.current_song())