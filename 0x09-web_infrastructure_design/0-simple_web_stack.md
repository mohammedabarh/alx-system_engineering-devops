imple Web Stack

## Diagram
https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png

## Design Overview
In this simple web infrastructure, a user accesses the website `www.foobar.com`, which is hosted on a single server.

### Components
1. **Server**
   - A physical or virtual machine that hosts the web and application servers and the database.
   
2. **Web Server (Nginx)**
   - Serves HTTP requests and delivers web content to users.

3. **Application Server**
   - Executes the application code and processes user requests.

4. **Application Files**
   - The codebase containing the application logic and resources.

5. **Database (MySQL)**
   - Stores and manages data for the application.

6. **Domain Name**
   - `www.foobar.com` is configured with a DNS record pointing to the server IP `8.8.8.8`.

### DNS Record
- The `www` in `www.foobar.com` is a CNAME record that points to the server's IP address.

### Issues
- **Single Point of Failure (SPOF)**: If the server goes down, the website becomes inaccessible.
- **Downtime**: Maintenance or code deployment requires server restarts, resulting in downtime.
- **Scalability**: Limited ability to handle increased traffic without additional servers.

## URL
Repo: https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png
Directory: 0x09-web_infrastructure_design
File: 0-simple_web_stack
