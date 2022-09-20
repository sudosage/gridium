## Octopus Energy Python challenge

### Scope
Write a simple Python web scraper to help us visit the tide pools. 
Go to https://www.tide-forecast.com/ to get tide forecasts for these locations:
- Half Moon Bay, California

- Huntington Beach, California

- Providence, Rhode Island

- Wrightsville Beach, North Carolina

Load the tide forecast page for each location and extract information on low tides that occur after sunrise and before sunset. Return the time and height for each daylight low tide.
In your response, be sure to include a URL where we can see the code and a description of how to run it (including installing dependencies, if needed).

### Requirements Documentation

Email via Employer  
### Technical Constraints
Python web scraper

### Application outline
- Simple python application to scrape and ingest data from provided URL into a sqlite DB for storage and future viewing.(SQLite for the provided demonstration for its light weight nature)
- Makefile for environment setup and integration testing."Run" cmd included for ease of application use.
- .github/workflows/main.yml file provided for simple CICD via github actions.
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