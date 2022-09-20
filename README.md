## Octopus Energy Python challenge

### Scope

OE needs to process so-called Electronic Data Interchange (EDI) files in order to
communicate with the energy industry. These are pipe, tilde, and star delimited
text files that are sent to and from us via a variety of different methods. Our
systems then import each file into our database.
There are lots of different types of EDI files but, for this project, we are only
concerned with the EDI 867 files which contain information about meter readings
gathered by field agents (that is, not submitted by customers).
We need a new service that can import these files into a database

### Requirements Documentation

instructions/Python Developer Challenge - Siphon .pdf

### Technical Constraints
SQLite DB
Linux / Mac Compatible  
Python-Version matrix[3.6, 3.7]  
#NOTE No Dataclasses in 3.6  
Environment contraints are enusured with CICD pipeline. Will test parallel builds on ubuntu-latest.  
Check .github/workflows/main.yml for build details.


### Installation and Use

- Create a virtualenv '~/project_folder/.venv'.
- Source that venv. I like to source via updating '~/.bashrc' with 'source ~/project_folder/.venv/bin/activate' - NOTE you can call .bashrc with vim or nano in linux.
- CD to project folder. you should now be operating within your venv.
- extract\decompress gzipped tarball into project folder.
- CD into interview_octopus where the main config files are located including the Makefile.
- run 'make all' - This will set up the needed environment, run CICD, and create an initial SQLite3 database with blank table structs. NOTE - if you do not have make installed a linux prompt will ask you to apt install the package.
- Application is ready for use. Call python3 src/main.py <filename_path or file_directory> and provide either an EDI_96702.txt file or a directory containing the file(s).
- Additionally you can update the run line in the Makefile with the correct paths and use make run after make all. (Default value: run:	python3 src/main.py test_data)
- git Actions CICD pipeline provided for CICD and cooperative work. 
- database files and related scripts can be found in src/database/
- default database name == octopus.db

### Entity Relationship Diagram

![867_02 ERD](T86702_ERD.PNG "867_02 ERD")

### Modifications

NA

 Version              : V0.1

### Authors

Contributors:

Sage Gonzales
Sage@3rdgen.tech

### Version History

- 0.1
  - Initial Release

### License

N/A

### Acknowledgments

N/A