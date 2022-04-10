import pulsar
from pulsar.schema import *

class Word(Record):
	word = String()
	index = Integer()
	length = Integer()
	sentenceid = Integer()

# Zombie strings, http://www.zombieipsum.com/
zombie_ipsum = ["Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro.",
	"De carne lumbering animata corpora quaeritis. Summus brains sit, morbo vel maleficia?", 
	"De apocalypsi gorger omero undead survivor dictum mauris."]

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer(topic = 'zombies1', schema=AvroSchema(Word))

# Send words to broker
for sentenceid, sentence in enumerate(zombie_ipsum):
	words = sentence.split(" ")
	length = len(words)
	for index, word in enumerate(words):
		producer.send(Word(word=word, index=index, length=length, sentenceid=sentenceid))

# Destroy pulsar client
client.close()