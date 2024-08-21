terraform {
  backend "gcs" {
    bucket      = "YOUR-BACKEND-BUCKET" # CHANGE THIS
    prefix      = "main-iam/state"
    credentials = "PATH/TO/CREDENTIALS/FILE.JSON" # CHANGE THIS
  }
}
