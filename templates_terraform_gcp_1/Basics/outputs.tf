output "vm_name" {
    value = google_compute_instance.flask_app_1.name
}

output "vm_internal_ip" {
    value = google_compute_instance.flask_app_1.network_interface[0].network_ip
}

output "vm_external_ip" {
    value = google_compute_instance.flask_app_1.network_interface[0].access_config[0].nat_ip
}

output "vm_zone" {
    value = google_compute_instance.flask_app_1.zone
}

output "vm_status" {
    value = google_compute_instance.flask_app_1.current_status
}
