# business-app-1 TCP HC
resource "google_compute_health_check" "business_app_1_hc_igm" {
  name    = "hc-tcp-8888-${var.business_app_1_app_vm_config.short_app_name}-0"
  project = module.proj_infra_bapp1_prod_0.project_id

  timeout_sec         = 15
  check_interval_sec  = 15
  healthy_threshold   = 2
  unhealthy_threshold = 3

  tcp_health_check {
    port = "8888"
  }

  depends_on = [
    module.proj_infra_bapp1_prod_0
  ]
}
