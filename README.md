# game-of-life_HackClub
A terminal version of [Conways Game of Life](https://playgameoflife.com/)

The program gets a game of life board, either from a user inputted file or a user chosen random soup.  
Then the user gets asked what type of neighborhood layout they want the cells to use (Moore or Von Neumann).  
The board gets played out until it repeats itself or until a figure is made that loops without being stationary and the   
user has to stop the program themselves.    

Rules of Life:
- Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
- Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
- Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
- Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

## EXAMPLE

Starting board (Using Moore's neighborhood)   
<img src="https://imgur.com/P3A7gvf.jpg" width="200">

After calculations   
<img src="https://imgur.com/yJiZ16a.jpg" width="200">

## How to Run
#### (This has only been tested on a Mac so instructions are only for Mac)
1. Download the most recent executable from the [releases page](https://github.com/hardeek-sharma/game-of-life_HackClub/releases)
2. Open up Terminal.app and cd to where the file is downloaded
3. type "chmod +x " and drag the executable over to the terminal line so it auto fills in its path
4. The terminal thing might look like this: chmod +x /Users/name/Downloads/main
5. Type ./main in the terminal and now the program works
6. only step 5 is needed to use the program again