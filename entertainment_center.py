import fresh_tomatoes
import media


# Justice League movie: movie title, storyline, poster image and movie trailer
justice_league = media.Movie(
    "Justice League",
    ("Justice League is an upcoming American superhero film "
     "based on the DC Comics superhero team of the same name, "
     "distributed by Warner Bros. Pictures."),
    "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=RWCQ22JyCL4"
    )

# GOTG movie: movie title, storyline, poster image and movie trailer
guardians_of_the_galaxy = media.Movie(
    "Guardians of the Galaxy",
    ("Guardians of the Galaxy is a 2014 American superhero film "
     "based on the Marvel Comics superhero team of the same name, "
     "produced by Marvel Studios."),
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=d96cjJhvlMA"
    )

# Batman Begins movie: movie title, storyline, poster image and movie trailer
batman_begins = media.Movie(
    "Batman Begins",
    ("Batman Begins is a 2005 superhero film based on the DC Comics "
     "character Batman, co-written and directed by "
     "Christopher Nolan."),
    "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=neY2xVmOfUM"
    )

# Tron Legacy movie: movie title, storyline, poster image and movie trailer
tron = media.Movie(
    "Tron: Legacy",
    ("Tron: Legacy is a 2010 American science fiction action film "
     "directed by Joseph Kosinski from a screenplay written by "
     "Adam Horowitz and Edward Kitsis."),
    "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=L9szn1QQfas"
    )

# Set the movies that will be passed to the media file
movies = [justice_league, guardians_of_the_galaxy, tron, batman_begins]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
