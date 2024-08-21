# Random suffix for the template name
resource "random_string" "random_suffix" {
  length  = 5
  special = false
  upper   = false

  keepers = {
    app_version = "${var.business_app_1_app_vm_config.app_version}"
  }
}

# business-app-1 VMs instance template
resource "google_compute_instance_template" "business_app_1_app_vm_template" {
  project      = module.proj_infra_bapp1_prod_0.project_id
  name         = "templ-${var.business_app_1_app_vm_config.short_app_name}-${random_string.random_suffix.result}"
  machine_type = var.business_app_1_app_vm_config.vm_type
  region       = var.gcp_region

  tags = var.business_app_1_app_vm_config.vm_tags

  labels = {
    environment    = "prod"
    app-name       = var.business_app_1_app_vm_config.app_name
    app-short-name = var.business_app_1_app_vm_config.short_app_name
    role           = "app"
  }

  disk {
    source_image = var.business_app_1_app_vm_config.vm_image
    auto_delete  = true
    boot         = true
    disk_type    = var.business_app_1_app_vm_config.vm_boot_disk_type
    disk_size_gb = var.business_app_1_app_vm_config.boot_disk_size

    labels = {
      disk-type = "boot"
      app-name  = var.business_app_1_app_vm_config.app_name
    }
  }

  metadata = {
    startup-script-url = "gs://${google_storage_bucket.business_app_1_bucket.name}/${google_storage_bucket_object.business_app_1_app_startup_script.name}"
    enable-os-login    = "true"
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_prod_0_usw1.id
  }

  service_account {
    email  = google_service_account.sa_vm_bapp1.email
    scopes = ["cloud-platform"]
  }

  scheduling {
    preemptible        = true
    automatic_restart  = false
    provisioning_model = "SPOT"
  }

  lifecycle {
    create_before_destroy = true
    ignore_changes = [
      disk[0].resource_policies,
      network_interface[0].queue_count,
      scheduling[0].instance_termination_action,
      scheduling[0].min_node_cpus,
    ]
  }

  depends_on = [
    module.proj_infra_bapp1_prod_0,
    google_compute_shared_vpc_service_project.vpc_hub_prod_0_service_0
  ]
}
