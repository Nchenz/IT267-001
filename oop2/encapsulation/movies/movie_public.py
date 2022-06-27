class Movie:

    def __init__(self) -> None:
        self.title = ''
        self.year = 0
        self.genre = ''
    
    #public method
    def add_movie(self,title:str,year:int,genre:str):
        self.title = title
        self.year = year
        self.genre = genre
        
    def get_movie(self):
        return self.title

if __name__ == '__main__':
    m = Movie()
    #call public method -> ชื่อobj.method
    m.add_movie('Mulan',2020,'action')
    print(f'Title: {m.get_movie}')

    #access public attributes -> obj.attribute
    print(f'Title: {m.title}')
    print(f'Year: {m.year}')
    print(f'Genre: {m.genre}')