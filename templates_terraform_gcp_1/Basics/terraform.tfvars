project_id = "bank-425606"
credentials_file = "/Users/jojobizarre/.config/gcloud/application_default_credentials.json"
gcp_region = "us-west1"
gcp_zone = "us-west1-a"
subnet_ip_range = "10.0.1.0/24"
vpc_auto_create_subnets = false
vpc_mtu = 1460
vm_config = {
    vm_name = "flask-app-2"
    vm_type = "e2-micro"
    vm_tags = [ "ssh", "flask", "web-app", "python-311" ]
    vm_image = "debian-cloud/debian-11"
    boot_disk_size = 10
    vm_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python3-pip rsync; pip install flask"
}
