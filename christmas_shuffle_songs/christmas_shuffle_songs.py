
import pygame
import random
import time

def play_song(file_path):
    """Play a single song."""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # Check if music is still playing
        pygame.time.Clock().tick(10)

def shuffle_and_play_playlist(songs):
    """Shuffle and play a list of songs."""
    random.shuffle(songs)  # Shuffle the playlist
    for song in songs:
        print(f"Now playing: {song}")
        play_song(song)

def main():
    # Initialize pygame mixer
    pygame.mixer.init()

    # List of song file paths
    christmas_songs = [
        'song1.mp3',  # Replace with actual file paths
        'song2.mp3',
        'song3.mp3',
        # Add as many songs as you like
    ]

    shuffle_and_play_playlist(christmas_songs)

if __name__ == "__main__":
    main()
