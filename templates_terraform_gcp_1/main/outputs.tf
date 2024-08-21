output "proj_infra_bapp1_prod_0_number" {
  value = module.proj_infra_bapp1_prod_0.number
}

output "proj_infra_bapp1_prod_0_project_id" {
  value = module.proj_infra_bapp1_prod_0.project_id
}

output "proj_net_hub_prod_0_number" {
  value = module.proj_net_hub_prod_0.number
}

output "proj_net_hub_prod_0_project_id" {
  value = module.proj_net_hub_prod_0.project_id
}

output "bapp_1_public_url" {
  value = google_compute_managed_ssl_certificate.business_app_1_cert.managed[0].domains[0]
}

output "cloud_sql_instance_internl_ip" {
  value = google_sql_database_instance.cloud_sql_instance_bapp_1_prod.private_ip_address
}

output "cloud_sql_instance_connection_name" {
  value = google_sql_database_instance.cloud_sql_instance_bapp_1_prod.connection_name
}

output "cloud_sql_app_db_name" {
  value = google_sql_database.cloud_sql_app_db_bapp_1_prod.name
}
