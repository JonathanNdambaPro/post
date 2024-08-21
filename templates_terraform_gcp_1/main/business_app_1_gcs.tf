# GCS bucket
resource "google_storage_bucket" "business_app_1_bucket" {
  project                     = module.proj_infra_bapp1_prod_0.project_id
  name                        = "gcs-${module.proj_infra_bapp1_prod_0.project_id}-bapp1-scripts"
  location                    = "US"
  storage_class               = "STANDARD"
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  depends_on = [
    module.proj_infra_bapp1_prod_0
  ]
}

resource "time_sleep" "delay_create_30s" {
  depends_on = [
    google_storage_bucket.business_app_1_bucket
  ]
  create_duration = "30s"
}

# Startup script object
resource "google_storage_bucket_object" "business_app_1_app_startup_script" {
  name = "scripts/startup-script.sh"
  #source = "scripts/bapp-1/startup-script.sh"
  content = file("scripts/bapp-1/startup-script.sh")
  bucket  = google_storage_bucket.business_app_1_bucket.id

  depends_on = [
    time_sleep.delay_create_30s
  ]
}
