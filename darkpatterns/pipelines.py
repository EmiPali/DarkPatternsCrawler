# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import sqlite3

class DarkpatternsPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user ='root',
            passwd = 'Emithebillionaire1',
            database = 'dp'
            )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS dp_table""")
        self.curr.execute("""create table dp_table(
                            author text,
                            hour text,
                            status text
                            )""") 

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self,item):
        self.curr.execute("""insert into dp_table values (%s,%s,%s)""",(
            str(item['author'][0].encode('utf-8')),
            str(item['hour'].encode('utf-8')),
            str(item['status'].encode('utf-8'))
        ))
        self.conn.commit()