import pulsar
from pulsar.schema import *

# Create a schema
class Word(Record):
	word = String()
	index = Integer()
	length = Integer()
	sentenceid = Integer()

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('zombies1', subscription_name='zombie3',schema=AvroSchema(Word))

# Create message var
message = ""

# Store sentences
sentences = {}

while True:
	
	# Receive message
	msg = consumer.receive()

	# Get message content as Word schema
	wrd = msg.value()
	try:

		# The word
		word = wrd.word.upper()

		# Index of word in sentence
		index = wrd.index

		# Total leng
		length = wrd.length
		sentenceid = wrd.sentenceid
		print("sentenceid",sentenceid)
		if not sentenceid in sentences:
			sentences[sentenceid] = [word]
		else:
			sentences[sentenceid].append(word)

		# Send response to broker
		consumer.acknowledge(msg)

		if sentenceid == 2 and index+1 == length:
			break

	except:
		print("exception")
		consumer.negative_acknowledge(msg)

	

# Print sentences
print(sentences)

print("closing")
client.close()