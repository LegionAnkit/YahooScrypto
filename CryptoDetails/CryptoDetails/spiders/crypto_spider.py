import scrapy
from bs4 import BeautifulSoup
from ..items import CryptodetailsItem

class CryptoSpider(scrapy.Spider):
	name='crypto'
	start_urls= [
		'https://in.finance.yahoo.com/cryptocurrencies'
	]

	def parse(self, response):

		items = CryptodetailsItem()

		#Beautifulsoup for parsing source code
		
		soup = BeautifulSoup(response.text, 'lxml')
		for data in soup.select('.simpTblRow '):
			#print scraped data
			symbol=data.select('[aria-label=Symbol]')[0].get_text()
			name=data.select('[aria-label=Name]')[0].get_text()
			price=data.select('[aria-label="Price (intraday)"]')[0].get_text()
			change=data.select('[aria-label=Change]')[0].get_text()
			per_change=data.select('[aria-label="% change"]')[0].get_text()
			market_cap=data.select('[aria-label="Market cap"]')[0].get_text()

			items['symbol']=symbol
			items['name']=name
			items['price']=price
			items['change']=change
			items['per_change']=per_change
			items['market_cap']=market_cap

			yield items