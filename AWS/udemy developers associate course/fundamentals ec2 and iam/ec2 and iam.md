
## Fundamentals

### AWS Regions
- each one has availability zones(AZ) - represents physical data centers
- AZs are separate. 
- 1 Region has min of 3 AZ
- except IAM and s3 - each service depends on region

### IAM - Identity and Access Management
- users - physical person (1 IAM user per physical person)
- groups - functions(admins, devs) Teams(eng, design)
- roles - internal usage within aws resources(1 IAM role per application)

- Users must be created with proper permission.
- Policies are written in JSON.
- IAM has predefined `managed policies`

#### IAM federation ??? (SAML standard)

#### IAM hands on


### EC2
Has capability of:
    - Renting virtual machines (EC2)
    - Storing data on virtual drives(EBS)
    - distributing load across machines(ELB)
    - scaling the services using an auto scaling group(ASG)

#### Hands on - launching an EC2 instance

#### Access EC2 using SSH
- copy the public ip address(IPV4) from the aws console's ec2 instance
- place the key file (.pem file) in the directory.
- run `chmod 0400 <keyfile>.pem` >> makes the private key inaccessible
- run - `ssh -i <keyfile>.pem ec2-user@<IPV4>` , here [ec2-user] is the user in the ec2 instance

**PS-** In order to access the instance from `EC2 instance connect` from the browser, you need to have ssh configured and a port exposed. This is done while configuring or you can do it later from - 
- go to security group > edit inbound rule > give a port(22) and source as `anywhere`.


### Security Groups
- fundamental of network security in aws.

### Types of EC2 instances
**Very Important for exam**


