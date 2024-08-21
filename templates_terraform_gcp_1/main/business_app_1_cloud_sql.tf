# Data block for the DB password to use for the user in the Cloud SQL instance
data "google_secret_manager_secret_version" "bapp1_cloud_sql_db_user_pass_val" {
  project = module.proj_sec_bapp1_prod_0.project_id
  secret  = google_secret_manager_secret.bapp1_cloud_sql_db_user_pass.id
}

# Time sleep for 30 seconds to allow VPC peering to work
resource "time_sleep" "cloud_sql_delay_create_30s" {
  depends_on = [
    google_service_networking_connection.pvc_connection_0
  ]
  create_duration = "30s"
}

# The random_id value that will be added as a suffix to the Cloud SQL instance name
resource "random_id" "cloud_sql_instance_name_suffix" {
  byte_length = 4
}

# Cloud SQL instance configuration
resource "google_sql_database_instance" "cloud_sql_instance_bapp_1_prod" {
  project = module.proj_infra_bapp1_prod_0.project_id
  name    = "sql-${var.business_app_1_cloud_sql_config.short_app_name}-prod-${random_id.cloud_sql_instance_name_suffix.hex}"
  region  = var.gcp_region

  database_version = "MYSQL_5_7"

  settings {
    tier = var.business_app_1_cloud_sql_config.instance_tier

    disk_size       = var.business_app_1_cloud_sql_config.instance_disk_size
    disk_type       = var.business_app_1_cloud_sql_config.instance_disk_type
    disk_autoresize = var.business_app_1_cloud_sql_config.instance_disk_autoresize

    availability_type = var.business_app_1_cloud_sql_config.instance_availability_type

    backup_configuration {
      enabled            = true
      binary_log_enabled = true
      start_time         = "01:00"

      backup_retention_settings {
        retained_backups = 15
      }
    }

    ip_configuration {
      ipv4_enabled                                  = var.business_app_1_cloud_sql_config.instance_ipv4_enabled
      private_network                               = google_compute_network.vpc_hub_prod_0.id
      enable_private_path_for_google_cloud_services = true
    }

    user_labels = {
      environment    = "prod"
      app-name       = var.business_app_1_cloud_sql_config.app_name
      app-short-name = var.business_app_1_cloud_sql_config.short_app_name
      role           = "db"
    }

    deletion_protection_enabled = var.business_app_1_cloud_sql_config.instance_deletion_protection
  }

  depends_on = [
    time_sleep.cloud_sql_delay_create_30s
  ]
}

# The app database
resource "google_sql_database" "cloud_sql_app_db_bapp_1_prod" {
  name     = "${var.business_app_1_cloud_sql_config.short_app_name}_prod"
  project  = module.proj_infra_bapp1_prod_0.project_id
  instance = google_sql_database_instance.cloud_sql_instance_bapp_1_prod.name

  depends_on = [
    google_sql_database_instance.cloud_sql_instance_bapp_1_prod
  ]
}

# The app database user
resource "google_sql_user" "cloud_sql_app_db_bapp_1_prod_user" {
  name     = "bapp1dev"
  project  = module.proj_infra_bapp1_prod_0.project_id
  instance = google_sql_database_instance.cloud_sql_instance_bapp_1_prod.name
  host     = "%"
  password = data.google_secret_manager_secret_version.bapp1_cloud_sql_db_user_pass_val.secret_data

  depends_on = [
    google_sql_database_instance.cloud_sql_instance_bapp_1_prod
  ]
}
