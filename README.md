# Discord Game Tracker
This project was built as a simple tool to help me and my friends track current and upcoming games that we wanted to play. For our purposes, this bot is hosted locally on my machine and requires occasional manual intervention. Currently it runs on my computer as a service and only experiences difficulty with the youtub-dl package.
## Commands
Most commands are docuemnted pretty well internally, or via the `?help` command.
The goal of this bot was to make it as easy as possible for anyone in the server to add games to the list, without forcing them to add any extra command line arguemnts. I occasionally manually update these after the fact to ensure the more specific qureies relating to player numbers are up-to-date.
## Adding Games
Games can be added with a simple string, but support arguments to supply a URL, player counts and a "party" flag. If a string is provided, a simple google search is done appending "steam game" to the end. For 99% of our usecases this is sufficient and returns the approprite steam ID which is then fed into the steam api. If it fails to find an approprite match, it will simply add and disply the plain string as entered by the user. 
