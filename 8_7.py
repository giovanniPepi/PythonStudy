def make_album (album_name, year, artist, number =None):
    """Returns the info of an album by an artist"""
    album = {'Album name': album_name.title(), 'Year': year, 
    'Artist': artist.title()}
    if number:
        album[number] = number
    return album

album = make_album(album_name = 'The number of the beast', year = '1982', 
artist = 'iron maiden', number = 8)

print(album)

album = make_album(album_name = 'seventh son of a seventh son', year = '1988', 
artist = 'iron maiden')

print(album)

album = make_album(album_name = 'distance over time', year = '2019', 
artist = 'dream theater')

print(album)