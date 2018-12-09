# Challenge: Bowling Scores

The Pacific Pine Cone bowling league recently completed their season and wish to publish player results on the interleague website.

The league captain diligently tracked player scores each week in a mobile app on her phone and has provided data exported from the app.  See: `league.json`.

However, three challenges exist:

1. The phone app is limited to exporting JSON data but the web application only supports importing CSV data.
2. The JSON data uses bowling codes (e.g. `'X'` for denoting a strike) however the CVS import only supports numeric values.
3. The league captain doesn't quite trust the website operator and would like you to compute game scores and player season averages that she can verify the website against later.

## Some Tips on the Data

- A player game is represented as a list of 10 sublists:
  - The 10 sublists represent the 10 frames of a bowling game.
  - In the first 9 frames each frame consists of 1 or 2 rolls (only 1 roll for a *strike*, otherwise 2)
  - The 10th frame consists of 2 or 3 rolls (bonus rolls for *strike* or *spare*)
- The following bowling codes are used in the JSON:
  - `'X'` is a **strike** (first roll of a frame)
  - `'/'` is a **spare** (second roll of a frame)
  - `'-'` is a miss of all pins (either roll)
- Each player bowled 3 games per week played.  If a member didn't play a particular night, all game data for that night is replaced by the string `"absent"`.  The JSON data reflects these weekly groups of three games, however that grouping structure is not needed for the CSV import.

## Additional Bowling Information

- Full explanation on [keeping score](http://slocums.homestead.com/gamescore.html)
- An online [score calculator](https://www.bowlinggenius.com/)
