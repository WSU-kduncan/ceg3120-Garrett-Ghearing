# Project 4
- Objectives
- Project Description
  -  Provided Resources
- Part 1 - Cloud Formation Template TODOs
- Part 2 - Setup Load Balancing TODOs
- Resources and Warnings
- Submission
- Rubric
# Objectives:
- Modify the CF template to meet updated requirements
- Run a website of choice using nginx or apache2 on hosts in the pool
- Configure the HAProxy load balancer to direct traffic to the pool
# Project Description
In your repository, create a Project4 folder.

For this project, you will have two deliverables:

1. CloudFormation template that makes the recourses required for a load balancing setup: an application delivery controller (ADC) and two backend hosts in a pool.
2. Documentation for configuring the ADC and hosts. In order to visually check that load balancing is working, you will need to include screenshots that show different content fetched from each server.
As mentioned in class, you are welcome to use your own website for this project. However in order to visually check that load balancing is working, you will need to include screenshots that show different content
fetched from each server. If you look at the html files provided, which you are welcome to use, you'll see that one has text that is is from server 1 and the other text that it is from server 2.

## Provided Resources
The following is provided in this project folder:

- cf-template.yml
  - Note: this templated is updated from previous versions to get you started on this project
- index.srv1.html
  - Note: you can use your own webpage, but for this project you'll need the files to be "different" so that you can tell the content is coming from a different server
- index.srv2.html
# Part 1 - CloudFormation Template TODOs
The CloudFormation template provided in this project folder is updated from Project 3 to get you started on this project.

Sections you should pay attention to have comments with TODO

- No really, go in there and do a "Find" for TODO
All said and done, your template should do the following:

1. Modify the Security Group Ingress rules to have the following additional rules:
  - Access HTTP from any IP address
    - I will allow trusted IPs if you're feeling shy
  - Access HTTP from within the VPC
2. For the HAProxy instance:
  - install haproxy
3. For the pool of content servers:
  - create two total backend host instances
    - one is created already as a template to refer to
  - attach them to the private subnet
    - the private subnet is already configured to route traffic through the NAT gateway
  - assign each instance a unique private IP within the private subnet
  - install webserver of choice on each instance
    - apache2 or nginx is fine
  - on each instance, change the hostname and Tag name to be unique for each system
### The deliverable for this part is the CloudFormation template in your Project 4 folder.

# Part 2 - Setup Load Balancing TODOs
### Using the instances created by your CloudFormation template, setup the following and add documentation or screenshots to your README.md file as specified.

1. Create an /etc/hosts OR .ssh/config file on each system that correlates hostnames to private IPs of systems within the subnet (your instances).
  - I configured this part of the project by making a .ssh/config file i then edited the config file to inclused a Host Sever1 it also contained the private subnet ip to the specific sever and contained a user declared port 22 and told this file where to find my private key in the IdentityFile portion of this config 
2. Document how to SSH in between the systems utilizing their private IPs.
  - after setting up the .ssh/config file for both of my servers all i needed to do was ssh Sever1 or ssh Sever2 based on which server i was wanting to enter
3. HAProxy configuration & documentation requirements
  - How to set up a HAProxy load balancer
    - the files modified were /etc/haproxy/haproxy.cfg
    - The config changes that i set were in the haproxy.cfg file inside of this config file i had to add two things front end and backend configurations for the frontend i made it listen on port 80 and forward all users to the backend servers. next the backend server does the round robing server balancing it also contains the ips to these servers and is set to listen to port 80 as well. 
    - sudo systemctl restart haproxy 
    -  I used the two posted by you in the project 4 git repo and i used https://linuxhostsupport.com/blog/how-to-install-and-configure-haproxy-on-ubuntu/
## 4. Webserver 1 & 2 configuration & documentation requirements
  - How set up a webserver
    -What file(s) were modified and their location 
       - I added a directory mine was /var/www/connect then after this i made a file in it called index1.html i did this for both isntances
    - What configuration(s) were set (if any)
      - after creating the file and directory above I then needed to configure the apache2 and add new config files the next thing i did was create a new directory /etc/apache2/sites-avaiable/connect/index1.conf inside of this file i added a configuration of a virtual host on server 80 this includes the server, severname, documentroot(where the index1.html is. next I needed to set this as the default configuration in order to gain access to it so the sequence of commands i did was sudo a2ensite connect.conf after this command i did sudo a2dissite 000-deafult.conf the purpose of these two commnands where to make my conf file default after these i then ran sudo systemctl restart apache2 in order to update the config files. 
    - Where site content files were located (and why)
      - the site files were located inside /var/www/connect the ppurpose for them being located here is to keep it in a seperate directory this will allow you to be able to make multiple sites without needing more virtualhost systems for them to run in.
    - How to restart the service after a configuration change
      - sudo systemctl restart apache2
    - Resources used (websites)
      - for this i only used the resources provided by you 

5. From the browser, when connecting to the proxy server, take two screenshots.
  - one screenshot that shows content from "server 1"
    - I ran into a issue here i am unsure why I couldnt reach my sites I had correctly formed my haproxy and recieved no errors their I also quadrupled checked my secuirty rules they seem to have been fine as well. I checked my configurations for apache2 a lot and everything seemed fine the only issue I had was when i tried to restart my apache2 system it would ask for a password even with sudo or switching to root as my user. I thought that It still went through but I am unsure if it did. -    - so how did i try to solve this issue?
      - I attempted to solve this issue I was having by deleting my stack and restarting it from scratch i made sure to not look at my old resources so that way I would hopefully protect myself from accidentally duplicating the mistake that was causing this issue. however, this did not work after I got back to finishing the setup for my apache2 severs I had the same prompt arise.
      - After this I did some googling(should have done this first but i was extremely frustrasted and decided to nuke it). however googling my issue I came across many unhelpful articles all telling me to use sudo even though I was.
      - next I decided to look around the internet on how to do it all via command line from one instance to try to narrow down which instance was causing the issue i found a very helpful article to do this it is listed in (resources for haproxy). after following this succesfully i determiend that their was no errors inside of my proxy instance 
      - next I decided to go check the subnetting on my instances however it seemed all correct here as well specially considering I was able to ssh sever1 to go to server one and ssh server 2 to go to server2
      - after this I just accepted defat. however, it wasnt a complete waste i feel like I learned alot by researching my issue in an attempt to solve it. 
  - one screenshot that shows content from "server 2"
 6. (Optional) - link to your proxy so I can click it.
