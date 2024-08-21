terraform {
	backend "gcs" {
    	bucket  = "backend_terraform_1"
    	prefix  = "terraform/state"
        credentials = "/Users/jojobizarre/.config/gcloud/application_default_credentials.json"
	}
}
