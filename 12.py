class Media:
    pass

class Book(Media):
    pass

class Movie(Media):
    pass

def check_media_type(obj):
    if isinstance(obj, Book):
        print("Book")
    elif isinstance(obj, Movie):
        print("Movie")
    elif isinstance(obj, Media):
        print("Media")
    else:
        print("Unknown media")

book = Book()
movie = Movie()
unknown = "Some Text"

check_media_type(book)
check_media_type(movie)
check_media_type(unknown)