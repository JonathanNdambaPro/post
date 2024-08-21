# Service account - Business app 1
resource "google_service_account" "sa_vm_bapp1" {
  project      = module.proj_infra_bapp1_prod_0.project_id
  account_id   = "SA-ACCOUNT-ID"
  display_name = "SA DISPLAY NAME"
  description  = "Service account to attafch to the VMs of BApp 1 application."

  depends_on = [
    module.proj_infra_bapp1_prod_0
  ]
}

# Service account - bapp1-cleaner CF
resource "google_service_account" "sa_cf_bapp1_cleaner" {
  project      = module.proj_infra_bapp1_prod_0.project_id
  account_id   = "SA-ACCOUNT-ID" # CHANGE THIS
  display_name = "SA DISPLAY NAME"
  disabled     = true

  depends_on = [
    module.proj_infra_bapp1_prod_0
  ]
}

# UNCOMMENT IF YOU WANT TO CREATE KEYS
# Service account key - bapp1-cleaner CF
#resource "google_service_account_key" "sa_cf_bapp1_cleaner_key" {
#  service_account_id = google_service_account.sa_cf_bapp1_cleaner.name
#
#  depends_on = [
#    google_service_account.sa_cf_bapp1_cleaner
#  ]
#}

# UNCOMMENT IF YOU WANT TO DOWNLOAD KEYS
# REALLY BAD IDEA
#
# Service account key FILE export - bapp1-cleaner CF
#resource "local_file" "sa_cf_bapp1_cleaner_key_file" {
#  filename = "outputs/${google_service_account.sa_cf_bapp1_cleaner.account_id}.json"
#  content  = base64decode(google_service_account_key.sa_cf_bapp1_cleaner_key.private_key)
#
#  depends_on = [
#    google_service_account_key.sa_cf_bapp1_cleaner_key
#  ]
#}
