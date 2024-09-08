PHONY: redirect_local_host_kubeflow install_kind_mac install_k8s_mac check_install_k8s deploy_kubeflow

install_kind_mac:
	brew install kind

install_k8s_mac:
	brew install kubernetes-cli

check_install_k8s:
	kubectl version --client --output=yaml

create_cluster_mlewp:
	kind create cluster --name mlewp

deploy_kubeflow:
	bash deploy_kubeflow_pipelines.zsh

redirect_local_host_kubeflow:
	kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
