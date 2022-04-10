
import pulsar
from pulsar.schema import *
import sys

class Wordd(Record):
    wordd = String()


if __name__ == "__main__":
    args = sys.argv
    
    print("args",args)

    try:
        client_type = args[1]
    except:
        exit()
        assert("error")

    try:
        topic_name = args[2]
    except:
        topic_name = "zombies"

    try:
        host = args[3]
    except:
        host = "localhost"

    if client_type == "producer":
        # Create a pulsar client by supplying ip address and port
        client = pulsar.Client('pulsar://localhost:6650')

        # Create a producer on the topic that consumer can subscribe to
        producer = client.create_producer(topic = topic_name, schema=AvroSchema(Wordd))

        # Zombie string, http://www.zombieipsum.com/
        zombie_ipsum = "Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro."    

        for word in words:
            print(word)
            producer.send(Word(wordd=word))

        # Destroy pulsar client
        client.close()

    elif client_type == "consumer":
        consumer = Consumer(topic_name, host)
