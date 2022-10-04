Part1 - Build a VPC 

1. Create a VPC

![succes vpc](https://user-images.githubusercontent.com/70773439/193670729-8b316b2e-80a5-4a35-81d1-88b773ea87c0.PNG)

2. create a subnet

![succes subnet](https://user-images.githubusercontent.com/70773439/193670787-be9c816e-2b3b-4365-8262-a170eab21888.PNG)

3. Create a internet gateway

![internetgateway](https://user-images.githubusercontent.com/70773439/193670381-e1137ede-72fe-4fa3-a0f6-35a054c858d6.PNG)
![internet succes](https://user-images.githubusercontent.com/70773439/193670454-8f6a153f-a073-4ef5-ba70-03a2e1da1d5d.PNG)
![instance proof](https://user-images.githubusercontent.com/70773439/193670547-8879d2fa-71d2-4c25-b9c3-f4940b6e7b08.PNG)

4. create a route table 
![route table](https://user-images.githubusercontent.com/70773439/193670062-25c4df72-a902-48dc-949b-0f2d06691eb8.PNG)
![route table assoc](https://user-images.githubusercontent.com/70773439/193670104-2c0152bb-fc59-4c68-b58b-2ca063e9d806.PNG)
![route rule](https://user-images.githubusercontent.com/70773439/193670203-b4c6202b-e4d1-4b83-80f1-ed91adcecf1f.PNG)

5. create a secuirty group
 
![sg succes](https://user-images.githubusercontent.com/70773439/193669170-2db08745-45e1-415e-b2c2-5458ab69c64f.PNG)
![sg vpc assoc](https://user-images.githubusercontent.com/70773439/193669189-173bce3c-688c-411c-ae12-6369d40b29c0.PNG)
![SG i rule](https://user-images.githubusercontent.com/70773439/193669751-86f59dfd-4558-4619-b046-0c09049c4406.PNG)
![sg vpc assoc](https://user-images.githubusercontent.com/70773439/193669852-2c56e3d7-40a9-4083-9698-e8201c9973b2.PNG)


6 create a key pair

i did not need to do this 


part 2 - EC2 instances 

1. create a new instance Give a write up 
  
  the ami i setup was ubuntu mainly because it is what i am use to 
  the default username is ubuntu
  the instance type i selected was t2.micro

2. attach the instance to your VPC explain how you did it 
   
   i attached my instance to my vpc by going to the vpc section clicking the drop down menu then selecting Ghearing-VPC

3. Determine whether a public IPv4 address will be auto assigned and justify your choice 
  
  i decided to auto assign a IPv4 my reason to do this was just cut back the chance of me creating an error.
  this did not make assigning a elastic IP address any harder or anymore steps.

4. attach a volume to your instance as discussed there are diff pathways to doing this say how you did it

for selecting a volume for my instance what i did was find the section labeled configure storage and found the volume section I left everything default meaning i have 8 gigabyte reserved with gp2 

5. tag your instance with a "NAME" of "YOURLASTNAME-instance" say how you did this 

at the start of the creating instansce their was a category labled name & tags so their i set up the tag Ghearing-Instance.

6. associate your secuirty group and say how you did it

i did this by selecting "select existing secuirty group" I then clicked on ghearing=sg

7. reserve an associate an elastic IP address with your instance

i did this by going down the list on the left side until saw elastic IP i then added a tag and completed the build i then pressed actions and associated it with my instance  

![elasticIP](https://user-images.githubusercontent.com/70773439/193668717-559fc0ca-1a1e-4804-a866-53809e517847.PNG)
![associate eip](https://user-images.githubusercontent.com/70773439/193668743-c8841bf7-d69c-4dff-94e5-b3fca502e456.PNG)


8. snapshot of finished instance details

![part8](https://user-images.githubusercontent.com/70773439/193668603-31535bfd-ed14-42fb-b104-3dcc651690e9.PNG)

9 & 10

![proof i am in](https://user-images.githubusercontent.com/70773439/193723814-a04b2713-f972-41e0-9b03-3d3f3755f5c5.PNG)
![succesful copy](https://user-images.githubusercontent.com/70773439/193724093-63548b1e-0094-4c05-833f-e4dd7678949f.PNG)
![su![proof](https://user-images.githubusercontent.com/70773439/193723909-4f38a52e-fb04-48ce-8222-4ab3e1dfa6c6.PNG)
![succes](https://user-images.githubusercontent.com/70773439/193724230-0e13b3d3-aef3-4fe7-99d7-cd21b0aa8b2b.PNG)
