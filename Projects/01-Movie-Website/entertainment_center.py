import media
import fresh_tomatoes

# Create Multiple Instances of Movies
# Movie Instance - Movie Title, Movie Art URL, Movie Trailer URL
# Instance Creation - 01
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Instance Creation - 02
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# Instance Creation - 03
robot = media.Movie("MrRobot",
                    "https://upload.wikimedia.org/wikipedia/en/9/95/MrRobot_intertitle.png",  # NOQA
                    "https://www.youtube.com/watch?v=8qZYW_1hj2g")
# Instace Creation - 04
lotr1 = media.Movie("Lord of the Rings",
                    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")
# Instance Creation - 05
avengers = media.Movie("Avengers: Infinity War",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
# Instance Creation - 06
wick = media.Movie("John Wick: Chapter 2",
                   "https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",  # NOQA
                   "https://www.youtube.com/watch?v=XGk2EfbD_Ps")
# Instance Creation - 07
antmanwasp = media.Movie("Ant-Man adn the Wasp",
                         "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=8_rTIAOohas")
# Instance Creation - 08
deadpool2 = media.Movie("Deadpool 2",
                        "https://upload.wikimedia.org/wikipedia/en/c/ca/Deadpool.png",  # NOQA
                        "https://www.youtube.com/watch?v=I4tFNfROlqk&vl=en")
# Instance Creation - 09
aquaman = media.Movie("Aquaman",
                      "https://upload.wikimedia.org/wikipedia/en/9/9d/Aquaman_Rebirth_1.png",  # NOQA
                      "https://www.youtube.com/watch?v=ZmqJJqFX_CU")
# Instance Creation - 10
creed = media.Movie("Creed",
                    "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Uv554B7YHk4")
# Instance Creation - 11
rockybalboa = media.Movie("Rocky Balboa V",
                          "https://upload.wikimedia.org/wikipedia/en/a/a5/Rocky_v_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=8tab8fK2_3w")
# Instance Creation - 12
interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

# Array With Instances
movies_list = [toy_story,
               avatar,
               robot,
               lotr1,
               avengers,
               wick,
               antmanwasp,
               deadpool2,
               aquaman,
               creed,
               rockybalboa,
               interstellar]
# Call HTML - Pass Movies List
fresh_tomatoes.open_movies_page(movies_list)
