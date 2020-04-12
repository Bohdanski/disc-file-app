# Disc File App

Disc File App is a package that takes in the tops_disc_items.lst file that is pulled from main frame every Friday(currently), reads through the file line by line, separates the file using commas, trims any trailing spaces, and saves it under the .txt format. The file is saved to the workdrive in a folder to be picked up by a SSIS package.

# Installation

This program is mostly self contained within its folder. Where-ever you decide to place the folder, the path must be manually adjusted within the launcher.bat script.

# Usage

step 1 - Save the tops_disc_items.lst directly to the main script directory.
step 2 - Double click on "launcher.bat" to run the script.

# Versions

v1.0 - 11/27/2019 - Initial stable release

# Author

Bohdan Tkachenko