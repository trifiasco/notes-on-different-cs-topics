
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


