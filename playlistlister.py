import os
import pygame
import tkinter as tk
from tkinter import filedialog

class PlaylistListener:
    # TODO: Add more customisability (idk how it spells)
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Listener")
        self.playlist = []
        self.current_song_index = 0

        self.load_button = tk.Button(self.root, text="Load Playlist", command=self.load_playlist)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(pady=5)

        self.shuffle_button = tk.Button(self.root, text="Shuffle", command=self.shuffle_playlist)
        self.shuffle_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(pady=5)

        self.previous_button = tk.Button(self.root, text="Previous", command=self.previous_song)
        self.previous_button.pack(pady=5)

        pygame.init()
        pygame.mixer.init()

    def load_playlist(self):
        playlist_folder = filedialog.askdirectory(title="Select Playlist Folder")
        if playlist_folder:
            self.playlist = [os.path.join(playlist_folder, file) for file in os.listdir(playlist_folder) if file.endswith(".mp3")]
            self.current_song_index = 0
            self.play_song()

    def play_song(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()

    def shuffle_playlist(self):
        if self.playlist:
            pygame.mixer.music.stop()
            random.shuffle(self.playlist)
            self.current_song_index = 0
            self.play_song()

    def next_song(self):
        if self.playlist:
            pygame.mixer.music.stop()
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play_song()

    def previous_song(self):
        if self.playlist:
            pygame.mixer.music.stop()
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            self.play_song()


if __name__ == "__main__":
    # Executing from the module will create a very simple GUI
    root = tk.Tk()
    app = PlaylistListener(root)
    root.mainloop()
