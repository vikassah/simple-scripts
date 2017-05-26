import Algorithmia
from Algorithmia.acl import ReadAcl, AclType

apiKey = 'simRR0Obs7rM5LTlvIknbGom1L11'
# Create the Algorithmia client
client = Algorithmia.client(apiKey)

# Set your Data URI
nlp_directory = client.dir("data://vikassah/nlp_directory")
# Create your data collection if it does not exist
if nlp_directory.exists() is False:
	nlp_directory.create()

# Create the acl object and check if it's the .my_algos default setting
acl = nlp_directory.get_permissions()  # Acl object
acl.read_acl == AclType.my_algos  # True

# Update permissions to private
nlp_directory.update_permissions(ReadAcl.private)
nlp_directory.get_permissions().read_acl == AclType.private # True

text_file = "data://vikassah/nlp_directory/jack_london.txt"

# Upload local file
if client.file(text_file).exists() is False:
	client.file(text_file).putFile("/your_local_path_to_file/jack_london.txt")

# Download contents of file as a string
if client.file(text_file).exists() is True:
	input = client.file(text_file).getString()

# Create the algorithm object using the Summarizer algorithm
algo = client.algo('nlp/Summarizer/0.1.3')
# Pass in input required by algorithm
try:
	# Get the summary result of your file's contents.
	response = algo.pipe(input).result
except:
	# Algorithm error if the input is not correctly formatted.
	print(algo.pipe(input).error.message)