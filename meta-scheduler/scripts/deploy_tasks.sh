#!/bin/bash
# Apply Kubernetes manifests for each task
kubectl apply -f ../data-processing-task/k8s/kubernetes.yaml
kubectl apply -f ../ml-task/k8s/kubernetes.yaml
kubectl apply -f ../simulation-task/k8s/kubernetes.yaml
