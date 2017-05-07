# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:21:19 2016

@author: Javid
"""

import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                      
#print(toy_story.storyline)

avatar=media.Movie("Avatar",
                   "A marine on an aliene planet",
                   "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                   
#print(avatar.storyline)
#avatar.show_trailer()

troy=media.Movie("Troy","Troy war","https://en.wikipedia.org/wiki/Troy_(film)#/media/File:Troy2004Poster.jpg",
                 "https://www.youtube.com/watch?v=znTLzRJimeY")

#troy.show_trailer()

school_of_rock=media.Movie("School of Rock","Using rock music to learn",
                           "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris=media.Movie("Midnight in Paris","Going back in time to meet authors",
                              "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=FAfR8omt-CY")
                              
hunger_games=media.Movie("Hunger Games","Real reality show",
                         "https://en.wikipedia.org/wiki/The_Hunger_Games#/media/File:The_Hunger_Games_cover.jpg",
                         "https://www.youtube.com/watch?v=mfmrPu43DF8")
                         
movies=[toy_story,avatar,troy,school_of_rock,midnight_in_paris,hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
                              