module "proj_infra_iam_test_0" {
  source = "./modules/projects"
  project_id            = "THE-PROJECT-ID" # CHANGE THIS
  project_parent_folder = google_folder.infrastructure.id
  billing_account       = var.billing_account

  project_services_list = var.proj_infra_iam_test_0_services

  budget_amount = "50"
  budget_rules = var.project_budgets.default
  notification_emails = [
    "USER@EXAMPLE.COM", # CHANGE THIS
  ]

  depends_on = [
    google_folder.infrastructure
  ]
}

module "proj_infra_bapp1_prod_0" {
  source = "./modules/projects"
  project_id            = "THE-PROJECT-ID" # CHANGE THIS
  project_parent_folder = google_folder.infrastructure.id
  billing_account       = var.billing_account

  project_services_list = var.proj_infra_bapp1_prod_0_services

  budget_amount = "50"
  budget_rules = var.project_budgets.default
  notification_emails = [
    "USER@EXAMPLE.COM", # CHANGE THIS
  ]

  depends_on = [
    google_folder.infrastructure
  ]
}

module "proj_net_hub_prod_0" {
  source = "./modules/projects"
  project_id = "THE-PROJECT-ID" # CHANGE THIS
  project_parent_folder = google_folder.network.id
  billing_account = var.billing_account

  project_services_list = var.proj_net_hub_prod_0_services

  budget_currency = "USD"
  budget_amount = "50"
  budget_rules = var.project_budgets.proj_net_hub_prod_0

  notification_emails = [
    "USER@EXAMPLE.COM", # CHANGE THIS
  ]

  depends_on = [
    google_folder.network
  ]
}

module "proj_sec_bapp1_prod_0" {
  source = "./modules/projects"
  project_id            = "THE-PROJECT-ID" # CHANGE THIS
  project_parent_folder = google_folder.security.id
  billing_account       = var.billing_account

  project_services_list = var.proj_sec_bapp1_prod_0_services

  budget_amount = "10"
  budget_rules = var.project_budgets.default
  notification_emails = [
    "USER@EXAMPLE.COM", # CHANGE THIS
  ]

  depends_on = [
    google_folder.security
  ]
}
