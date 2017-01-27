## make pubMLST DB files ##

Scripts to obtain all schemes from pubMLST (http://pubmlst.org/data/dbases.xml) and convert them into Loci Sequences File, in FASTA format, and Sequence Types (profiles) File, in  tab-separated format. These can then be used to create new DB in metaMLST(https://bitbucket.org/CibioCM/metamlst/wiki/metamlst-index). 

## Usage:

First the directory contaning all schemas from pubMLST needs to be created. For that, run the mlst-download_pub_mlst.sh script. It will retrieve all schemas from http://pubmlst.org/data/dbases.xml and save them in a 'pubmlst' folder. 

	./mlst-download_pub_mlst.sh

After you have the pubmlst folder, with all schemes and the xml file inside, you can run the python script to create the sequence and profile files. 

	python makeDB.py ./pubmlst/

## Dependencies:

- Python (2.7.x)
- [Biopython] (http://biopython.org/) (1.66 or similar)

## Installation:

This is a standalone bash/python script and does not require any installation. Simply clone the git repository.

	

## Contact
Catarina Mendes (cimendes@medicina.ulisboa.pt)