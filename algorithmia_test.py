import Algorithmia

input = "vikassah"

client = Algorithmia.client('simRR0Obs7rM5LTlvIknbGom1L11')

algo = client.algo('demo/Hello/0.1.1')

response =  algo.pipe(input).result
print (response)

