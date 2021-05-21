# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: c


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class CryptodetailsPipeline(object):

	def __init__(self):
		self.conn = pymongo.MongoClient('localhost',27017)
		db = self.conn['Crypto']
		self.collection=db["crypto_details"]

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item
