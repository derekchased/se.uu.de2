import pulsar
from pulsar.schema import *

# Schema for data transfer
class Word(Record):
	word = String()
	index = Integer()
	length = Integer()
	sentenceid = Integer()

"""
Sample consumer application which accepts messages, converts them to uppercase, and then merges them

*** I added some complexity to the assignment to test out the schema and to think about 
the message properties object (not represented in the code) and how sequence is handled. 
*** Therefore, the output is slightly different. It combines words into sentences rather.
"""


# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('zombies1', subscription_name='zoadsdd',schema=AvroSchema(Word))

# Create storage dict
sentences = {}

# "Forever" loop
while True:
	
	# Receive message
	msg = consumer.receive()

	# Get message object with access according to Word schema
	wrd = msg.value()
	try:
		# Get word and convert
		word = wrd.word.upper()

		# Index of word, length of sentence: not used
		index = wrd.index
		length = wrd.length

		# ID of sentence this word belongs to
		sentenceid = wrd.sentenceid
		if not sentenceid in sentences:
			sentences[sentenceid] = [word]
		else:
			sentences[sentenceid].append(word)
		
		# Send response to broker
		consumer.acknowledge(msg)

		# For this assignment, I send 3 sentences. Instead of printing out
		# all messages, let's just break out of this loop then print it once.
		if sentenceid == 2 and index+1 == length:
			break

	except Exception as e:
		print(f"exception {e}")
		consumer.negative_acknowledge(msg)

# Print each sentences
for i in sentences:
	print( " ".join(sentences[i]) )

# Close this consumer client
client.close()