# Folder 'My GCP Env'
resource "google_folder" "my_gcp_env_root" {
  display_name = "My GCP Env"
  parent       = "organizations/${var.organization_id}"
}

# Folder 'Network'
resource "google_folder" "network" {
  display_name = "Network"
  parent       = google_folder.my_gcp_env_root.name

  depends_on = [
    google_folder.my_gcp_env_root
  ]
}

# Folder 'Infrastructure'
resource "google_folder" "infrastructure" {
  display_name = "Infrastructure"
  parent       = google_folder.my_gcp_env_root.name

  depends_on = [
    google_folder.my_gcp_env_root
  ]
}

# Folder 'Security'
resource "google_folder" "security" {
  display_name = "Security"
  parent       = google_folder.my_gcp_env_root.name

  depends_on = [
    google_folder.my_gcp_env_root
  ]
}
