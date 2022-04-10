# se.uu.de2

A1
derek_c1_1: producer, pulsar
130.238.29.222

derek_c1_2: consumer
130.238.29.160

sudo docker run -it -p 6650:6650 -p 8080:8080 \
--mount source=pulsardata,target=/pulsar/data \
--mount source=pulsarconf,target=/pulsar/conf \
apachepulsar/pulsar:2.7.0 bin/pulsar standalone