# BApp1 Cloud SQL DB user password
resource "google_secret_manager_secret" "bapp1_cloud_sql_db_user_pass" {
  project   = module.proj_sec_bapp1_prod_0.project_id
  secret_id = "secret-bapp1-cloudsql-db-pass"

  labels = {
    env      = "prod"
    app-name = var.business_app_1_app_vm_config.short_app_name
  }

  replication {
    user_managed {
      replicas {
        location = "us-central1"
      }
      replicas {
        location = "europe-west1"
      }
    }
  }

  depends_on = [
    module.proj_sec_bapp1_prod_0
  ]
}
