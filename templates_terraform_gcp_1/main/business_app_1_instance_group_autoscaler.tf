# business-app-1 Autoscaler settings
resource "google_compute_region_autoscaler" "business_app_1_igm_autoscaler" {
  project = module.proj_infra_bapp1_prod_0.project_id
  name    = "autoscaler-${google_compute_region_instance_group_manager.business_app_1_igm.name}"
  region  = var.gcp_region
  target  = google_compute_region_instance_group_manager.business_app_1_igm.id

  autoscaling_policy {
    max_replicas    = var.business_app_1_app_vm_config.autoscaler_max_replicas
    min_replicas    = var.business_app_1_app_vm_config.autoscaler_min_replicas
    cooldown_period = 120

    cpu_utilization {
      target = 0.5
    }
  }

  depends_on = [
    google_compute_region_instance_group_manager.business_app_1_igm
  ]
}
