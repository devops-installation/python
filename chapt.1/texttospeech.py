import pyttsx4

engine = pyttsx4.init()
engine.say(''' As a Cloud Operational engineer at Jio Platforms Limited (OPL) in India, I was responsible for ensuring the smooth operation of cloud infrastructure and services.
This includes maintaining and troubleshooting servers, managing virtual machines, and implementing security protocols. 

I also collaborated with cross-functional teams to optimize cloud Designed and implemented a continuous integration and delivery (CI/CD) pipeline using Jenkins and Docker. 
Write Nginx configurations for load balancing and reverse proxy, enhancing application performance and reliability.  
Designed and deployed AWS cloud infrastructure using services such as EC2, Auto Scaling, and Load Balancers, IAM policies and VPC configurations, ensuring high availability and fault tolerance for critical applications.  Deployment of backend Nodejs API on Docker and frontend react framework on Nginx webserver.

Optimize Nginx configurations for load balancing and reverse proxy enhancing application performance and reliability. 
Configured and deployed MongoDB databases, optimizing performance and ensuring data integrity and security.  Conducted regular database backups and implemented disaster recovery strategies, minimizing data loss risks in case of failures''')
engine.runAndWait()