class Movie:
    def __init__(self,title,year,genre) -> None:
        #private attribute ขึ้นต้นด้วย__ ใช้ได้ในclassตัวเองเท่านั้น 
        self.__title = title
        self.__year = year
        self.__genre = genre

    #private method
    def __get_movie(self):
        print(f'Titlte: {self.__title}\nGenre: {self.__genre}')

    #เตรียม public method สำหรับการเข้าถึง private method
    def print_detail(self):
        self.__get_movie()
