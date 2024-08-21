# Global IP Address for the app
resource "google_compute_global_address" "business_app_1_glb_ext_ip" {
  name    = "ip-ext-${var.business_app_1_app_vm_config.short_app_name}"
  project = module.proj_infra_bapp1_prod_0.project_id

  depends_on = [
    module.proj_infra_bapp1_prod_0,
    google_compute_network.vpc_hub_prod_0
  ]
}

# Managed SSL certificate
resource "google_compute_managed_ssl_certificate" "business_app_1_cert" {
  name    = "cert-${var.business_app_1_app_vm_config.short_app_name}"
  project = module.proj_infra_bapp1_prod_0.project_id

  managed {
    domains = [
      "${google_compute_global_address.business_app_1_glb_ext_ip.address}.nip.io"
    ]
  }

  depends_on = [
    google_compute_global_address.business_app_1_glb_ext_ip
  ]
}

# The backend service definition
resource "google_compute_backend_service" "business_app_1_backend_svc" {
  name                  = "besvc-${var.business_app_1_app_vm_config.short_app_name}"
  project               = module.proj_infra_bapp1_prod_0.project_id
  protocol              = "HTTP"
  port_name             = var.named_ports.bapp1.port_name
  load_balancing_scheme = "EXTERNAL_MANAGED"
  timeout_sec           = 30
  health_checks         = [google_compute_health_check.business_app_1_hc_glb.id]

  backend {
    group           = google_compute_region_instance_group_manager.business_app_1_igm.instance_group
    balancing_mode  = "UTILIZATION"
    max_utilization = 0.8
    capacity_scaler = 0.8
  }

  security_policy = google_compute_security_policy.bapp1_cloud_armor_owasp.name

  depends_on = [
    google_compute_region_instance_group_manager.business_app_1_igm
  ]
}

# URL map config
resource "google_compute_url_map" "business_app_1_url_map_0" {
  name    = "url-map-${var.business_app_1_app_vm_config.short_app_name}"
  project = module.proj_infra_bapp1_prod_0.project_id

  default_service = google_compute_backend_service.business_app_1_backend_svc.id

  host_rule {
    hosts        = ["*"]
    path_matcher = "allpaths"
  }

  path_matcher {
    name            = "allpaths"
    default_service = google_compute_backend_service.business_app_1_backend_svc.id

    path_rule {
      paths   = ["/"]
      service = google_compute_backend_service.business_app_1_backend_svc.id
    }
  }

  depends_on = [
    google_compute_backend_service.business_app_1_backend_svc
  ]
}

# Target proxy
resource "google_compute_target_https_proxy" "business_app_1_https_target_proxy" {
  name             = "target-proxy-https-${var.business_app_1_app_vm_config.short_app_name}"
  project          = module.proj_infra_bapp1_prod_0.project_id
  url_map          = google_compute_url_map.business_app_1_url_map_0.id
  ssl_certificates = [google_compute_managed_ssl_certificate.business_app_1_cert.id]

  depends_on = [
    google_compute_url_map.business_app_1_url_map_0,
    google_compute_managed_ssl_certificate.business_app_1_cert
  ]
}

# Global Forwarding Rule
resource "google_compute_global_forwarding_rule" "business_app_1_global_forwarding_rule" {
  name                  = "gfwr-${var.business_app_1_app_vm_config.short_app_name}"
  project               = module.proj_infra_bapp1_prod_0.project_id
  load_balancing_scheme = "EXTERNAL_MANAGED"
  target                = google_compute_target_https_proxy.business_app_1_https_target_proxy.id
  port_range            = 443
  ip_address            = google_compute_global_address.business_app_1_glb_ext_ip.id

  depends_on = [
    google_compute_target_https_proxy.business_app_1_https_target_proxy
  ]
}
