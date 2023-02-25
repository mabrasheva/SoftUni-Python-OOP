from project.song import Song


class Album:
    def __init__(self, album_name: str, *songs):
        self.album_name = album_name
        self.published = False
        self.songs = [song for song in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.song_name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.song_name} has been added to the album {self.album_name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.song_name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.album_name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.album_name} is already published."
        self.published = True
        return f"Album {self.album_name} has been published."

    def details(self):
        result = [f"Album {self.album_name}"]
        for song in self.songs:
            result.append(f"== {song.get_info()}")
        return "\n".join(result)
