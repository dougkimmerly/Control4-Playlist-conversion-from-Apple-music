
This script will take Apple Music playlists and convert the format so it can be 
imported into Control4.  Since C4 uses its own internal numbers to identify the tracks
you need to first export all the media to a file so the script can look up the numbers
that C4 uses.

From Composer export all media to a file named allC4Music.xml in this directory

From Apple Music Export the playlists that you want in C4 into this directory
to make it easier when exporting name the file with no spaces or funny characters

if you want to start with a clean list of playlists delete the file C4Playlists.xml
Otherwise it will add to the playlists already in that file

run python3 convertPlaylist.py

It will ask you which file you want to convert from the Apple format
then it will ask what you want the C4 playlist to be named

when done (a few seconds) it will display that it is complete 

go to Composer in the media section Import Playlists (right click on playlists) 

Choose the file in this directory named C4Playlists.xml

it will replace all the playlists in C4 with what is now in that file

