import fresh_tomatoes
import movies_api
import MovieClass


ip_man = MovieClass.Movie("IP Man", "Although the Wing Chun master Ip Man is the most skilled martial artist in Foshan," 
                          "he is unassuming and keeps a low profile. ", "https://upload.wikimedia.org/wikipedia/en/2/2f/Ipmanposter02.jpg", 
                          "https://youtu.be/yaIhfOzahX8")


guardians = MovieClass.Movie("Guardians of the Galaxy", "a 2014 American superhero film based on the Marvel Comics superhero team of the same name", 
                            "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", 
                            "https://youtu.be/2XltzyLcu0g")

choke = MovieClass.Movie("Choke", "The film is based on the 2001 novel of the same name by Chuck Palahniuk."
                        "It tells the story of a man who works in a colonial theme park,attends sexual addiction"
                        "recovery meetings, and intentionally chokes on food in upscale restaurants"
                        "so his rescuers would give him money out of sympathy and thus cover his mother's Alzheimer's disease hospital bills.", 
                        "https://upload.wikimedia.org/wikipedia/en/0/0d/Chokeposter.jpg", 
                        "https://youtu.be/yMZ3Mi1vT-w")

ong_bak = MovieClass.Movie("Ong-Bak", "In the rural northeastern Thailand village of Ban Nong Pradu" 
                          "lies an ancient Buddha statue named Ong-Bak. The village falls in despair"
                          "after thieves from Bangkok decapitate the statue and take the head with them."
                          "Ting, a villager extremely skilled in Muay Thai, volunteers to travel to Bangkok to recover the stolen"
                          "head of Ong-Bak. His only lead is Don, a drug dealer who attempted to buy the statue one day earlier.", 
                          "https://upload.wikimedia.org/wikipedia/en/1/11/ONG-BAK.jpg", 
                          "https://youtu.be/iJvMhOkwH9I")


apocalypto = MovieClass.Movie("Apocalypto", "Set in pre-Columbian Yucatan and Guatemala around the year 1511,"
                            "even though the Mayan collapse happened some 600 years earlier,"
                            "Apocalypto depicts the journey of a Mesoamerican tribesman who must escape"
                            " human sacrifice and rescue his family after the capture and destruction of his village"
                            "at a time when the Mayan civilization is about to come to an end.", 
                            "https://upload.wikimedia.org/wikipedia/en/6/62/Apocalypto-poster01.jpg", 
                            "https://youtu.be/ngWBddVNVZs")

wood = MovieClass.Movie("The Wood", "The Wood is a 1999 American coming of age film written by Rick Famuyiwa and Todd Boyd and directed by Rick Famuyiwa."
                        "The film stars Omar Epps, Richard T. Jones and Taye Diggs.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f7/Wood_poster.jpg", 
                        "https://youtu.be/4_HEXcaDpMI")

movie_list = [ip_man, guardians, choke, ong_bak, apocalypto, wood]
fresh_tomatoes.open_movies_page(movie_list, movies_api.get_movie_data)
