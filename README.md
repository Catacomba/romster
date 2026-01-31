Manually downloading and then copying Roms to the appropriate location takes time.
This is a python script for mass copying of rom files from a single folder to the appropriate destinations.

It does the following:

1. Reads all the files in the source folder, including files in .zip archives.
2. Copies the files from the source folder to the destination folder while adhering to the folder structure defined in rom_mappings.json.

    For example, files with .gba extension are copied into destination/gba/
    Files which do not have a config entry will be ignored.

To run the script:

1. Make sure `python3` and `tqdm` python module is installed (this is a module that shows the progress bar).
2. Note down your source (where you download all your roms) and your destination (probably your sdcard/roms) folders.
2. Run the script with `python3 rom_sorter.py <<source>> <<destination>>`

This is work in progress. So I recommend you first do a test run and have a specific folder on disk as a destination folder.
Sofar I have tested it on the Knulli Gladiator OS. But the script should work on all firmware, as long as the config and destination folder is properly selected.
