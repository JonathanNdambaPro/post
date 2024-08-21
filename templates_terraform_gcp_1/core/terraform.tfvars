project_id = "YOUR-CORE-PROJECT-ID" # CHANGE THIS
credentials_file = "PATH/TO/CREDENTIALS/FILE.JSON" # CHANGE THIS
gcp_region = "us-west1"
gcp_zone = "us-west1-a"

core_tf_project_services = [
    "cloudbilling.googleapis.com",
    "billingbudgets.googleapis.com",
    "sqladmin.googleapis.com",
    "servicenetworking.googleapis.com",
    "iam.googleapis.com"
]
