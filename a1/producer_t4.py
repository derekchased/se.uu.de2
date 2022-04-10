import pulsar
import random

# Zombie strings, http://www.zombieipsum.com/
zombie_ipsum = ["Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro.",
	"De carne lumbering animata corpora quaeritis. Summus brains sit, morbo vel maleficia?", 
	"De apocalypsi gorger omero undead survivor dictum mauris."]

# "Source" of data for the producer
string_src = zombie_ipsum[random.randint(0, 2)]

# Split string using spaces
string_split = string_src.split(" ")

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('zombies')

# Send words to broker
for word in string_split:
	producer.send(word.encode('utf-8'))

# Destroy pulsar client
client.close()