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


## Transcribe Data From Prosgres to ElasticSearch (ETL step)

In order to create a data visualization in Kibana, the data you wish to work with must be loaded into ElasticSearch. To do this, we typically use python scripts to query data from postgres and output it to ElasticSearch. The python script could be as simple as querying a few selected columns from a table, or it could be more complex and could programmatically aggregate and transform data.

See postgresToElasticSearch.py as an example.

## Creating Data Visualization in Kibana
After you run your python script, navigate to your local kibana instance and configure a visualization. Consult the [Kibana User Guide](https://www.elastic.co/guide/en/kibana/current/index.html) as needed.

When your visualization is complete, [export it to a JSON file](https://discuss.elastic.co/t/how-to-save-dashboard-as-json-file/24561/4).

Commit the JSON export file to your repository.

## Submit Pull Request
When you are satisfied with the python script and visualization JSON file, submit a pull request. If approved, your script will be added to the repository, the script will be executed, and the data you staged should become available in ElasticSearch. The approver will also import your visualization JSON file into the production Kibana instance.

## Support

Please [open an issue](https://github.com/ConservationInternational/vsvolunteer/issues/new) for support.