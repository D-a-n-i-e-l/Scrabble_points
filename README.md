# Scrabble_points
A simple calculator to see how many Scrabble points a word or name is.

# Background
I was inspired by an r/NBA reddit post(https://reddit.com/r/nba/comments/bvfen8/random_oc_which_nba_players_full_name_would/) in which the poster fed the names of active/paid basketball players and returned a sorted list of who's name would yield the highest points in Scrabble. I saw this and immediately thought it would be an interesting coding challenge for myself.

# Scrabble Key
The user had provided a key to go off of: https://www.thewordfinder.com/scrabble-point-values.php

# Challenges
Syntactically, there were a few requirements:
- Hyphens, spaces, apostrophes etc. are worth 0 points
- Need to make it so that code dosen't throw a keyerror if text entered not in dictionary

# Solution
I first created a dictionary with all the scrabble word point pairs. Then I greated a generator that listed every number value that was found in the word entered. I then summed the whole generator. In addition, I changed scrab[value] to scrab.get[value, 0] so that any letter/character that was not found in the dictionary would be passed as a zero, therefor having no impact on score.
