# Python_Access-log
Python program to analyze access log and plot details as graphs. 

# Description

Here I have created a python script to analyze access_log and plot the hits per IP, date and country using the matplotlib and pandas modules. The script also uses two other custom modules, logparser and ipstack , which I have uploaded in this repository. The script analyze the access_log with respect to hits per IP, hits per date and hits per country. 

### Hits per IP

Here the script uses a for loop to iterate through the access log line by line and counts the hits per IP and stores it in a dictionary. The logparser module is used for organizing the log into necessary fields. Later this result is sorted and plotted with the help of matplotlib module. The graph will show the top 20 IP details.

### Hits per Date

Here the script will gets the hits based on date and store it on another dictionary. The results are plotted with 20 dates with highest hits. 

### Hits per Country

Here I have used another module named ipstack, which have a function to make api calls to [ipstack](https://ipstack.com/) and get the country detail of the IP. Here if different IP's of same orgin country is detected in the access_log the hits to the IP's are added and used this detail to plot another graph based on it. 

## How to use

```
1. Install Python and Jupyter

# yum install python3 python3-pip -y
# pip3 install jupyter
# systemctl reboot

2. Clone this Repo to your server
# git clone https://github.com/MarkAntonyGit/Python_Access-log.git
# cd Python_Access-log

3. Add your access_log in this directory or mention the location in the "log = open('access.log')" section of the code.

4. Open Jupyter notebook and run the code.
```

This is it! You will be able to see the graphs based on Hits per date, IP and country. You can also make simple modifications to the script for getting any specific details from access_log

### Sample Screenshots

![](https://raw.githubusercontent.com/MarkAntonyGit/MarkAntonyGit/main/Uploads/Python/G1.JPG)

![](https://raw.githubusercontent.com/MarkAntonyGit/MarkAntonyGit/main/Uploads/Python/G2.JPG)

![](https://raw.githubusercontent.com/MarkAntonyGit/MarkAntonyGit/main/Uploads/Python/G3.JPG)

### Connect with me

--------<img src="https://img.shields.io/badge/-Mark%20Antony-brightgreen"/> ----------------------------------------------------------------------------------------------------------------------------------- <a href="https://www.linkedin.com/in/profile-markantony/"><img src="https://img.shields.io/badge/-Linkedin%20Profile-blue"/></a> ------------------------------------------------------------------------------------------------------------------------------------ <a href="mailto:markantony.alenchery@gmail.com"><img src="https://img.shields.io/badge/-markantony.alenchery@gmail.com-D14836?style=flat&logo=Gmail&logoColor=white"/></a>-------------------------------------------------------
