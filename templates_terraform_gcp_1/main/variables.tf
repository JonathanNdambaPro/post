variable "project_id" {
  type        = string
  description = "The project ID that I will be working with"
}

variable "credentials_file" {
  type        = string
  description = "The JSON credential file to be used within the provider.tf file"
}

variable "gcp_region" {
  type        = string
  description = "The primary GCP region to deploy the resources"
  default     = "us-west1"
}

variable "gcp_zone" {
  type        = string
  description = "The primary GCP zone within the region to be used"
  default     = "us-west1-a"
}

variable "subnet_ip_range" {
  type        = list(string)
  description = "The list of IPv4 CIDR ranges to be used in the VPC that will be created"
}

variable "vpc_auto_create_subnets" {
  type        = bool
  description = "Defines the behavior for the VPC whether we want to use it in auto mode (true) or a custom VPC (false)"
  default     = false
}

variable "vpc_mtu" {
  type        = number
  description = "The value of the MTU for our new VPC"
  default     = 1460
}

variable "business_app_1_app_vm_config" {
  description = "The app VM configuration values and properties"
  type = object(
    {
      app_name                = string
      short_app_name          = string
      vm_name                 = string
      vm_type                 = string
      vm_tags                 = list(string)
      vm_image                = string
      vm_boot_disk_type       = string
      boot_disk_size          = number
      vm_startup_script       = string
      autoscaler_min_replicas = number
      autoscaler_max_replicas = number
      app_version             = string
    }
  )
}

variable "business_app_1_bastion_host_vm_config" {
  description = "The bastion host VM configuration values and properties"
  type = object(
    {
      app_name          = string
      short_app_name    = string
      vm_name           = string
      vm_type           = string
      vm_tags           = list(string)
      vm_image          = string
      vm_boot_disk_type = string
      boot_disk_size    = number
      vm_startup_script = string
    }
  )
}

variable "business_app_1_cloud_sql_config" {
  description = "The Cloud SQL instance configuration values and properties"
  type = object(
    {
      app_name                     = string
      short_app_name               = string
      instance_tier                = string
      instance_disk_type           = string
      instance_disk_size           = number
      instance_disk_autoresize     = bool
      instance_availability_type   = string
      instance_ipv4_enabled        = bool
      instance_deletion_protection = bool
    }
  )
}

variable "organization_id" {
  type        = string
  description = "The value of the organization ID"
}

variable "billing_account" {
  type        = string
  description = "The ID of the billing account that I will be using for this environment"
}

variable "proj_net_hub_prod_0_services" {
  type        = list(string)
  description = "The list of the services that we want to enable in the GCP project"
}

variable "proj_infra_bapp1_prod_0_services" {
  type        = list(string)
  description = "The list of the services that we want to enable in the GCP project"
}

variable "proj_sec_bapp1_prod_0_services" {
  type        = list(string)
  description = "The list of the services that we want to enable in the GCP project"
}

variable "named_ports" {
  type = object({
    bapp1 = object({
      port_name   = string
      port_number = number
    })
  })
}

variable "proj_infra_iam_test_0_services" {
  type        = list(string)
  description = "The list of the services that we want to enable in the GCP project"
}

variable "cloud_armor_policies" {
  type = map(object({
    action      = string
    priority    = string
    preview     = bool
    expression  = string
    description = string
    })
  )
  description = "The list of Cloud Armor rules to be created"
}

variable "project_budgets" {
  type = map(map(object({
      threshold_percent = number
      spend_basis       = string
  })))
  description = "The budget rules for the projects that will be created"
}
