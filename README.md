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
