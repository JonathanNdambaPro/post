module "bapp_1_bastion_host_vm" {
  source = "./modules/vms"

  project_id     = module.proj_infra_bapp1_prod_0.project_id
  vm_name        = var.business_app_1_bastion_host_vm_config.vm_name
  vm_name_suffix = "prod-0"
  vm_gcp_zone    = var.gcp_zone
  vm_type        = var.business_app_1_bastion_host_vm_config.vm_type
  vm_tags        = var.business_app_1_bastion_host_vm_config.vm_tags
  vm_labels = {
    environment    = "prod"
    app-name       = var.business_app_1_bastion_host_vm_config.app_name
    app-short-name = var.business_app_1_bastion_host_vm_config.short_app_name
    vm-role        = "app"
  }
  vm_subnetwork_id = google_compute_subnetwork.subnet_prod_0_usw1.self_link

  vm_image          = var.business_app_1_bastion_host_vm_config.vm_image
  vm_boot_disk_size = var.business_app_1_bastion_host_vm_config.boot_disk_size
  vm_boot_disk_type = var.business_app_1_bastion_host_vm_config.vm_boot_disk_type

  vm_provisioning_model = "SPOT"
  vm_metadata = {
    enable-os-login = "true"
  }
}
