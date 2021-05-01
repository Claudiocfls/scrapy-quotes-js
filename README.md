## Scrapy-quotes-js

A simple project using Scrapy to extract quotes from `http://quotes.toscrape.com/js/`. The page content is build with a JavaScript code, so the scraping should be conducted with any tool able to run this scripts. In this project, Splash is used with this purpose.

## How To Run

`docker-compose` is needed!

```bash
mkdir venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

make run/scrapy_quotes_js
```

## Output example

[File with the extracted items](https://github.com/Claudiocfls/scrapy-books/blob/main/books.csv)
