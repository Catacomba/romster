Write a python script.

The python script will have two input parameters.

The first parameter will be the location of the files.
The second parameter will be the root location where the files will be copied to.

The script should also have a config file, which will have the defined the mappings for file locations.
The script should copy files from the first directory to the second directory.
When doing this it should sort the files, based on the file extension into extra subdirectories.

For example:
.gba files should go into ./root/gba
.sfc files should go into ./root/snes

Based on your best knowledge, also create the config file. As you see, this script will copy roms from a large directory into the proper folder structure in the second directory. Consider the file extension and the retro console foldername. The games will then be uploaded to a sd card which will be used in knulli gladiator.

The script should work on windows and Linux. 

If the folders are missing it should create them. 
If the folders already exists it should just copy files into them. If files with the same name already exist it should not replace or overwrite those files,
The script should also first check permissions, so that it can copy the files into the destination and read files from the source.

The script should also include a progress bar that will show how many files are to be copied.
Before beginning copying it should show the user a preview of the first 5 source files and the destination location, so that the user can verify that the files will be copied into the appropriate location.
