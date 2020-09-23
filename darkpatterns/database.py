import sqlite3

conn = sqlite3.connect('darkpatterns.db')
curr = conn.cursor()
# curr.execute("""create table dp_table(
#                 website_title text,
#                 cookies text
#             )""") 

curr.execute("""insert into dp_table values('Emi Ylli','Emi pasanikja')""")

conn.commit()
conn.close()