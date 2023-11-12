# XML-RPC Scanner and Brute Force Tool

## Description
This Python script is designed to identify the presence of the xmlrpc.php file in WordPress installations and perform a variety of actions through XML-RPC requests. The tool supports both detection mode, to identify the existence of xmlrpc.php, and brute-force attacks against the WordPress login using XML-RPC.

## Features
  - Detection Mode: Identifies the presence of xmlrpc.php on a given WordPress site.
  - Brute Force: Conducts a brute force attack on the WordPress login through XML-RPC using provided usernames and passwords.
  - XML-RPC Methods: Supports various XML-RPC methods to interact with the WordPress site, including system.listMethods, system.getCapabilities, demo.sayHello, pingback.ping, and specific WordPress methods like wp.deleteFile, wp.uploadFile, wp.getAuthors, wp.editProfile,   wp.getProfile, wp.getUsers, wp.getPosts, wp.getPost, wp.deletePost, and wp.getUsersBlogs.

## Usage
python xmlrpc_scanner.py --url https://example.com/xmlrpc.php/ [options]

## Options 
Options
  --url: URL of the target WordPress site (e.g., https://example.com/xmlrpc.php/).
  -d or --detection: Activate detection mode.
  -m or --method: Specify the XML-RPC method to execute.
  -u or --user: Username for XML-RPC requests.
  -p or --password: Password for XML-RPC requests.
  -L or --luser: List of usernames for brute-force attack.
  -P or --lpassword: List of passwords for brute-force attack.
  Additional options for specific XML-RPC methods (e.g., --source_url, --target_url, --id_blog, --file_path, --file_name, --file_type, --num_posts, --post_id).

## Example
### Detection Mode
python xmlrpc_scanner.py --url https://example.com/xmlrpc.php/ -d

### Brute Force
python xmlrpc_scanner.py --url https://example.com/xmlrpc.php/ -m bruteforce -u admin -P password.txt

### Execute XML-RPC Method
python xmlrpc_scanner.py --url https://example.com/xmlrpc.php/ -m wp.getPosts -u admin -p password

## Note
The script requires the requests library, which can be installed using pip install requests.
Use this tool responsibly and only on systems you have permission to test.

## Disclaimer
This tool is intended for educational and security testing purposes only. Unauthorized access to computer systems, networks, and data is illegal. Use this tool at your own risk and only with explicit permission. The developers are not responsible for any misuse or damage caused by this script.
