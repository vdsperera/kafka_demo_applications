# kafka_demo_applications

# start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# start kafka
bin/kafka-server-start.sh config/server.properties

# generate values and publish them to raw_values_topic(new terminal)
python3 value_producer.py 

# consume raw values from raw_values_topic, process them(find even values) and publish them to processed_values_topic(new terminal)
python value_consumer_processed_value_producer.py

# consumes values from processed_values_topic(new terminal)
bin/kafka-console-consumer.sh --topic raw_values_topic --from-beginning --bootstrap-server localhost:9092