
This script will take Apple Music playlists and convert the format so it can be 
imported into Control4.  This way you can use Apple Music to control and update all
the playlists on your NAS and then simply import them into Control 4 for playing 
on the system.


Since C4 uses its own internal numbers to identify the tracks
you need to first export all the media to a file so the script can look up the numbers
that C4 uses.

From Composer export all media to a file named FullC4MusicList.xml in this directory

From Apple Music Export the playlists that you want in C4 into this directory where you have the convertPlaylist.py script.  Export all the playlists you want to have in C4, this directory also serves as a backup of your Apple and C4 playlists.

run python3 convertPlaylist.py

The script will first of all delete a file of C4Playlists.xml if it exists and then 
recreate it.  This is because C4 will only import all the playlists at once not each 
one individually.  So the import replaces all the playlists at once with the contents 
of the C4Playlists.xml file

As it processes it will display messages letting you know each playlist converted.
"Conversion complete for Classical.xml. The Control4 playlist is saved to: C4Playlists.xml"

Since C4 can only accept a playlist of less than 500 tracks each playlist in C4 will be 
named as the saved file from Apple Music with a number appended to it
Such as "Classical01" and "Classical02" in the above example.  You can rename the playlist
in C4 if you want after import.

Now go to Composer and in the media section Import Playlists (right click on playlists) 

Choose the file in this directory named C4Playlists.xml

it will replace all the playlists in C4 with what is now in that file

One note not documented anywhere is that in order to get C4 to connect to a shared drive 
the password used for the user can't have any special characters in it or C4 does not make 
the connection.

Also it seems there is a problem with the automatic scanning of the network music directory.
I've opted now to just scan manually when I update the playlists manually that way all the 
internal numbers pointing to the music files stay intact and the playlists continue to 
work.
