from movie_private import Movie
class Documentary(Movie):
    def __init__(self, title, year, genre) -> None:
        super().__init__(title, year, genre)
        self.channel = None

    def add_channel(self,channel):
        self.channel = channel

    def show_channel(self):
        print(f'channel: {self.channel}')