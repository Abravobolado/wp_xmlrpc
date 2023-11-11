import base64
import requests, argparse, sys
import methods



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Ejemplo de script con argumentos.')
    
    # Add arguments
    parser.add_argument('--url', dest='url', required=True, help='URL to test. Example: https://xxxxxxxx.com/xmlrpc.php/')
    parser.add_argument('-d', '--detection', action='store_true', required=False, help='Detection mode activated')
    parser.add_argument('-m', '--method', dest='method', required=False, help='Method to request by xmlrpc.php')
    parser.add_argument('-u', '--user', dest='user', required=False, help='User to send for the request')
    parser.add_argument('-p', '--passwword', dest='password', required=False, help='Password to send for the request')
    parser.add_argument('-L', '--luser', dest='users', required=False, help='List of users to brute force')
    parser.add_argument('-P', '--lpasswword', dest='passwords', required=False, help='List of passwords to brute force')
    parser.add_argument('--source_url', dest='source_url', required=False, help='Source URL for the pingback')
    parser.add_argument('--target_url', dest='target_url', required=False, help='Target URL for the pingback')
    parser.add_argument('--id_blog', dest='id_blog', required=False, help='Id of the blog')
    parser.add_argument('--file_path', dest='file_path', required=False, help='Path where the file is')
    parser.add_argument('--file_name', dest='file_name', required=False, help='Name of the file')
    parser.add_argument('--file_type', dest='file_type', required=False, help='Type of the file. Example: image/jpeg')
    parser.add_argument('--num_posts', dest='num_posts', required=False, help='Maximum of posts to be shown')
    parser.add_argument('--post_id', dest='post_id', required=False, help='Id of the post to be shown')

    # Parse the arguments
    args = parser.parse_args()

    # Access argument values
    url = args.url
    method = args.method
    user = args.user
    password = args.password
    detection = args.detection
    users = args.users
    passwords = args.passwords

    if len(sys.argv) == 4:
        methods.detecction(url)

    elif method == "bruteforce":
        methods.bruteforce(url, users, passwords)

    elif method == "system.listMethods":
        methods.listMethods(url)

    elif method == "system.getCapabilities":
        methods.getCapabilities(url)

    elif method == "demo.sayHello":
        methods.sayHello(url)

    elif method == "pingback.ping":
        methods.pingBack(url,args)

    elif method == "wp.deleteFile":
        methods.deleteFile(url,args)

    elif method == "wp.uploadFile":
        methods.uploadFile(url,args)

    elif method == "wp.getAuthors":
        methods.getAuthors(url,args)

    elif method == "wp.editProfile":
        methods.editProfile(url,args)
    
    elif method == "wp.getProfile":
        methods.getProfile(url,args)

    elif method == "wp.getUsers":
        methods.getUsers(url,args)

    elif method == "wp.getPosts":
        methods.getPosts(url,args)
    
    elif method == "wp.getPost":
        methods.getPost(url,args)

    elif method == "wp.deletePost":
        methods.deletePost(url,args)

    elif method == "wp.getUsersBlogs":
        methods.getUsersBlogs(url,args)

    else:
        print(f"\033[91m[*]\033[0m Method {args.method} not supported")

    