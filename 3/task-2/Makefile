run:
	@python3 kafka-consumer.py "crop-prices"
	@cat kafka-5-percent-dataset.csv | python3 kafka-producer.py "crop-prices"

consumer:
	python3 kafka-consumer.py "crop-prices"

producer:
	cat kafka-5-percent-dataset.csv | python3 kafka-producer.py "crop-prices"

save:
	@python3 kafka-consumer.py "crop-prices" > output.json

# test: 
# 	diff -s <(jq --sort-keys . output.json) <(jq --sort-keys . solution.json)
