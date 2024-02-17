import requests
from lxml import html
import sys
import urllib.parse

# Check if the required arguments are provided
if len(sys.argv) != 3:
    print("Usage: python dorking.py <subdomain_list> <dork_list>")
    sys.exit(1)

# Open the subdomain list and dork list files
with open(sys.argv[1], 'r') as subdomains_file:
    subdomains = [line.strip() for line in subdomains_file.readlines()]

with open(sys.argv[2], 'r') as dorks_file:
    dorks = [line.strip() for line in dorks_file.readlines()]

# Define the Google Dork query
query = "site:{}"

# Loop through each subdomain and dork
for subdomain in subdomains:
    for dork in dorks:
        # Construct the URL with the subdomain and dork
        url = query.format(urllib.parse.urljoin(subdomain, "/")) + " " + dork

        # Send a request to the Google search page with the URL
        response = requests.get("https://www.google.com/search", params={"q": url})

        # Check if the request was successful
        if response.status_code == 200:
            # Print the subdomain and dork
            print(f"Subdomain: {subdomain}\nDork: {dork}\n")

            # Parse the HTML content
            tree = html.fromstring(response.content)

            # Extract the search result links
            links = tree.xpath('//div[@class="g"]/div[@class="rc"]/div[@class="r"]/a/@href')

            # Print the search result links
            for link in links:
                print(f"Link: {link}\n")
        else:
            print(f"Error: Failed to fetch results for {url}")

