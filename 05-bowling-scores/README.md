# Challenge: Bowling Scores

The Pacific Pine Cone bowling league recently completed their season and wish to publish player results on the interleague website.

The league captain diligently tracked player scores each week in a mobile app on her phone and has provided data exported from the app.  See: `league.json`.

However, three challenges exist:

1. The phone app is limited to exporting JSON data but the web application only supports importing CSV data, and organized differently (see below).
2. The JSON data uses bowling codes (e.g. `'X'` for denoting a strike) however the CVS import only supports numeric values.
3. The league captain doesn't quite trust the website operator and would like you to compute game scores and player season averages that she can verify the website against later.

## Some Tips on the JSON Data

- A player game is represented as a list of 10 sublists:
  - The 10 sublists represent the 10 frames of a bowling game.
  - In the first 9 frames each frame consists of 1 or 2 rolls (only 1 roll for a *strike*, otherwise 2)
  - The 10th frame consists of 2 or 3 rolls (bonus rolls for *strike* or *spare*)
- The following bowling codes are used in the JSON:
  - `'X'` is a **strike** (first roll of a frame)
  - `'/'` is a **spare** (second roll of a frame)
  - `'-'` is a miss of all pins (either roll)
- Each player bowled 3 games per week played.  If a member didn't play a particular night, all game data for that night is replaced by the string `"absent"`.  The JSON data reflects these weekly groups of three games, however that grouping structure is not needed for the CSV import.

## Expected CSV Data

The CSV importer is finicky and requires the CSV data conform to a particular structure to be processed:

Each player game is represented as a line in the CSV, split into 22-23 cells:

  - 1 cell for the player name
  - 18 cells for the first 9 frames, with a cell for each of the 2 rolls per frame
  - 3 cells for the 10th frame with a possible 3 rolls
  - 1 cell for the game score (optional)

Cells where a roll is not normally taken should be left blank (e.g. the second roll of a frame after a **strike**).

Rows should be grouped by weekly game instead of by player as they are in the JSON data.

Each new week group should have a header row with the text `"# Week nn"` where _nn_ is the week number starting from a count of `1`.

Blank rows are ignored by the CSV importer and are safe to use to separate weekly data.

Example result:

    "# Week 1"
    "player 1",3,4,9,1,6,3,7,2,8,1,8,2,7,2,7,3,5,0,6,2,,104
    "player 2",6,3,7,2,5,5,4,6,5,3,7,2,7,3,8,1,9,0,9,1,7,117
    "player 3",10,,10,,10,,10,,10,,10,,10,,10,,10,,10,10,10,300
    "player 1",3,5,7,2,8,2,7,2,6,3,5,5,5,4,7,2,8,1,9,0,,103
    "player 2",6,3,7,3,8,1,8,0,7,2,9,1,7,1,6,0,8,0,7,2,,101
    "player 3",9,1,8,2,8,1,8,1,7,3,7,2,8,2,8,1,9,0,9,1,9,135
    
    "# Week 2"
    "player 1", ...


## Additional Bowling Information

- Full explanation on [keeping score](http://slocums.homestead.com/gamescore.html)
- An online [score calculator](https://www.bowlinggenius.com/)
