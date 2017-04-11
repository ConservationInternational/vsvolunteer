import psycopg2
from elasticsearch import Elasticsearch
import json

hostname = 'localhost'
username = 'volunteer'
password = 'password'
database = 'vitalsigns_staging'

es = Elasticsearch()

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
	cur = conn.cursor()
	
	#viewName = "curation__agric_byprod"
	#cur.execute( 'SELECT uuid AS id, row_to_json(' + viewName + ') AS body FROM ' + viewName)
	
	#for row in cur.fetchall():
	
	#	if row[1]["latitude"] != "undefined":
	#		row[1]["location"] = [
	#			row[1]["longitude"],
	#			row[1]["latitude"]
	#		]
	#	else:
	#		del row[1]["latitude"]
	#		del row[1]["longitude"]
	
	#	res = es.index(
	#		index=viewName, doc_type=viewName, id=row[0], body=row[1]
	#		)
	#	status="Row ID: " + row[0] + " | Created: " + str(res['created']) + " | Result: " + res['result']
	#	print(status)
	
	viewName = "curation__household_secB"
	cur.execute( 'SELECT uuid AS id, row_to_json(' + viewName + ') AS body FROM ' + viewName)
	
	for row in cur.fetchall():

		if row[1]["latitude"] != "undefined":
			row[1]["location"] = [
				row[1]["longitude"],
				row[1]["latitude"]
			]
		else:
			del row[1]["latitude"]
			del row[1]["longitude"]

		res = es.index(
			index=viewName.lower(), doc_type=viewName.lower(), id=row[0], body=row[1]
			)
		status="Row ID: " + row[0] + " | Created: " + str(res['created']) + " | Result: " + res['result']
		print(status)


myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database, port=5432 )
doQuery( myConnection )
myConnection.close()