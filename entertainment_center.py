import fresh_tomatoes
import media

# Create 3 Movie instances, add to list, and run the fresh_tomatoes program

office_space = media.Movie("Office Space",
                           "Life in a Corporate America cubicle",
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=3_fG_zLbBeU")

animal_farm = media.Movie("Animal Farm",
                          "George Orwell's Book about America's future soon",
                          "https://upload.wikimedia.org/wikipedia/en/8/85/Tt0204824.jpeg",  # noqa
                          "https://www.youtube.com/watch?v=LAeKX5n-5IE")

rock_star = media.Movie("Rock Star",
                        "Dream comes true but he finds out not so glamourous",
                        "http://www.impawards.com/2001/posters/rock_star_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=-OTQoNvgyYs")

movies = [office_space, animal_farm, rock_star]

fresh_tomatoes.open_movies_page(movies)
