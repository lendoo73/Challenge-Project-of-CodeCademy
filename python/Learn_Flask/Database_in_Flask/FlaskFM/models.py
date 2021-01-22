from app import app, db

# ----- Create the Song model -----
#the User model: each user has a username, and a playlist_id foreign key referring
#to the user's Playlist
class User(db.Model):
  id = db.Column(
    db.Integer, 
    primary_key = True
  )
  username = db.Column(
    db.String(50), 
    index = True, 
    unique = True
  ) 
  playlist_id = db.Column(
    db.Integer,  
    db.ForeignKey('playlist.id')
  )
  
  #representation method
  def __repr__(self):
        return "{}".format(self.username)

# ----- Create the Song model -----
# 4-6. create the Song model here + add a nice representation method
class Song(db.Model):
  id = db.Column(
    db.Integer, 
    primary_key = True
  )
  title = db.Column(
    db.String(50),
    index = True,
    unique = False
  )
  artist = db.Column(
    db.String(50),
    index = True,
    unique = False
  )
  n = db.Column(
    db.Integer,
    index = False,
    unique = False
  )
  # 7.
  def __repr__(self):
        return f"{self.title} by {self.artist}"

# ----- Create Song-Playlist pairs -----
# 8-9. create the Item model here + add a nice representation method
class Item(db.Model):
  id = db.Column(
    db.Integer, 
    primary_key = True
  )
  song_id = db.Column(
    db.Integer,
    db.ForeignKey("song.id")
  )
  playlist_id = db.Column(
    db.Integer,
    db.ForeignKey("playlist.id") # 11.
  )

# ----- Creating the Playlist model -----  
# 10. create the Playlist model here + add a nice representation method
class Playlist(db.Model):
  id = db.Column(
    db.Integer, 
    primary_key = True
  )
  # 12.
  items = db.relationship(
    "Item",
    backref = "playlist",
    lazy = "dynamic",
    cascade = "all, delete, delete-orphan"
  )

