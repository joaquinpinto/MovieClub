# MovieClub
Analysis of Movie Ratings For Movie Club

This is a project I worked on using data I received from my friends.

## Who Are My Friends:

We are a group of 5 friends who met in High School (and 1 person who made his way into the group during college) who are all thoroughly interested in cinema. During High School one of our main weekend hang-outs was at the matinee showing of new films at AMC. Together we endulged ourselves in classics such as The Hunger Games and The Purge for the low price of $5. 


## Movie Club:

After college a few of us found ourselves outside of the city. We thought it would be a great idea to continue our tradition of watching films during the weekend with a bi-weekly, long-distance movie club. We were to watch movies every other Friday and comment on them the following Sunday. 


## How Do We Select These Movies:

This idea behind this club changed a bit, we were originally going to watch new films, however the cost of watching these would've been too high for our budget, so we decided to go through old movies first. We began by each offering up a set of movies that we were interested in watching, some of us already had lists, others just looked through their recomended movies lists on Netflix.

I then compiled those movies onto a Google Sheet and had each member rate their willingness to watch the movies with these guidelines:

  1. The score must be from 1-10.
  2. Be reasonable with movies you've watched already, if we've all seen them there's no use in watching them again.
  3. You may only use the 1 and the 10 a maximum of one time in your ratings (I'll mention why shortly).


## How Do We Make This Fun:

We didn't, it was very tedious. 

However, I added a little game to it.

## Each person has 2 Power-Ups, the 1-Card and the 10-Card.

  - 1-Card: This means you really don't want to watch this film, it functions as an extra -5 to the movie's score.  
  - 10-Card: This means that the film is your top choice, it functions as an extra +5 to the movie's score.  

The Google Sheet would mark that person't column red if they had 2 or more 1 or 10 ratings.


## That's Cool and All, But Where's The Analysis:

I'm getting there, give me a second!

After getting the ratings from my friends I sought to balance each person's ratings, so that we all had the same say in the movie selection. 

This was performed by finding the Z-Scores of each rating for each Rater:
  - Z-Score = (Score - Rater's AVG Score)/Rater's SD.   

I then took the average Z-score for each movie and normalized it back to a 1-10 scale with 5 being the mid-point:
  - 5 + (Avg Z-Score * 10)/(Max AVG Z - Min AVG Z)    
  
Afterwards I added/subtracted the power ups and rounded to two-digits:
  - Blazing Saddle Adjusted Score = 5.04 + 5/6 = 5.87   

This was all completed directly on the Google Sheet so as to be as open as possible, I have recreated this in a Jupyter Notebook.


## Movie Order:

Once I found out how each movie was rated I ranked them and removed all the movies with scores below 5.

Since the plan was to watch all the movies, but we weren't sure how long the club would last, I recomended that we make a weighted average ranking. This would allow us to vary the movies, so that we don't watch all the good ones first and then get bored near the end. We gave preference to the top movies, but the ultimate ranking was random.

The code for the weighted ranking is shown here as MovieRankWeight.py.

I ran this 3 times and we chose our favorite from there.

### This was our final order:

  Week 1: District 9  
  Week 2: Goodfellas  
  Week 3: Coco  
  Week 4: City of God  
  Week 5: Moonrise Kingdom  
  Week 6: Blazing Saddles  
  Week 7: Usual Suspects  
  Week 8: Hoop Dreams  
  Week 9: Dazed and Confused  
  Week 10: Shaun of the Dead  
  Week 11: Gattaca  
  Week 12: Scott Pilgrim  
  Week 13: Escape from New York  
  Week 14: Old School  
  Week 15: Set it Up  
  Week 16: 12 Monkeys  
  Week 17: Annihilation  
  Week 18: The Fight Club  
  Week 19: Incredibles 2  
  Week 20: Halloween  
  Week 21: Warriors  
  Week 22: Scream  
  Week 23: Hot Fuzz  
  Week 24: The Jerk  
  Week 25: Forrest Gump  
  Week 26: Airplane!  
  Week 27: Basic Instinct  
  Week 28: Reservoir Dogs  
  Week 29: Crazy Rich Asians  
  Week 30: Saw  
  Week 31: Matrix  
  Week 32: Blade Runner 2049  
  Week 33: In Bruges  
  Week 34: Shawshank Redemption  
  Week 35: Zodiac  
  Week 36: Ghost in the Shell (1995)  
  Week 37: Accident Man  
  Week 38: Return of the Dragon  
  Week 39: Gangs Of New York  
  Week 40: Taxi Driver  
  Week 41: Bill and Ted  
  Week 42: Easy A  
  Week 43: Apocalypse Now  
  Week 44: American Gangster  
  Week 45: Donnie Darko  
  Week 46: Bourne  
  Week 47: The Naked Gun  
  Week 48: Dredd  
  Week 49: Cool Hand Luke  

Lastly, I also ran through the original scores to find the closest raters and how far each person strayed from the group.

The code for this is in MovieClubRating.py.

These are the results:

### Closest Raters 

  1. Givnos and Mohinos with an average distance of 1.89 per movie
  2. Joaquinos and Marquinos with an average distance of 1.98 per movie
  3. Marquinos and Mohinos with an average distance of 2.04 per movie
  4. Givnos and Joaquinos with an average distance of 2.05 per movie
  5. Givnos and Marquinos with an average distance of 2.05 per movie
  6. Givnos and Jerminos with an average distance of 2.16 per movie
  7. Jerminos and Marquinos with an average distance of 2.23 per movie
  8. Joaquinos and Mohinos with an average distance of 2.26 per movie
  9. Jerminos and Joaquinos with an average distance of 2.28 per movie
  10. Jerminos and Mohinos with an average distance of 2.35 per movie
  11. Givnos and Jaminos with an average distance of 2.36 per movie
  12. Jaminos and Joaquinos with an average distance of 2.48 per movie
  13. Jaminos and Marquinos with an average distance of 2.51 per movie
  14. Jaminos and Mohinos with an average distance of 2.59 per movie
  15. Jaminos and Jerminos with an average distance of 2.91 per movie

 ### Average Group Distance 

  1. Givnos with an average distance of 2.1 from the group
  2. Marquinos with an average distance of 2.16 from the group
  3. Joaquinos with an average distance of 2.21 from the group
  4. Mohinos with an average distance of 2.22 from the group
  5. Jerminos with an average distance of 2.39 from the group
  6. Jaminos with an average distance of 2.57 from the group
