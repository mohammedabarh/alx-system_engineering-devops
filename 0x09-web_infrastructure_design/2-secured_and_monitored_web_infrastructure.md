ecured and Monitored Web Infrastructure

## Diagram
![Secured and Monitored Web Infrastructure Diagram](https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)

## Design Overview
This infrastructure adds security and monitoring features to the distributed setup.

### Components
1. **Firewalls**
   - Three firewalls protect against unauthorized access.

2. **SSL Certificate**
   - Enables HTTPS to encrypt data in transit, enhancing security.

3. **Monitoring Clients**
   - Tools that collect data for performance monitoring (e.g., Sumologic).

### Key Concepts
- **Purpose of Firewalls**: Protect the network by filtering incoming and outgoing traffic.
- **HTTPS**: Secures data transmission between the user and the server.
- **Monitoring Usage**: Tracks performance metrics and alerts on anomalies.
- **QPS Monitoring**: To monitor queries per second, tools can analyze server logs.

### Issues
- **SSL Termination**: Terminating SSL at the load balancer can expose sensitive data if not configured correctly.
- **Single Write MySQL Server**: Having only one MySQL server for writes can create a bottleneck.
- **Same Components on All Servers**: This can lead to inefficiencies and complicate load balancing.

## URL
Repo: https://github.com/mohammedabarh/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png
Directory: 0x09-web_infrastructure_design
File: 2-secured_and_monitored_web_infrastructure
