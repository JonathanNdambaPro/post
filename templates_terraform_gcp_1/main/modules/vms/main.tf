# business-app-1 bastion host
resource "google_compute_instance" "default_vm" {
  project      = var.project_id
  name         = "${local.name_prefix}-${var.vm_name}-${var.vm_name_suffix}"
  machine_type = var.vm_type
  zone         = var.vm_gcp_zone
  tags         = var.vm_tags

  labels = var.vm_labels

  metadata = var.vm_metadata

  boot_disk {
    initialize_params {
      image = var.vm_image
      size  = var.vm_boot_disk_size
      type  = var.vm_boot_disk_type
    }
  }

  network_interface {
    subnetwork = var.vm_subnetwork_id
  }

  service_account {
    email = var.vm_service_account_email != "" ? var.vm_service_account_email : "${data.google_project.default_project_number.number}-compute@developer.gserviceaccount.com"
    scopes = var.vm_service_account_scopes
  }

  scheduling {
    preemptible        = var.vm_provisioning_model == "STANDARD" ? false : true
    automatic_restart  = var.vm_provisioning_model == "STANDARD" ? true : false
    provisioning_model = var.vm_provisioning_model
  }

  lifecycle {
    ignore_changes = [
      scheduling[0].instance_termination_action
    ]
  }
}
