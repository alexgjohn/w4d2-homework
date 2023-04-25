from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repo

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    rows = run_sql(sql, values)
    id = rows[0]['id']
    return album


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE ID = %s"
    values = [id]
    rows = run_sql(sql, values)
    if rows:
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'], album_info['genre'], artist, album_info['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

# oof, let's see if this works!
#UPDATE: it did not :(
def list_albums_by_artist(artist):
    albums_by_artist = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    rows = run_sql(sql, values)
    if rows:
        for row in rows:
            album = Album(row['title'], row['genre'], row['artist'], row['id'])
            albums_by_artist.append(album)
    return albums_by_artist
