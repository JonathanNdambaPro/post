variable "project_id" {
  description = "The ID of the project where the VM will be provisioned"
  type = string
}

variable "vm_name" {
  description = "The name of the VM without prefix or suffix"
  type = string
}

variable "vm_name_suffix" {
  description = "The suffix of the VM's name to be added at the end of the VM name"
  type = string
}

variable "vm_type" {
  description = "The type of the VM according to Google's convention (such as f1-micro, e2-standard, etc...)"
  type = string
}

variable "vm_gcp_zone" {
  description = "The zone where the VM will be created"
  type = string
}

variable "vm_tags" {
  description = "List of the network tags that will be assigned to the VM"
  type = list(string)
  nullable = true
  default = null
}

variable "vm_labels" {
  description = "The labels to be assigned on the VM"
  type = map(string)
  nullable = true
  default = null
}

variable "vm_metadata" {
  description = "The metadata values to be added on the VM"
  type = map(string)
  nullable = true
  default = null
}

variable "vm_image" {
  description = "Name of the OS image to be used by the VM boot disk"
  type = string
  default = "debian-cloud/debian-11"
}

variable "vm_boot_disk_size" {
  description = "The size of the boot disk of the VM"
  type = number
  default = 10
}

variable "vm_boot_disk_type" {
  description = "The type of the boot disk for the VM (pd-standard, pd-balanced or pd-ssd)"
  type = string
  default = "pd-standard"
}

variable "vm_subnetwork_id" {
  description = "The ID of the subnetwork to be used with the VM"
  type = string
}

variable "vm_service_account_email" {
  description = "The email address of the service account that will be used by the VM"
  type = string
  default = ""
}

variable "vm_service_account_scopes" {
  description = "The list of the scopes to be enabled for the VM's service account"
  type = list(string)
  default = [
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring.write",
      "https://www.googleapis.com/auth/pubsub",
      "https://www.googleapis.com/auth/service.management.readonly",
      "https://www.googleapis.com/auth/servicecontrol",
      "https://www.googleapis.com/auth/trace.append",
    ]
}

variable "vm_provisioning_model" {
 description = "The provisioning mode of the VM (STANDARD or SPOT)"
 type = string
 default = "STANDARD"
}
