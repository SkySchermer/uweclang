import uweclang
from uweclang import get_files
import antlr4
import ntpath

def compare_result(result, expected):
	num_lines = sum(1 for line in open(expected)) #don't we need to compare if the lines are equal?
	return len(result) == num_lines
	
def run_test(input, text, expected):
	query = None
	result = None
	with open(input, 'r') as infile:
		query = Query(infile.read())
	with open(text_file, 'r') as infile:
		result = query.execute_query(infile.read())
	
	return compare_result(result, expected)
	
def get_basename(path):	#Function to avoid empty strings if file ends with '\'
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def tester(dir): #change it to main?
	
	files, num_files = get_files(dir) #returns a tuple
	test_results = []
	
	print('Running tests')
	for f in files:
	    filename = get_basename(f)
		if filename.startswith('query'):
			e = 'example_' + filename[6] #not generic but works for our case
			r = 'result_' + filename[6:7]
			test_results.append(filename, e, r, run_test(filename, e, r))
	print('Tests results:')
	
	for (q, e, r, t) in test_results:
		print "Query: ", q, "."*(20-len(q)), "Example: ", e, "."*(20-len(e)), "Result: ", r, "."*(20-len(r)), "TEST: ", t