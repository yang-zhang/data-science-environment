# AWS 
- EC2 Configure Instance:
  - One default VPC has been created for each region you use.
  - One subnet corresponds to one availability zone.
  - Enable CloudWatch detailed monitoring (5-min to 1-min; additional charge)
  - A security group is a virtual firewall
    - Example name: "MyWebDMZ"
  - ssh (details [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)) 
    - Change permit for generated ssh key: `$ chmod 400 .ssh/MyEC2KeyPair.pem`
    - ssh: `$ ssh ec2-user@[Public IP]52.91.36.218 -i .ssh/MyEC2KeyPair.pem`
    - User name:
      - For Amazon Linux, the user name is ec2-user. 
      - For RHEL, the user name is ec2-user or root. 
      - For Ubuntu, the user name is ubuntu or root. 
      - For Centos, the user name is centos. 
      - For Fedora, the user name is ec2-user. 
      - For SUSE, the user name is ec2-user or root. 
      - Otherwise, if ec2-user and root don't work, check with your AMI provider.
    


### References
- (A Cloud Guru)[https://acloud.guru]

