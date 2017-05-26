from amazon.api import AmazonAPI # https://pypi.python.org/pypi/python-amazon-simple-product-api 
import configparser

# config variables
config = configparser.ConfigParser()
config.read('config.ini')

# setup keywords/ search queries
keywords = []

kfile = open('./keywords.data', 'r') 
for line in kfile: 
	keywords.append(line)
	#print("Error reading keywords.data file")
print(keywords)
	
# setup brands
brands = []

bfile = open('./brands.data', 'r') 
for line in bfile: 
	brands.append(line)
print(brands)
		
# setup AMAZON API
amazon = AmazonAPI(config['API']['AMAZON_ACCESS_KEY'], config['API']['AMAZON_SECRET_KEY'], config['API']['AMAZON_ASSOC_TAG'])

# run amazon product search
products = amazon.search(Keywords='Diapers', SearchIndex=config['LOCALE']['REGION'])


hcount = 0
pcount = 0
for i, product in enumerate(products):
	if 'huggies' in product.title.lower():
		hcount += 1
	if 'pampers' in product.title.lower():
		pcount += 1
	print(str(i) + ": " + product.title)
	
print(" -- Huggies found :" + str(hcount))
print(" -- Pampers found :" + str(pcount))
