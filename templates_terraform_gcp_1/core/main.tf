resource "google_storage_bucket" "default" {
  name          = "${var.project_id}-bucket-tfstate"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}

# Enabling the CRM API
resource "google_project_service" "core_tf_project_crm_service" {
  project = var.project_id
  service = "cloudresourcemanager.googleapis.com"
  disable_dependent_services = true
}

# Enabling the remaining APIs and services
resource "google_project_service" "core_tf_project_services" {
  count = length(var.core_tf_project_services)
  project = var.project_id
  service = var.core_tf_project_services[count.index]
  disable_dependent_services = true
}

# IAM - Owner - tuser02
resource "google_project_iam_member" "core_tf_project_owner_tuser02" {
  project = var.project_id
  role = "roles/owner"
  member = "user:USER@EXAMPLE.COM" # CHANGE THIS
}
