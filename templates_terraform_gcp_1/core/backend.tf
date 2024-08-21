terraform {
	backend "gcs" {
    	bucket  = "YOUR-BACKEND-BUCKET" # CHANGE THIS
    	prefix  = "core/state"
        credentials = "PATH/TO/CREDENTIALS/FILE.JSON" # CHANGE THIS
	}
}
