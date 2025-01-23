import json
import logging
from node_metrics_collector import get_node_metrics

logging.basicConfig(filename="scheduler_logs/logs.txt", level=logging.INFO)

def compute_energy_cost(task, node):
    """Compute energy cost for running the task on the given node."""
    metrics = node['metrics']
    return task['cpu'] * metrics['cpu_power'] + task['mem'] * metrics['mem_power']

def schedule_task(task, nodes):
    """Find the best node for a task based on energy cost."""
    best_node = None
    min_cost = float('inf')
    for node in nodes:
        energy_cost = compute_energy_cost(task, node)
        if energy_cost < min_cost and node['metrics']['load'] < 0.8:  # Ensure node isn't overloaded
            min_cost = energy_cost
            best_node = node
    return best_node

def main():
    with open("task_profiles.json", "r") as file:
        tasks = json.load(file)

    nodes = get_node_metrics()

    for task in tasks:
        best_node = schedule_task(task, nodes)
        if best_node:
            logging.info(f"Scheduled task {task['name']} on node {best_node['name']}.")
        else:
            logging.warning(f"No suitable node found for task {task['name']}.")

if __name__ == "__main__":
    main()
