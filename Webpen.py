import requests

# Check HTTP response
def http_response(url):
    print("HTTP Response Code:", requests.get(url).status_code)

# Find admin panels
def admin_finder(url, paths):
    for path in paths:
        if requests.get(url + path).status_code == 200:
            print("Admin panel found:", url + path)

# SQL Injection detection
def sql_check(url):
    if "error" in requests.get(url + "'").text:
        print("Vulnerable to SQL Injection")

# XSS testing
def xss_test(url):
    if "<script>" in requests.get(url + "?q=<script>").text:
        print("Vulnerable to XSS")

# Subdomain scanning
def subdomain_scan(domain, subdomains):
    for sub in subdomains:
        if requests.get(f"http://{sub}.{domain}").status_code == 200:
            print("Subdomain found:", sub + "." + domain)

def main():
    print("Website Pentesting Toolkit")
    while True:
        print("\n1. Check HTTP response")
        print("2. Find admin panels")
        print("3. Test for SQL Injection")
        print("4. Test for XSS vulnerability")
        print("5. Scan subdomains")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            url = input("Enter URL: ")
            http_response(url)
        elif choice == "2":
            url = input("Enter base URL: ")
            paths = input("Enter admin paths (comma-separated): ").split(',')
            admin_finder(url, paths)
        elif choice == "3":
            url = input("Enter URL: ")
            sql_check(url)
        elif choice == "4":
            url = input("Enter URL: ")
            xss_test(url)
        elif choice == "5":
            domain = input("Enter domain: ")
            subdomains = input("Enter subdomains (comma-separated): ").split(',')
            subdomain_scan(domain, subdomains)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()