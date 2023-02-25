from project.album import Album


class Band:
    def __init__(self, band_name: str):
        self.name = band_name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.album_name}."
        return f"Band {self.name} already has {album.album_name} in their library."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.album_name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for album in self.albums:
            result.append(album.details())
        return "\n".join(result)
