## Installation Instructions

NOTE - Only tested in MacOS Mojave.

`pip install sp-games` - This will pull for the PyPi where the solution is hosted.

Local development teams can clone the git repo and run the `local_build.sh` to get the CLI tool locally in their Virtual environment or directory.

## Getting Started

First item of business is to create an API Key from [Giant Bomb](https://www.giantbomb.com/api/)

`spag congfigure`

## Searching

To search all games, please bear in mind that the API only responds with 100 results and there is currently no pagination.

`spag search`

### Additional options 

`-n` which will be a fuzzy text lookup of the name so:

`spag search -n Fallout`

Providing you have a valid API key this will return some JSON with the matching game titles and GUID.

## Specific Game

To search for a specific game you need the GUID which can be got from [Search](#searching)

`spag game -g 3030-20504`

Will return the specific information about that game.

### Additional Options

`-d` will add an additional search for the DLCs for that game and return them (if any) in order of release date.

Please note if you are searching for Rock Band 2 for example there are a lot of DLCs!

`spag game -g 3030-20504 -d`

## Things to note

- JSON was readable enough for this first version.  This can be improved.
- Friendly User Interaction responses in this version are not yet at a decent level, for example it will not specifically say if there are no DLCs for a game.
- Error Handling leave a lot to be desired at this point in time.
- The API called (being python) for getting DLC release date are not async or threaded so this should probably be done to make this faster.
- Code duplication is currently quite high and can be refactored to be more generic.

## Potential Additions
- We could add an option to pick the response type: i.e. json, text
- Types of information to respond with about a game
- More API integrations...
 
## Testing
- Current tests only validate the response from Giant Bomb API and are not exhaustive.  These would need to be built out further before taking it to a production build.
- Testing of the CLI components would also need to be added.  But my knowledge of testing argparse applications is non-existent.