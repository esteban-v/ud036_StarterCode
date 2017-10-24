import fresh_tomatoes
import media

justice_league = media.Movie("Justice League",
                     "Justice League is an upcoming American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros. Pictures",
                     "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                     "https://www.youtube.com/watch?v=RWCQ22JyCL4")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                     "Guardians of the Galaxy is a 2014 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures",
                     "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                     "https://www.youtube.com/watch?v=d96cjJhvlMA")

batman_begins = media.Movie("Batman Begins",
                     "Batman Begins is a 2005 superhero film based on the DC Comics character Batman, co-written and directed by Christopher Nolan and starring Christian Bale, Michael Caine, Liam Neeson, Katie Holmes, Gary Oldman, Cillian Murphy, Tom Wilkinson, Rutger Hauer, Ken Watanabe and Morgan Freeman",
                     "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                     "https://www.youtube.com/watch?v=neY2xVmOfUM")

tron = media.Movie("Tron: Legacy",
                     "Tron: Legacy is a 2010 American science fiction action film directed by Joseph Kosinski from a screenplay written by Adam Horowitz and Edward Kitsis, based on a story by Horowitz, Kitsis, Brian Klugman and Lee Sternthal",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                     "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [justice_league, guardians_of_the_galaxy, tron, batman_begins]
fresh_tomatoes.open_movies_page(movies)
