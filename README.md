# google_dorking

# Overview
This Python script automates the process of performing Google Dork searches for specified subdomains and dorks. It efficiently constructs search queries, retrieves results, and extracts relevant links for further analysis.

# Key Features
Direct Subdomain Targeting: Pinpoints searches to specific subdomains for focused results.
Customizable Dork Lists: Supports various dorks for uncovering diverse vulnerabilities.
Streamlined HTML Parsing: ⚡️ Efficiently extracts links for immediate investigation.
Clear Error Handling: ⚠️ Provides informative messages for troubleshooting.

# Usage
Install Required Libraries:
pip install requests lxml

# Execute the Script:

python3 dorking.py <subdomain_list> <dork_list>

subdomain_list: A text file containing a list of subdomains, one per line.
dork_list: A text file containing a list of dorks, one per line.

# Example Output
Subdomain: example.com
Dork: intitle:login

Link: https://example.com/login.php
Link: https://example.com/admin/login.html
