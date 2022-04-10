import pulsar
from pulsar.schema import *

class Word(Record, word, sentenceid, index, total):
    self.word = word
    self.sentenceid = sentenceid
    self.index = index
    self.total = total

    



# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://130.238.29.222:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('zombies', subscription_name='zombie-sub6')

# Create message var
message = ""

# Display messages received from producer
while True:
	# Receive message
	msg = consumer.receive()
	try:
		# Get content
		msg_data = msg.data().decode('utf-8')

		# Append to message
		message += msg_data.upper() + " "

		# Send response to broker
		consumer.acknowledge(msg)
	except:
		print("exception")
		consumer.negative_acknowledge(msg)
	
	# Print full message
	print(message)

print("closing")
client.close()
