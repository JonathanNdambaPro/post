# Internal VPC traffic for Business App 1 VMs
resource "google_compute_firewall" "business_app_1_internal_fw" {
  name        = "fw-${google_compute_network.vpc_hub_prod_0.name}-allow-local-tcp-in-${var.business_app_1_app_vm_config.short_app_name}"
  project     = module.proj_net_hub_prod_0.project_id
  network     = google_compute_network.vpc_hub_prod_0.name
  description = "Firewall rule to allow internal traffic between the bapp-1 VMs"

  direction = "INGRESS"

  source_ranges = [
    "${var.subnet_ip_range[0]}"
  ]

  target_tags = ["bapp1"]

  allow {
    protocol = "tcp"
  }

  allow {
    protocol = "udp"
  }

  allow {
    protocol = "icmp"
  }

  depends_on = [
    google_compute_network.vpc_hub_prod_0
  ]
}

# GCP health checks firewall rule
resource "google_compute_firewall" "business_app_1_health_checks_fw" {
  name        = "fw-${google_compute_network.vpc_hub_prod_0.name}-allow-health-checks-tcp-in-${var.business_app_1_app_vm_config.short_app_name}"
  project     = module.proj_net_hub_prod_0.project_id
  network     = google_compute_network.vpc_hub_prod_0.name
  description = "Firewall rule to allow the GCP health checks to reach the VMs"

  direction = "INGRESS"

  source_ranges = [
    "35.191.0.0/16",
    "130.211.0.0/22"
  ]

  target_tags = ["app-fe"]

  allow {
    protocol = "tcp"
    ports    = ["8888"]
  }

  depends_on = [
    google_compute_network.vpc_hub_prod_0
  ]
}

# GCP IAP IP ranges
resource "google_compute_firewall" "business_app_1_iap_fw" {
  name        = "fw-${google_compute_network.vpc_hub_prod_0.name}-allow-iap-tcp-in-${var.business_app_1_app_vm_config.short_app_name}"
  project     = module.proj_net_hub_prod_0.project_id
  network     = google_compute_network.vpc_hub_prod_0.name
  description = "Firewall rule to allow the GCP IAP IP range to reach the VMs"

  direction = "INGRESS"

  source_ranges = [
    "35.235.240.0/20"
  ]

  target_tags = ["iap"]

  allow {
    protocol = "tcp"
    ports = [
      "22",
      "3389",
      "3306"
    ]
  }

  depends_on = [
    google_compute_network.vpc_hub_prod_0
  ]
}
