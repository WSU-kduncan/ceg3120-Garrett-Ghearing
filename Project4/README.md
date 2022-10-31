# H1Project 4
- Objectives
- Project Description
  -  Provided Resources
- Part 1 - Cloud Formation Template TODOs
- Part 2 - Setup Load Balancing TODOs
- Resources and Warnings
- Submission
- Rubric
#Objectives:
Modify the CF template to meet updated requirements
Run a website of choice using nginx or apache2 on hosts in the pool
Configure the HAProxy load balancer to direct traffic to the pool
Project Description
In your repository, create a Project4 folder.

For this project, you will have two deliverables:

CloudFormation template that makes the recourses required for a load balancing setup: an application delivery controller (ADC) and two backend hosts in a pool.
Documentation for configuring the ADC and hosts. In order to visually check that load balancing is working, you will need to include screenshots that show different content
fetched from each server.
As mentioned in class, you are welcome to use your own website for this project. However in order to visually check that load balancing is working, you will need to include screenshots that show different content
fetched from each server. If you look at the html files provided, which you are welcome to use, you'll see that one has text that is is from server 1 and the other text that it is from server 2.

Provided Resources
The following is provided in this project folder:

cf-template.yml
Note: this templated is updated from previous versions to get you started on this project
index.srv1.html
Note: you can use your own webpage, but for this project you'll need the files to be "different" so that you can tell the content is coming from a different server
index.srv2.html
Part 1 - CloudFormation Template TODOs
The CloudFormation template provided in this project folder is updated from Project 3 to get you started on this project.

Sections you should pay attention to have comments with TODO

No really, go in there and do a "Find" for TODO
All said and done, your template should do the following:

Modify the Security Group Ingress rules to have the following additional rules:
Access HTTP from any IP address
I will allow trusted IPs if you're feeling shy
Access HTTP from within the VPC
For the HAProxy instance:
install haproxy
For the pool of content servers:
create two total backend host instances
one is created already as a template to refer to
attach them to the private subnet
the private subnet is already configured to route traffic through the NAT gateway
assign each instance a unique private IP within the private subnet
install webserver of choice on each instance
apache2 or nginx is fine
on each instance, change the hostname and Tag name to be unique for each system
The deliverable for this part is the CloudFormation template in your Project 4 folder.

Part 2 - Setup Load Balancing TODOs
Using the instances created by your CloudFormation template, setup the following and add documentation or screenshots to your README.md file as specified.

Create an /etc/hosts OR .ssh/config file on each system that correlates hostnames to private IPs of systems within the subnet (your instances).
Description of how file is configured
Document how to SSH in between the systems utilizing their private IPs.
HAProxy configuration & documentation requirements
How to set up a HAProxy load balancer
What file(s) where modified & their location
What configuration(s) were set (if any)
How to restart the service after a configuration change
Resources used (websites)
Webserver 1 & 2 configuration & documentation requirements
How set up a webserver
What file(s) were modified & their location
What configuration(s) were set (if any)
Where site content files were located (and why)
How to restart the service after a configuration change
Resources used (websites)
From the browser, when connecting to the proxy server, take two screenshots.
one screenshot that shows content from "server 1"
one screenshot that shows content from "server 2"
(Optional) - link to your proxy so I can click it.
Resources and Warnings
You DO NOT need to mess with UFW rules. You may lock yourself out of SSH access.
You can have a maximum of FIVE Elastic IP Addresses and FIVE VPCs
To manage resources & keep costs down, you will need to delete your CloudFormation stack in between build & test
Note: feel free to share additional resources over in Discord. I'll be updating this if I see you guys sharing something useful
An Introduction to HAProxy and Load Balancing Concepts
The Four Essential Sections of an HAProxy Configuration
How to Install the Apache Web Server on Ubuntu 20.04
How to Install Nginx on Ubuntu 20.04
How to edit /etc/hosts
The SSH config file
How to SFTP
Submission
Commit and push your changes to your repository. Verify that these changes show in your course
repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

Your repo should contain:
YOURLASTNAME-cf.yml
README.md
In Pilot, paste the link to your project folder.
Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project4
