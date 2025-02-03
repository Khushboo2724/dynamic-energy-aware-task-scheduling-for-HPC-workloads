# **Energy-Aware Meta-Scheduler for HPC on Kubernetes**

## **Overview**

This project focuses on optimizing **high-performance computing (HPC) workloads** using an **energy-aware meta-scheduler** in a **Kubernetes + Docker** environment. The scheduler intelligently assigns tasks—**data processing, machine learning (ML), and simulation**—based on real-time **energy and resource metrics** collected using **Prometheus**. The system enhances energy efficiency while maintaining performance across **microservices-based HPC environments**.

---

## **Project Structure**

```
📂 Energy-Aware-HPC-Scheduler/
│── 📂 container/                     # Contains all containerized tasks
│   ├── 📂 data-processing-task/      # Data processing workload container
│   ├── 📂 ml-task/                   # Machine learning workload container
│   ├── 📂 simulation-task/           # Simulation workload container
│── 📂 meta-scheduler/                # Intelligent energy-aware scheduler
│   ├── scheduler.py                  # Main scheduling logic
│   ├── node_metrics_collector.py     # Fetches real-time node metrics
│   ├── energy_model.py               # Energy consumption prediction
│── 📂 k8s-deployments/                # Kubernetes YAML manifests
│   ├── data-processing.yaml          # K8s deployment for data processing
│   ├── ml-task.yaml                  # K8s deployment for ML task
│   ├── simulation-task.yaml          # K8s deployment for simulation
│   ├── scheduler-deployment.yaml     # Meta-scheduler Kubernetes deployment
│── 📂 monitoring/                     # System monitoring setup
│   ├── prometheus-config.yaml        # Prometheus configuration
│── 📂 output/                         # Stores logs and results
│── requirements.txt                    # Python dependencies
│── README.md                           # Project documentation
│── setup.sh                            # Script to deploy all components
```

---

## **Key Features**

### **1. Containerized Workloads**

- **Data Processing Task**: Handles large-scale data transformations using Spark.
- **Machine Learning Task**: Trains models efficiently using TensorFlow/PyTorch.
- **Simulation Task**: Runs physics-based or computational simulations.

### **2. Meta-Scheduler**

- Uses **task-based scheduling** instead of simple round-robin or FIFO methods.
- Collects **real-time node energy consumption and resource metrics**.
- Adapts workload placement to **minimize energy waste** while optimizing performance.

### **3. Kubernetes Integration**

- Deploys all tasks and the scheduler as **Kubernetes Pods**.
- Uses **Prometheus** to collect system-wide metrics.
- Supports **scalability and efficient resource allocation** in cloud/HPC clusters.

---

## **Installation & Execution**

### **Step 1: Build and Run Docker Containers**

```sh
# Build container images
docker build -t hpc-data-processing:latest container/data-processing-task/
docker build -t hpc-ml-training:latest container/ml-task/
docker build -t hpc-simulation:latest container/simulation-task/
```

### **Step 2: Deploy Kubernetes Services**

```sh
# Deploy workloads and meta-scheduler in Kubernetes
kubectl apply -f k8s-deployments/data-processing.yaml
kubectl apply -f k8s-deployments/ml-task.yaml
kubectl apply -f k8s-deployments/simulation-task.yaml
kubectl apply -f k8s-deployments/scheduler-deployment.yaml
```

### **Step 3: Start Monitoring (Optional)**

```sh
# Deploy Prometheus for monitoring
kubectl apply -f monitoring/prometheus-config.yaml
# Forward Prometheus port to access metrics
kubectl port-forward svc/prometheus 9090:9090
```

---

## **Future Work**

✔️ **Dynamic Energy-Aware Scheduling**: Improve scheduling decisions with **machine learning models** for energy prediction.\
✔️ **Multi-Metric Optimization**: Optimize for **latency, throughput, and power consumption** simultaneously.\
✔️ **Support for GPU Workloads**: Extend scheduler capabilities to optimize GPU-based machine learning and simulations.\
✔️ **Adaptive Scaling**: Dynamically adjust the number of pods based on **real-time energy availability**.

---

