import random

def get_node_metrics():
    """Simulate node metrics. Replace with Prometheus or other monitoring data."""
    return [
        {"name": "node1", "metrics": {"cpu_power": 2.0, "mem_power": 1.5, "load": 0.4}},
        {"name": "node2", "metrics": {"cpu_power": 1.8, "mem_power": 1.2, "load": 0.6}},
        {"name": "node3", "metrics": {"cpu_power": 2.5, "mem_power": 1.8, "load": 0.5}}
    ]
