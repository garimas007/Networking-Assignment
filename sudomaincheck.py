import requests
import time
from tabulate import tabulate

# List of subdomains to check
subdomains = [
    "http://52.87.237.134/",
    "http://52.87.237.134/page2",
    "http://52.87.237.134/page3"
]

def check_subdomain_status(subdomains):
    statuses = []
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain)
            if response.status_code == 200:
                statuses.append((subdomain, "Up"))
            else:
                statuses.append((subdomain, "Down"))
        except requests.RequestException:
            statuses.append((subdomain, "Down"))
    return statuses

def display_status_table(statuses):
    headers = ["Subdomain", "Status"]
    table = tabulate(statuses, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    while True:
        statuses = check_subdomain_status(subdomains)
        display_status_table(statuses)
        time.sleep(60)  # Wait for 1 minute before checking again