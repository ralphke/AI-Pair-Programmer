"""
import os

# Get a dictionary of all environment variables
env_vars = os.environ

# Print each environment variable and its value
for key, value in env_vars.items():
    print(f"{key}: {value}")
"""
import sys

# Get the path to the site-packages directory
site_packages_path = next(p for p in sys.path if 'site-packages' in p)

print(f"Packages are installed in: {site_packages_path}")