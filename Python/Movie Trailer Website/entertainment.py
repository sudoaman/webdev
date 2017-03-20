import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "Hello World" , "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" , "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

avatar_story = media.Movie("Avatar", "Hello World" , "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" , "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print (avatar_story.storyline)
#avatar_story.show_trailer()

wonderwoman = media.Movie("Wonder Woman", "DC Super Hero" , "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg" ,
                          "https://www.youtube.com/watch?v=5lGoQhFb4NM")
#wonderwoman.show_trailer()

darkknightrises = media.Movie("Dark Knight Rises", "DC Super Hero" , "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg" ,
                          "www.youtube.com/watch?v=ay-Xg1oTeAs")

Logan = media.Movie("Logan", "DC Super Hero" , "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg" ,
                          "https://www.youtube.com/watch?v=Div0iP65aZo")

Mad_Max = media.Movie("Mad Max", "DC Super Hero" , "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg" ,
                          "https://www.youtube.com/watch?v=hEJnMQG9ev8")
movies = [toy_story,avatar_story,wonderwoman,darkknightrises,Logan,Mad_Max]
fresh_tomatoes.open_movies_page(movies)


