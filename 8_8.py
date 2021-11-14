def make_album (album_name, year, artist, number =None):
    """Returns the info of an album by an artist"""
    album = {'Album name': album_name.title(), 'Year': year, 
    'Artist': artist.title()}
    if number:
        album[number] = number
    return album

while True:
    print("\nPlease enter info about artist and albums: ")
    print("(enter 'q' at any time to quit)")
    
    a_name = input("Please enter the album name: ")
    if a_name == 'q':
        break
    
    a_year = input("Please enter the year of release: ")
    if a_name == 'q':
        break

    ar_name = input("Please enter the name of the artist: ")
    if a_name == 'q':
        break

    a_number = input("Please enter the number of songs in the album: ")
    if a_name == 'q':
        break

    complete_album = make_album(a_name, a_year, ar_name, a_number)
    print(f"Info about album: {complete_album}: ")


