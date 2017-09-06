import media
import fresh_tomatoes

# Create Movie instances for some of my favorites
the_thin_red_line = media.Movie("The Thin Red Line",
                                "https://upload.wikimedia.org/wikipedia/en/a/ae/The_Thin_Red_Line_Poster.jpg",
                                "https://www.youtube.com/watch?v=mKl5_OxKBn8")

the_dark_knight = media.Movie("The Dark Knight",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_godfather = media.Movie("The Godfather",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

star_wars = media.Movie("Star Wars - The Empire Strikes Back",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=mz_YWNhKOkM")

logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

fight_club = media.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# Store the separate instances in a list to be used by fresh_tomatoes
movies = [the_thin_red_line,
          the_dark_knight,
          the_godfather,
          star_wars,
          logan,
          fight_club]

# Create the webpage using fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
