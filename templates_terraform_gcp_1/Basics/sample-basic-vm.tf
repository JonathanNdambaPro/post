# Create a single Compute Engine instance
resource "google_compute_instance" "flask_app_1" {
  name         = var.vm_config.vm_name
  machine_type = var.vm_config.vm_type
  zone         = var.gcp_zone
  tags         = var.vm_config.vm_tags

  boot_disk {
    initialize_params {
      image = var.vm_config.vm_image
      size = var.vm_config.boot_disk_size
      type = "pd-standard"
    }
  }

  # Install Flask
  metadata_startup_script = var.vm_config.vm_startup_script

  network_interface {
    subnetwork = google_compute_subnetwork.subnet_1.id

    access_config {
      # Include this section to give the VM an external IP address
    }
  }

  scheduling {
    preemptible = true
    automatic_restart = false
    provisioning_model = "SPOT"
  }
}

resource "google_compute_network" "main_vpc" {
  name                    = "main-vpc"
  auto_create_subnetworks = var.vpc_auto_create_subnets
  mtu                     = var.vpc_mtu
}

resource "google_compute_subnetwork" "subnet_1" {
  name          = "subnet-1"
  ip_cidr_range = var.subnet_ip_range
  region        = var.gcp_region
  network       = google_compute_network.main_vpc.id
}
