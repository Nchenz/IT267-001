class Movie:
    def __init__(self) -> None:
        #protected attribute ขึ้นต้นด้วย _
        self._title = None
        self._year = 0
        self._genre = None
        self._rating = 6

    #protected method ขึ้นต้นด้วย  _
    def _add_movie(self,title,year,genre,rating=6):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = rating

    def _get_movie(self):
        return f'Title: {self._title}\nYear: {self._year}\nGenre: {self._genre}\nRating: {self._rating}'