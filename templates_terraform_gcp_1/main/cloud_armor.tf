# Cloud Armor security policiy and rules
resource "google_compute_security_policy" "bapp1_cloud_armor_owasp" {
  project = module.proj_infra_bapp1_prod_0.project_id
  name    = "casp-bapp1-owasp-top10"

  rule {
    action   = "allow"
    priority = "2147483647"
    match {
      versioned_expr = "SRC_IPS_V1"
      config {
        src_ip_ranges = ["*"]
      }
    }
    description = "default allow rule"
  }

  dynamic "rule" {
    for_each = var.cloud_armor_policies
    content {
      action   = rule.value.action
      priority = rule.value.priority
      match {
        expr {
          expression = rule.value.expression
        }
      }
      preview     = rule.value.preview
      description = rule.value.description
    }
  }
}
