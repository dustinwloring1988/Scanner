# Simple Security Scanner

A security tool to perform various types of scans, including:

## Features:

    1) Scan for vulnerable printers
        Scans for printers that are running on port 9100 and may be vulnerable to exploitation.
    2) Scan for Eternal Blue
        Scans for hosts that have open port 445, which is a common port for the EternalBlue exploit.
    3)Scan for passwordless SSH services
        Scans for hosts that have open port 22 and may be running passwordless SSH services.
    4) Nmap fingerprint
        Performs an Nmap OS fingerprinting scan to identify the operating system running on a device. You will be prompted to enter a domain name for the scan.
    5) Nmap subdomain enumeration
        Performs an Nmap subdomain enumeration scan to list all the subdomains of a given domain. You will be prompted to enter a domain name for the scan.
    6) Nmap exif data spider
        Performs an Nmap Exif data spider scan to extract metadata from image files that are accessible via HTTP on a given domain. You will be prompted to enter a domain name for the scan.
    Quit
        Exits the program.

## Usage

The user selects a scan option by entering a number, and the appropriate scan is executed. The results of the scan are displayed on the screen. The code makes use of several libraries, including os, sys, and subprocess. The code also uses the masscan and nmap tools to perform the scans.

## Note

This tool is for educational purposes only and should not be used for unauthorized purposes. The authors of this tool are not responsible for any unauthorized or illegal use of the tool.
Dustin Loring
can you use markup language

Sure! Here's an updated version of the previous response using GitHub-flavored Markdown:
Simple Security Scanner

A security tool to perform various types of scans, including:
Features:

    Scan for vulnerable printers
        Scans for printers that are running on port 9100 and may be vulnerable to exploitation.
    Scan for Eternal Blue
        Scans for hosts that have open port 445, which is a common port for the EternalBlue exploit.
    Scan for

