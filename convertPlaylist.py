import xml.etree.ElementTree as ET
import os
import glob

# Function to load Control4 song mapping from XML
def load_control4_song_mapping(control4_file):
    mapping = {}
    tree = ET.parse(control4_file)
    root = tree.getroot()
    
    # Navigate to the songs section and build the mapping
    for song in root.findall('.//song'):
        name = song.find('name').text if song.find('name') is not None else None
        artist = song.find('artist').text if song.find('artist') is not None else None
        song_id = song.find('id').text if song.find('id') is not None else None
        
        if name and artist and song_id:
            mapping[(name, artist)] = song_id  # Use a tuple (name, artist) as the key

    return mapping

def convert_apple_music_to_control4(input_file, output_file, control4_mapping, base_playlist_name):
    if os.path.exists(output_file):
        # Load existing file
        tree = ET.parse(output_file)
        root = tree.getroot()
        playlists = root.find('playlists')  # Get existing playlists
    else:
        # Create the root of the output XML
        root = ET.Element("media")
        version = ET.SubElement(root, "version")
        version.text = "2"
        playlists = ET.SubElement(root, "playlists")
    
    # Locate the "Tracks" dictionary in the Apple Music export
    tracks_dict = ET.parse(input_file).getroot().find('.//dict[key="Tracks"]/dict')

    if tracks_dict is not None:
        song_count = 0
        playlist_number = 1  # Start with the first playlist
        current_playlist = create_new_playlist(root, playlists, base_playlist_name, playlist_number)

        for track in tracks_dict:
            # Confirm we are looking at a dictionary (the individual track entries)
            if track.tag == 'dict':
                song_name = None
                artist_name = None
                track_no = None

                # Initialize variables for key lookups
                for i in range(0, len(track), 2):  # Keys are at even indices, values are at odd indices
                    key_elem = track[i].text if track[i].tag == 'key' else None
                    if key_elem is not None:
                        if key_elem == "Name":
                            song_name = track[i + 1].text  # This should be the <string> element
                        elif key_elem == "Artist":
                            artist_name = track[i + 1].text  # This should be the <string> element
                        elif key_elem == "Track Number":
                            track_no = track[i + 1].text if track[i + 1].tag == 'integer' else "0"

                # Find the Control4 ID using the song information
                control4_id = control4_mapping.get((song_name, artist_name))

                # Create song element in the current playlist
                song_element = ET.SubElement(current_playlist, "song")
                name_element = ET.SubElement(song_element, "name")
                name_element.text = song_name if song_name else "Unknown"
                artist_element = ET.SubElement(song_element, "artist")
                artist_element.text = artist_name if artist_name else "Unknown"
                track_no_element = ET.SubElement(song_element, "track_no")
                track_no_element.text = track_no if track_no else "0"
                id_element = ET.SubElement(song_element, "id")
                id_element.text = control4_id if control4_id else "0"  # Use Control4 ID or default to "0"
                type_element = ET.SubElement(song_element, "type")
                type_element.text = "SONG"  # Assuming all entries are songs

                # Increment the song count
                song_count += 1

                # When reaching 499 songs, create a new playlist
                if song_count % 499 == 0:
                    playlist_number += 1  # Increment playlist number
                    current_playlist = create_new_playlist(root, playlists, base_playlist_name, playlist_number)

    # Write to output file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def create_new_playlist(root, playlists, base_name, number):
    # Format the playlist name with leading zeroes if desired
    playlist_name = f"{base_name} {number:02d}"
    
    new_playlist = ET.SubElement(playlists, "playlist")
    playlist_id = ET.SubElement(new_playlist, "id")
    playlist_id.text = str(len(playlists.findall('playlist')) + 1)  # Incremental ID for new playlist
    title = ET.SubElement(new_playlist, "title")
    title.text = playlist_name  # Set the playlist name
    songs = ET.SubElement(new_playlist, "songs")  # Create the songs container
    return songs  # Return the songs element to add songs to this playlist

# Main execution
if __name__ == "__main__":
    control4_file = 'allC4Music.xml'  # Location of the Control4 music XML
    output_file = 'C4Playlists.xml'  # Desired output file location

    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Load the Control4 song mapping from the exported XML
    control4_mapping = load_control4_song_mapping(control4_file)

    # Process each XML file that starts with "a", ends with ".xml", and is not 'allC4Music.xml'
    for input_file in glob.glob('a*.xml'):
        if input_file == control4_file:
            continue  # Skip the 'allC4Music.xml' file
        
        # Extract the base playlist name from the input file name
        base_playlist_name = input_file[1:-4]  # Get the name between 'a' and '.xml'

        # Convert the Apple Music file to Control4 format using the mapping
        convert_apple_music_to_control4(input_file, output_file, control4_mapping, base_playlist_name)

        print(f"Conversion complete for {input_file}. The Control4 playlist is saved to: {output_file}")

