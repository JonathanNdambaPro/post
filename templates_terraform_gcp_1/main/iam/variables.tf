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
