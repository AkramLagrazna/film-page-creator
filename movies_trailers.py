import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=moSRMC5JNww")
il_dittatore = media.Movie("Il dittatore",
                           "A crazy dictator in the middleast",
                           "https://mr.comingsoon.it/imgdb/locandine/big/48444.jpg",
                           "https://www.youtube.com/watch?v=WtadfOVzo8s")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://is1.mzstatic.com/image/thumb/Video69/v4/22/50/c3/2250c3e7-6b24-a0df-dd8f-dea7321b3ee4/source/1200x630bb.jpg",
                          "https://www.youtube.com/watch?v=5GefcbKsWww")
back_to_the_future = media.Movie("Back to the Future",
                                "A viaggio on the past and future",
                                "https://images-production.global.ssl.fastly.net/uploads/photos/file/205224/back-to-the-future.jpg",
                                "https://www.youtube.com/watch?v=qvsgGtivCgs")
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcSNq5sLDlhOo0FnyGadcPWI_PD6Y8xdWUSd-2RucDnPIpvvt6db",
                           "https://www.youtube.com/watch?v=vJPfwRAbrBo")
movies = [toy_story,avatar,il_dittatore,back_to_the_future,hunger_games,ratatouille]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
