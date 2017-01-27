import sys, os, datetime, ntpath
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

mlstDirectory=sys.argv[1]

now = datetime.datetime.now()

#make db files - check if they already exist for this month
if os.path.isfile('pubMLST_'+str(now.month)+'_' +str(now.year)+'.txt'):
		os.remove('pubMLST_'+str(now.month)+'_' +str(now.year)+'.txt')
if os.path.isfile('pubMLST_'+str(now.month)+'_' +str(now.year)+'.fasta'):
		os.remove('pubMLST_'+str(now.month)+'_' +str(now.year)+'.fasta')

outfile_txt=open('pubMLST_'+str(now.month)+'_' +str(now.year)+'.txt', 'a')
outfile_fasta=open('pubMLST_'+str(now.month)+'_' +str(now.year)+'.fasta', 'a')


#read all schemas in mlstDirectory
for MLSTschema in os.listdir(mlstDirectory):
	#print MLSTschema
	if os.path.isdir(mlstDirectory+'/'+MLSTschema): #there's a xml in the folder
		schemaName=ntpath.basename(MLSTschema).replace('_','')
		print '-->' + str(schemaName)
		#print 'lala'
		for file in os.listdir(mlstDirectory+'/'+MLSTschema):
			#print file
			if '.txt' in file:
				outfile_txt.write('#'+schemaName+'|'+schemaName+'\n')
				with open(mlstDirectory+'/'+MLSTschema+'/'+file) as schemaTxT:
					for line in schemaTxT:
						outfile_txt.write(line)
			else:
				locusName=ntpath.basename(file)
				print locusName
				with open(mlstDirectory+'/'+MLSTschema+'/'+file) as locusTFA:
					alleles_dict = SeqIO.to_dict(SeqIO.parse(locusTFA, "fasta"))
					for record in alleles_dict:
						toWrite=SeqRecord(alleles_dict[record].seq, id=schemaName+'_'+record, description='')
						SeqIO.write(toWrite, outfile_fasta, "fasta")

outfile_txt.close()
outfile_fasta.close()


