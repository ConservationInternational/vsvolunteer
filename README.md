# Conservation International Data Visualizations

This is a guide for volunteers and data scientists to access Conservation International's repository and create data visualizations using the Kibana tool.

## Setup
Install Elasticsearch and Kibana locally. Find instructions for your operating system here: https://www.elastic.co/guide/index.html

## Database Access

We've provided data in PostgreSQL format that you can view and query to get an understanding what data is available for use.

Option 1. You can access the database by connecting with our volunteer read only user. This is a PostgreSQL database hosted on Amazon RDS. We recommend using a Postgres SQL client to connect and view data, such as Postico or pgAdmin.
username: volunteer
password: password
host: 54.242.126.6


## Transcribe Data From Postgres to ElasticSearch (ETL step)

In order to create a data visualization in Kibana, the data you wish to work with must be loaded into ElasticSearch. To do this, we typically use python scripts to query data from postgres and output it to ElasticSearch. The python script could be as simple as querying a few selected columns from a table, or it could be more complex and could programmatically aggregate and transform data.

See postgresToElasticSearch.py as an example.

## Creating Data Visualization in Kibana
After you run your python script, navigate to your local kibana instance and configure a visualization.

To perform this task, you must first create a new index pattern. This can be done by following these steps:

1) In Kibana, select "Management" from the left-side tab.
2) Select "Index Patterns" on the following screen.
3) Locate the “Add New” button in the top left hand corner and click the button.
4) On the following page, update the “Index name or Pattern” field to be the name of the index imported (i.e. curation__household_secb).
   - Note: To update the available indexes you will have to click outside the text field.
   - There will be a dropdown that will allow indexing on a time-based event.
     - This is optional, although it is important to keep in mind if the number of documents (rows in the DB) increases as time passes, indexing on a time-based field will allow searches to target the most recent documents. ( ref. https://www.elastic.co/guide/en/elasticsearch/guide/current/time-based.html ).

Consult the [Kibana User Guide](https://www.elastic.co/guide/en/kibana/current/index.html) as needed.

When your visualization is complete, [export it to a JSON file](https://discuss.elastic.co/t/how-to-save-dashboard-as-json-file/24561/4).

Commit the JSON export file to your repository.

## Submit Pull Request
When you are satisfied with the python script and visualization JSON file, submit a pull request. If approved, your script will be added to the repository, the script will be executed, and the data you staged should become available in ElasticSearch. The approver will also import your visualization JSON file into the production Kibana instance.

## Support

Please [open an issue](https://github.com/ConservationInternational/vsvolunteer/issues/new) for support.