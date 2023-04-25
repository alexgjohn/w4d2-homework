import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo

# artist_1 = Artist("Jimi Hendrix")
# artist_repo.save(artist_1)

# artist_2 = Artist("Amy Winehouse")
# artist_repo.save(artist_2)

artists = artist_repo.select_all()
for artist in artists:
    print(artist.__dict__)