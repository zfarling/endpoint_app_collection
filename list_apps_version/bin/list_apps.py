import os
import json
import platform
from configparser import ConfigParser

def get_splunk_apps_versions():
    # Determine the Splunk installation path
    splunk_home = os.environ.get("SPLUNK_HOME")
    if not splunk_home:
        return {"error": "SPLUNK_HOME environment variable is not set. Ensure the script is run on a Splunk instance."}

    apps_dir = os.path.join(splunk_home, "etc", "apps")
    if not os.path.exists(apps_dir):
        return {"error": f"Apps directory not found: {apps_dir}"}

    # Collect app names, labels, and versions
    apps_info = []
    for app_name in os.listdir(apps_dir):
        app_path = os.path.join(apps_dir, app_name)
        app_conf_path = os.path.join(app_path, "default", "app.conf")
        if os.path.exists(app_conf_path):
            config = ConfigParser()
            config.read(app_conf_path)
            version = config.get("launcher", "version", fallback="Unknown")
            label = config.get("ui", "label", fallback=app_name)
            apps_info.append({"App Name": app_name, "Label": label, "Version": version})

    return apps_info

def main():
    # Fetch the apps and versions with labels
    result = get_splunk_apps_versions()
    
    # Output the result in JSON format for Splunk consumption
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

