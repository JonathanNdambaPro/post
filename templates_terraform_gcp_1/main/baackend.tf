terraform {
  backend "gcs" {
    bucket      = "YOUR-BACKEND-BUCKET"  # CHANGE THIS
    prefix      = "main-env/state"
    credentials = "PATH/TO/CREDENTIALS/FILE.JSON" # CHANGE THIS
  }
}
