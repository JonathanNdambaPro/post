locals {
  name_prefix = "proj"
}

# Project resource
resource "google_project" "default_project" {
  name            = "${local.name_prefix}-${var.project_id}"
  project_id      = "${local.name_prefix}-${var.project_id}"
  billing_account = var.billing_account
  folder_id       = var.project_parent_folder
}

# Enabling the CRM API
resource "google_project_service" "default_project_crm_service" {
  project                    = google_project.default_project.id
  service                    = "cloudresourcemanager.googleapis.com"
  disable_dependent_services = true

  depends_on = [
    google_project.default_project
  ]
}

# Enabling the remaining APIs and services
resource "google_project_service" "default_project_services" {
  count                      = length(var.project_services_list)
  project                    = google_project.default_project.id
  service                    = var.project_services_list[count.index]
  disable_dependent_services = true

  depends_on = [
    google_project_service.default_project_crm_service
  ]
}

# Budget alert for the project
resource "google_billing_budget" "default_project_budget" {
  billing_account = var.billing_account
  display_name    = "budget-${google_project.default_project.project_id}"

  budget_filter {
    projects = ["projects/${google_project.default_project.number}"]
  }

  amount {
    specified_amount {
      currency_code = var.budget_currency
      units         = var.budget_amount
    }
  }

  threshold_rules {
    threshold_percent = 1.0
  }

  dynamic "threshold_rules" {
    for_each = var.budget_rules
    content {
      threshold_percent = threshold_rules.value.threshold_percent
      spend_basis = threshold_rules.value.spend_basis
    }
  }

  all_updates_rule {
    monitoring_notification_channels = [
      for channel in google_monitoring_notification_channel.default_project_notification_channel : channel.id
    ]
    disable_default_iam_recipients = true
  }

  depends_on = [
    google_project.default_project
  ]
}

# Project notification channels (email)
resource "google_monitoring_notification_channel" "default_project_notification_channel" {
  count = length(var.notification_emails)
  project      = google_project.default_project.project_id
  display_name = var.notification_emails[count.index]
  type         = "email"

  labels = {
    email_address = var.notification_emails[count.index]
  }

  depends_on = [
    google_project.default_project
  ]
}
