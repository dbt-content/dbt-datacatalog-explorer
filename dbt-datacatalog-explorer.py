
from flask import Flask, request,render_template,Markup
from datacatalog_functions import get_datacatalog_object_tags

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    gcp_project="dbt-test-301310"
    dbt_metadata_tag_template="dbt_metadata"

    dbt_model=""
    dbt_project=""
    dbt_cloud_job=""
    dbt_cloud_project=""
    datacatalog_objects_tags=[]

    if request.method == 'POST':
        dbt_model=request.form['dbt_model']
        dbt_project=request.form['dbt_project']
        dbt_cloud_job=request.form['dbt_cloud_job']
        dbt_cloud_project=request.form['dbt_cloud_project']
        datacatalog_objects_tags=get_datacatalog_object_tags(dbt_model,dbt_project,dbt_cloud_job,dbt_cloud_project,gcp_project,dbt_metadata_tag_template)

    return render_template('home.html',datacatalog_objects_tags=datacatalog_objects_tags,dbt_model=dbt_model,dbt_project=dbt_project,dbt_cloud_job=dbt_cloud_job,dbt_cloud_project=dbt_cloud_project,gcp_project=gcp_project)