# Google Cloud Data Catalog Explorer for dbt Tags


A simple Web application to explore BigQuery tables and views tagged in [Google Cloud Data Catalog](https://cloud.google.com/data-catalog/) with a [dbt](https://www.getdbt.com/) tag.

<img src="https://github.com/dbt-content/dbt-datacatalog-explorer/blob/main/static/dbt_datacatalog_explorer.png" width="50%" height="50%">

This application search all BigQuery tables and views in Google Cloud Data Catalog with a dbt metadata tag. You can also filter the request with dbt Project, dbt Model, dbt Cloud Job or dbt Cloud Project.

Learn how to update or create dbt tags on Google Cloud Data Catalog entries (BigQuery tables or view) here https://github.com/dbt-content/google-datacatalog-dbt-tag.

This Web application uses <a href="https://flask.palletsprojects.com/" target="_blank">Python Flask Web framework</a> and <a href="https://googleapis.dev/python/datacatalog/latest/index.html#" target="_blank">Python Client for Google Cloud Data Catalog API</a> to search in Data Catalog.

Python source code using Data Catalog API can be found in [datacatalog_functions.py](https://github.com/dbt-content/dbt-datacatalog-explorer/blob/main/datacatalog_functions.py) file.

## Installation

* Clone this repo

      git clone https://github.com/dbt-content/dbt-datacatalog-explorer.git
      
* Install the requirements (in a virtual environment)

      pip install -r requirements.txt

If need more details on Flask framework installation and configuration, [see here](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Running

1/ Update the **key_path** parameter in [datacatalog_functions.py](https://github.com/dbt-content/dbt-datacatalog-explorer/blob/main/datacatalog_functions.py) Python file. This parameter set your <a href="https://googleapis.dev/python/google-api-core/latest/auth.html#service-accounts" target="_blank">service account json key file to authenticating to Google Cloud services</a>.

2/ Update the 2 parameters in [dbt-datacatalog-explorer.py](https://github.com/dbt-content/dbt-datacatalog-explorer/blob/main/dbt-datacatalog-explorer.py) Python file:

* **gcp_project**  : The GCP project where to search your BigQuery tables
* **dbt_metadata_tag_template** : The name (id) of the Dataprep metadata tag template

3/ Start the Flask Web app

In the Dataprep Explorer directory run:
```shell script
FLASK_APP=datataprep-datacatalog-explorer.py
flask run --port 5000
```
  
Now you must be able to go to http://127.0.0.1:5000/ and play with the application:
  
  ![alt tag](https://github.com/dbt-content/dbt-datacatalog-explorer/blob/main/Search_BigQuery_objects_with_dbt_Metadata_Tag.png)
