# AWS Compute

### Sample app architecture
```
traffic --> ELB(elastic load balancer) --> EC2 --> S3
                                            |
                                            |
                                            /\
                                           /  \
                                          /    \
                                        RDS  DynamoDB 
```  

Services - 
1. EC2 - Elastic Compute Cloud - Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure and resizable compute capacity in the cloud. It's designed to make web-scale cloud computing easier for developers.

    Amazon EC2 presents a true virtual computing   environment, and it allows you to use web service    interfaces to launch instances with a variety of      operating systems, load them with your custom   application environment, manage your network’s   access permissions, and run your image by using as   many or few systems as you want.
    
    Details on the features and cost of Amazon EC2 are     available at: https://aws.amazon.com/ec2/
2. lightsail - Amazon Lightsail is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a simple virtual private server (VPS) solution. Lightsail provides developers compute, storage, and networking capacity, and it also provides capabilities to deploy and manage websites and web applications in the cloud. Lightsail includes everything you need to launch your project quickly--a virtual machine, solid state drive (SSD)-based storage, data transfer, Domain Name System (DNS) management, and a static IP--for a low, predictable monthly price.

    A more detailed introduction from AWS re:Invent 2017    is available here: https://www.youtube.com/watch?  v=29_LqYnomdg. Note that pricing has changed  (decreased) since this video was created. Specific   details are on the Lightsail web page.
    
    Details on Lightsail and the 30 day trial are   available at: https://aws.amazon.com/lightsail/
    
    Lightsail pricing can be found here: https://   aws.amazon.com/lightsail/pricing
3. Lambda - AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume--there is no charge when your code isn't running. Additional information about Lambda can be found at: https://aws.amazon.com/lambda
4. Container Services
    - Elastic Container Services (ECS) - Amazon Elastic Container Service (Amazon ECS) is a highly scalable, high-performance container orchestration service that supports Docker containers. It allows you to run and scale containerized applications on AWS. You can find more details at: https://aws.amazon.com/ecs/
    - ECS for kubernetes (EKS) - Amazon Elastic Container Service for Kubernetes (Amazon EKS) makes it straightforward to deploy, manage, and scale containerized applications that use Kubernetes on AWS. Details can be found at: https://aws.amazon.com/eks/
    - Fargate - AWS Fargate is a compute engine for Amazon ECS and Amazon EKS that allows you to run containers without having to manage servers or clusters. You can find more information at: https://aws.amazon.com/fargate/