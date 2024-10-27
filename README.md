
This script will take Apple Music playlists and convert the format so it can be 
imported into Control4.  Since C4 uses its own internal numbers to identify the tracks
you need to first export all the media to a file so the script can look up the numbers
that C4 uses.

From Composer export all media to a file named allC4Music.xml in this directory

From Apple Music Export the playlists that you want in C4 into this directory
The files must be named starting with a small "a" then the name you want to see in C4
ending of course with ".xml"  example is "aDinner Music.xml" and put into the working
directory where you have the convertPlaylist.py script.  Export all the playlists you 
want to have in C4, this also serves as a backup of your Apple playlists.

run python3 convertPlaylist.py

The script will first of all delete a file of C4Playlists.xml if it exists and then 
recreate it.  This is because C4 will only import all the playlists at once not each 
one individually.  So the import replaces all the playlists at once with the contents 
of the C4Playlists.xml file

As it processes it will display messages letting you know each playlist converted.
"Conversion complete for aClassical.xml. The Control4 playlist is saved to: C4Playlists.xml"

Since C4 can only accept a playlist of less than 500 tracks each playlist in C4 will be 
named as everything in between the "a" and ".xml" with a number appended to it
Such as "Classical01" and "Classical02" in the above example.

Now go to Composer and in the media section Import Playlists (right click on playlists) 

Choose the file in this directory named C4Playlists.xml

it will replace all the playlists in C4 with what is now in that file

One note not documented anywhere is that in order to get C4 to connect to a shared drive 
the password used for the user can't have any special characters in it or C4 does not make 
the connection.
