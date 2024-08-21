provider "google" {
  project     = var.project_id
  credentials = file(var.credentials_file)
  region      = var.gcp_region
  zone        = var.gcp_zone
}
