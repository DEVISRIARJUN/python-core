# 19. Create an abstract MediaPlayer with:
# • load()
# • play()
# • stop()
# Implement:
# • MP3Player
# • WAVPlayer
# • AACPlayer
# Demonstrate calling each via a unified interface.


from abc import ABC,abstractmethod
class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        print("play something")
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3Player(MediaPlayer):
    def load(self):
        print("loading mp3 song")
        super().load()
    def play(self):
        print("playing mp3 song")
    def stop(self):
        print("Stopping mp3 song")
class WAVPlayer(MediaPlayer):
    def load(self):
        print("loading wavplayer")
    def play(self):
        print("playing wav player")
    def stop(self):
        print("stopping wav player")


