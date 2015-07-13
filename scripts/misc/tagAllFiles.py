import nltk
import glob

fileNames = glob.glob('*.txt')

print "The tagger is about to process the following files: "
print fileNames
userOK = raw_input("Continue? (y/n)")

if userOK.lower()[0] == 'y':
	for f in fileNames:
		try:
			nextFile = open(f,'rU')
		except IOError:
			print "cannot open ", arg
		else:
			#The new tagged file will have the same filename, with T added to the beginning
			outputFilename = 'T-'+f

			#read contents of opened file
			raw = nextFile.read()

			#Separate the input text into sentences
			sentences = nltk.sent_tokenize(raw)

			#Separate each sentence into words
			nested = []
			for sentence in sentences:
				nested.append(nltk.word_tokenize(sentence))

    		#Add a part of speech tag to each word
			nested_tagged = []
			for sentence in nested:
				nested_tagged.append(nltk.pos_tag(sentence))

			#Create a new file and write each word, followed by /, followed by its tag.
			#Each sentence is placed on a separate line.
			output_file = open(outputFilename,'w')
			for sentence in nested_tagged:
				for word in sentence:
					output_file.write(word[0] + "/" + word[1] + " ")
				output_file.write("\n")
			output_file.flush() #gets the last bit of data from the buffer to the file
			output_file.close() #suggested as best practice; frees up system memory
