variable "project_id" {
    type = string
    description = "The project ID that I will be working with"
}

variable "credentials_file" {
    type = string
    description = "The JSON credential file to be used within the provider.tf file"
}

variable "gcp_region" {
    type = string
    description = "The primary GCP region to deploy the resources"
    default = "us-west1"
}

variable "gcp_zone" {
    type = string
    description = "The primary GCP zone within the region to be used"
    default = "us-west1-a"
}

variable "subnet_ip_range" {
    type = string
    description = "The IPv4 CIDR range to be used in the VPC that will be created"
    default = "10.0.1.0/24"
}

variable "vpc_auto_create_subnets" {
    type = bool
    description = "Defines the behavior for the VPC whether we want to use it in auto mode (true) or a custom VPC (false)"
    default = false
}

variable "vpc_mtu" {
    type = number
    description = "The value of the MTU for our new VPC"
    default = 1460
}

variable "vm_config" {
    description = "The VM configuration values and properties"
    type = object(
        {
            vm_name = string
            vm_type = string
            vm_tags = list(string)
            vm_image = string
            boot_disk_size = number
            vm_startup_script = string
        }
    )
    default = {
        vm_name = "flask-app-1"
        vm_type = "f1-micro"
        vm_tags = [ "ssh", "flask", "web-app" ]
        vm_image = "debian-cloud/debian-11"
        boot_disk_size = 10
        vm_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python3-pip rsync; pip install flask"
    }
}
