#Simple Security Scanner - 
Because even the most secure systems need a good laugh

## Description
A security tool that's not afraid to have a little fun while performing various types of scans, including:
Features:

1) Scan for vulnerable printers - Scans for printers that have their guard down and may be vulnerable to exploitation. And who knows, maybe you'll even find a post-it with a funny joke on it.

2) Scan for Eternal Blue - Scans for hosts that have port 445 open, which is a common port for the infamous EternalBlue exploit. But hey, don't worry, we've got your back... and your front... and your sides.

3) Scan for passwordless SSH services - Scans for hosts that have port 22 open and may be running passwordless SSH services. It's like an open invitation to a party, but without the password!

4) Nmap fingerprint - Performs an Nmap OS fingerprinting scan to identify the operating system running on a device. You'll be prompted to enter a domain name for the scan, because who doesn't love a good game of "Guess the OS"?

5) Nmap subdomain enumeration - Performs an Nmap subdomain enumeration scan to list all the subdomains of a given domain. It's like a scavenger hunt, but with subdomains!

6) Nmap exif data spider - Performs an Nmap Exif data spider scan to extract metadata from image files that are accessible via HTTP on a given domain. Get ready for a wild ride of extracting metadata from image files!

7) Quit - Exits the program. But why would you want to leave all the fun behind?

## Usage

The user selects a scan option by entering a number, and the appropriate scan is executed. The results of the scan are displayed on the screen. The code makes use of several libraries, including os, sys, and subprocess. The code also uses the masscan and nmap tools to perform the scans. It's like a magician's hat, but with code!

## Note

This tool is for educational purposes only and should not be used for unauthorized purposes. The authors of this tool are not responsible for any unauthorized or illegal use of the tool. But let's be real, it's not like we're going to jail because you used it to scan your neighbor's printer for funny jokes.
