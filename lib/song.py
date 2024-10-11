from config import CONN, CURSOR

class Song:

    def __init__(self, name, album):
        self.name = name
        self.album = album

## Creates the table using SQL
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

## Saves instance of a song and inserts it into the database
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

## Creates and saves song to database
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song