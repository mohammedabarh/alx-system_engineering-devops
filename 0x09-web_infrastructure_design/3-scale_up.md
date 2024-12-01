cale Up

## Diagram
![Scale Up Diagram](https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png)

## Design Overview
This infrastructure scales the application by splitting components across multiple servers.

### Components
1. **Server**
   - A dedicated server for the load balancer.

2. **Load Balancer (HAproxy)**
   - Configured in a cluster for high availability.

3. **Separated Components**
   - Separate servers for the web server, application server, and database to distribute the load.

### Key Concepts
- **Why Split Components?**: Enhances performance, scalability, and fault isolation.
- **Load Balancer Clustering**: Provides redundancy and ensures continuous availability.

## URL
Repo: [GitHub repository: alx-system_engineering-devops](https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png)
Directory: 0x09-web_infrastructure_design
File: 3-scale_up
