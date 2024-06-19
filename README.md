# Networking-Assignment
hero vired assignment on networking

Q1. Deploy a website on localhost using either apache2 or Nginx. Create a DNS name for this website as ‘awesomeweb’. You can use any web template you want or can write your own simple HTML code. 
Write the detailed documentation with steps involved.
<br>
Solution steps -
1. Install Apache2 / Nginx (I am installing nginx)
  > sudo apt-get update <br>
  > sudo apt-get install nginx
2. Include your html page for website - 'awesomeweb'
  > cd /var/www/html <br>
  > sudo vi index.html <br>
![image](https://github.com/garimas007/Networking-Assignment/assets/146625788/424f8a53-306e-4cec-a968-e785fdcd1d2b) <br>
3. Make changes to config file for hosting your website
  > cd /etc/nginx/sites-available <br>
  > sudo rm -rf default <br>
  > sudo vi awesomeweb <br>
![image](https://github.com/garimas007/Networking-Assignment/assets/146625788/54a51e18-2f85-401b-b001-2fbbbda9a8c8) <br>
4. Make changes to host file for DNS
  > sudo vi /etc/hosts
    - 127.0.0.1   awesomeweb <br>
  > sudo systemctl restart nginx <br>
5. View at 'http://awesomeweb' <br>
<img width="131" alt="image" src="https://github.com/garimas007/Networking-Assignment/assets/146625788/35f6990a-bafa-47bc-a613-fede990b485c"> <br>
<br>
<br>
Q2. A website can have many subdomains and different services are running on them. Write a Python script to check the status of the subdomains which are up or down. The script should automatically check the status every minute and should update it in tabular format on the screen.
Write documentation of it. <br>
Solution steps: -
1. Install python, pip, tabulate<br>
  > sudo apt-get install python3<br>
  > sudo apt install python3-pip<br>
  > pip install requests tabulate<br>
2. Write python script 'sudomaincheck.py' <br>
3. Output after runnung script <br>
<img width="196" alt="image" src="https://github.com/garimas007/Networking-Assignment/assets/146625788/d9f14894-ce0c-4d65-b22f-658c1772c5bc"> <br>
