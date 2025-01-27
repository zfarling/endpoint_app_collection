List Apps and Versions
======================
This app scans the `etc/apps` directory of a Splunk host and lists all installed apps and their versions.

New Features:
- The app runs weekly and indexes app details into the `_internal` index with the sourcetype `splunk_apps`.

Installation:
- Install via Splunk UI or place the app in the `etc/apps` directory.

Usage:
- The data is indexed in `_internal` with the sourcetype `splunk_apps`.
- Use Splunk searches to analyze the data.

