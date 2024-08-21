# business-app-1 bastion host
resource "google_compute_instance" "bapp_1_bastion_host_vm" {
  project      = module.proj_infra_bapp1_prod_0.project_id
  name         = "vm-${var.business_app_1_bastion_host_vm_config.vm_name}-prod-0"
  machine_type = var.business_app_1_bastion_host_vm_config.vm_type
  zone         = var.gcp_zone
  tags         = var.business_app_1_bastion_host_vm_config.vm_tags

  labels = {
    environment    = "prod"
    app-name       = var.business_app_1_bastion_host_vm_config.app_name
    app-short-name = var.business_app_1_bastion_host_vm_config.short_app_name
    vm-role        = "app"
  }

  metadata = {
    enable-os-login = "true"
  }

  boot_disk {
    initialize_params {
      image = var.business_app_1_bastion_host_vm_config.vm_image
      size  = var.business_app_1_bastion_host_vm_config.boot_disk_size
      type  = var.business_app_1_bastion_host_vm_config.vm_boot_disk_type
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_prod_0_usw1.id
  }

  service_account {
    scopes = [
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring.write",
      "https://www.googleapis.com/auth/pubsub",
      "https://www.googleapis.com/auth/service.management.readonly",
      "https://www.googleapis.com/auth/servicecontrol",
      "https://www.googleapis.com/auth/trace.append",
    ]
  }

  scheduling {
    preemptible        = true
    automatic_restart  = false
    provisioning_model = "SPOT"
  }

  lifecycle {
    ignore_changes = [
      scheduling[0].instance_termination_action
    ]
  }

  depends_on = [
    google_compute_shared_vpc_service_project.vpc_hub_prod_0_service_0,
    module.proj_infra_bapp1_prod_0
  ]
}
