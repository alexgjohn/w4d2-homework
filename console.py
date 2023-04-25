import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo


album_repo.delete_all()
artist_repo.delete_all()

artist_1 = Artist("Jimi Hendrix")
artist_2 = Artist("Amy Winehouse")
artist_repo.save(artist_1)
artist_repo.save(artist_2)



album_1 = Album("Are You Experienced?", "Rock and Roll", artist_1)
album_2 = Album("Electric Ladyland", "Rock and Roll", artist_1)
album_3 = Album("A Day At The Races", "Soul", artist_2)

album_repo.save(album_1)
album_repo.save(album_2)
album_repo.save(album_3)

artists = artist_repo.select_all()
for artist in artists:
    print(artist.__dict__)

albums = album_repo.select_all()
for album in albums:
    print(album.__dict__)

#didn't crack this one, but oh well!
# albums_by_artist_1 = album_repo.list_albums_by_artist(artist_1)

# print(albums_by_artist_1)