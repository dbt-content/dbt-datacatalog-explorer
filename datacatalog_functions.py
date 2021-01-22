from google.cloud import datacatalog
from datetime import datetime

key_path="<path to Google service account json key file>"
datacatalog_client = datacatalog.DataCatalogClient.from_service_account_json(key_path)

def get_datacatalog_object_tags(dbt_model,dbt_project,dbt_cloud_job,dbt_cloud_project,gcp_project,dbt_tag_template):

	datacatalog_objects_tags=[]

	bq_objects = get_dbt_objects(dbt_model,dbt_project,dbt_cloud_job,dbt_cloud_project,gcp_project,dbt_tag_template)

	for bq_object in bq_objects:

		tag=get_tags_object(bq_object.relative_resource_name,dbt_tag_template)

		run_timestamp=tag.fields['dbt_run_timestamp'].timestamp_value
		run_date = datetime.combine(date=run_timestamp.date(), time=run_timestamp.time(), tzinfo=run_timestamp.tzinfo).strftime("%d/%m/%Y %H:%M")

		object_items=bq_object.linked_resource.split('/')

		object_tag = {
			"object": {
				"relative_resource_name":bq_object.relative_resource_name,
				"dataset":object_items[6],
				"name":object_items[8]
			},
			"tag":tag,
			"run_date":run_date
		}

		datacatalog_objects_tags.append(object_tag)

	return datacatalog_objects_tags


def get_dbt_objects(dbt_model,dbt_project,dbt_cloud_job,dbt_cloud_project,gcp_project,dbt_tag_template):

	scope = datacatalog.SearchCatalogRequest.Scope()
	scope.include_project_ids.append(gcp_project)

	if dbt_project:
		query='tag:'+dbt_tag_template+'.dbt_project_name:'+dbt_project
	elif dbt_model:
		query='tag:'+dbt_tag_template+'.dbt_model_name:'+dbt_model
	elif dbt_cloud_job:
		query='tag:'+dbt_tag_template+'.dbt_job_name:'+dbt_cloud_job
	elif dbt_cloud_project:
		query='tag:'+dbt_tag_template+'.dbt_cloud_project_name:'+dbt_cloud_project
	else:
		query='tag:'+dbt_tag_template
	
	bq_objects = datacatalog_client.search_catalog(scope=scope, query=query)
	
	return(bq_objects)


def get_tags_object(object_entry_name,dbt_tag_template):

	for tag in datacatalog_client.list_tags(parent=object_entry_name):

		if dbt_tag_template in tag.template:
	
			return(tag)

	return None
