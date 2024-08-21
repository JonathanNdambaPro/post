# Project resource
resource "google_project" "proj_infra_iam_test_0" {
  name            = "THE-PROJECT-ID" # CHANGE THIS
  project_id      = "THE-PROJECT-ID" # CHANGE THIS
  billing_account = var.billing_account
  folder_id       = google_folder.infrastructure.id

  depends_on = [
    google_folder.infrastructure
  ]
}

# Enabling the CRM API
resource "google_project_service" "proj_infra_iam_test_0_crm_service" {
  project                    = google_project.proj_infra_iam_test_0.id
  service                    = "cloudresourcemanager.googleapis.com"
  disable_dependent_services = true

  depends_on = [
    google_project.proj_infra_iam_test_0
  ]
}

# Enabling the remaining APIs and services
resource "google_project_service" "proj_infra_iam_test_0_services" {
  count                      = length(var.proj_infra_iam_test_0_services)
  project                    = google_project.proj_infra_iam_test_0.id
  service                    = var.proj_infra_iam_test_0_services[count.index]
  disable_dependent_services = true

  depends_on = [
    google_project_service.proj_infra_iam_test_0_crm_service
  ]
}
