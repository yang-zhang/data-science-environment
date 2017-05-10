# AWS 
- EC2 Configure Instance:
  - One default VPC has been created for each region you use.
  - One subnet corresponds to one availability zone.
  - Enable CloudWatch detailed monitoring (5-min to 1-min; additional charge)
  - A security group is a virtual firewall (DMZ)
    - Example name: "MyWebDMZ"
  - ssh (details [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)) 
    - Change permit for generated ssh key: `$ chmod 400 [pem file]`, e.g., `$ chmod 400 .ssh/MyEC2KeyPair.pem`
    - ssh command:
      - `$ ssh [user name]@[Public IP] -i [pem file]`, e.g.: `ssh ec2-user@52.91.36.218 -i .ssh/MyEC2KeyPair.pem`
      - `$ ssh [user name]@[Public DNS] -i [pem file]`, e.g., `ssh ec2-user@ec2-52-91-36-218.compute-1.amazonaws.com -i .ssh/MyEC2KeyPair.pem`
    - User name:
      - For Amazon Linux, the user name is ec2-user. 
      - For RHEL, the user name is ec2-user or root. 
      - For Ubuntu, the user name is ubuntu or root. 
      - For Centos, the user name is centos. 
      - For Fedora, the user name is ec2-user. 
      - For SUSE, the user name is ec2-user or root. 
      - Otherwise, if ec2-user and root don't work, check with your AMI provider.
- Example `run-instances` command: `aws ec2 run-instances --image-id ami-c58c1dd3 --count 1 --instance-type t2.micro --key-name MyEC2KeyPair --security-group-ids sg-c82ffeb6 --subnet-id subnet-cccf3784`
- [Script lab](https://acloud.guru/course/aws-certified-developer-associate/learn/ec2/663b39fd-2e74-1fe7-71be-30e3b4cec40a/watch)
  ```bash
  #!/bin/bash
  yum update -y
  yum install httpd -y
  service httpd start
  chkconfig httpd on
  aws s3 cp s3://mywebsitebucket/index.html /var/www/html/
  ```
### References
- [A Cloud Guru](https://acloud.guru)

