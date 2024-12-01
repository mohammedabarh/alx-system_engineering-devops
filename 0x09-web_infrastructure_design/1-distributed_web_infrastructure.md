stributed Web Infrastructure

## Diagram
https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png

## Design Overview
This infrastructure includes multiple servers to distribute the load and improve availability.

### Components
1. **Servers**
   - Two servers to handle requests and improve redundancy.

2. **Web Server (Nginx)**
   - Distributes incoming HTTP requests to application servers.

3. **Application Server**
   - Processes application logic and interacts with the database.

4. **Load Balancer (HAproxy)**
   - Distributes traffic across multiple servers using algorithms like round-robin.

5. **Database (MySQL)**
   - Stores data in a Primary-Replica setup for failover and load distribution.

### Key Concepts
- **Distribution Algorithm**: The load balancer can be configured to use round-robin or least connection methods.
- **Active-Active vs. Active-Passive**: Active-active means both servers handle traffic, while active-passive has one server as a backup.
- **Primary-Replica Cluster**: The primary node handles writes, while replicas handle read requests.

### Issues
- **SPOF**: If the load balancer fails, the entire system may go down.
- **Security**: Lack of firewalls and HTTPS exposes the system to vulnerabilities.
- **No Monitoring**: Without monitoring, performance issues may go unnoticed.

## URL
Repo: https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png
Directory: 0x09-web_infrastructure_design
File: 1-distributed_web_infrastructurei
