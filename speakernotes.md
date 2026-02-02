Hi my name is Ryan Arnzen
My project is called the smart home media server 

It is a self hosted Ubuntu server that replaces cloud storage and media services with my own private systems.

2:
Right now a lot of families have several subscriptions that they pay for monthly. I know my family has at least 6, but by hosting my own server, 
and not subscribing to a bunch of different cloud providers and streaming services. I can save hundrends a year, and I will have seamless access 
to all my data across my devices. 


3:
This project is majority software focused. 

I will be implementing my own
- personal cloud service
- media storage
- remote access  
- and system monitoring


---

4: How it works

 The system allows devices like phones, TVs, and laptops to connect through Cloudflare.
Cloudflare provides a secure tunnel that will hide my home IP so I don’t expose my network directly to the internet.
Inside my server, I run a reverse proxy container that routes requests to the correct service, such as Nextcloud or Jellyfin.

---
 
 5: Docker
 Docker is a way to package applications into containers
  each container will have its own
   - app 
   - dependicies
   - configuration
   
  So instead of installing everything directly to the OS I can run my services independantly 
 for example
  - One service for nextcloud
  - One for monitoring
  - one for reverse proxy 

---
  
 6:
Nextcloud and Jellyfin
Next cloud is the personal cloud storage
 - it will replace my google drive and icloud storage.
 
 It will allow me to
 - upload files
 - sync photos
 - share folders
 - acces from any device
   
 Jellyfin will 
 handle media streaming 
 Stores your media files
 Organizes them
 Serves them over the network
 Streams/transcodes them to devices

---

 
 7: Security
 For security we will be using cloudlfare proxy
 - this will allow for no public IP exposure
 - encrypted connections
 - built in protection from attacks    ----------- What protection?

 ---
 
 8: AI usage
 I plan on using AI to teach me the different technologies I will be implementing. 
 I have very little knowledge of system networking and AI will be a big help in understanding how to secure my system.
 I also don't have much knowledge with containers and using docker so it will also be teaching me that. 
 
 --------------------------
 
 9:
 Cotainer setup:
 My containers are structured like this:
 Nextcloud -> Storage
 Jellyfin -> media streaming
 Reverse proxy container -> handles network routing to route requests to the correct service.
 Future Iot container -> sensors/system handling.
 
 This means if ones service breaks it wont affect the others.

---
 
 Timeline:
 In the first phase I work on learning and udnerstanding how my system should be setup. 
 In the second phase I deploy and build the services. 
 
 
 10:
 Goals:
 By the end of the semester I want a fully working prototype with 
 - private cloud
 - media streaming
 - remote access
 - sys monitoring 
 - personal dvd ripper
 
