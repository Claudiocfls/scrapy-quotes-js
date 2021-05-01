run/scrapy_quotes_js:
	docker-compose up --build -d splash
	scrapy runspider scrapy_quotes_js.py -o quotes.json
	docker-compose down