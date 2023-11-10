# PPP
Python Playlist Player (PPP) is a simple Python application that allows you to listen to musics offline on your computer
# Versions

None

# Requirements

Clone the repository on your computer:
`git clone https://github.com/Ierzi/PPP.git`

Install the required Python librairy:
`pip install pygame`

Create a folder with all of your songs in the mp3 format.

# Usage

* Method 1
Run the python script:
`python playlistlistener.py`

Click the "Load Playlist" button to start. The program will ask you to select a folder (your playlist).
Then click on Play to start playing the song

Want some variety? Click the "Shuffle" button to mix up your playlist and start from a random song.

Use the "Next" and "Previous" buttons to skip to the next or previous song in your playlist.

* Method 2

You can import the main file in your own program: `import playlistlistener`

Then, you can create a window by copying this program:

`root = tk.Tk()´
´app = PlaylistListener(root)´
´root.mainloop()´

