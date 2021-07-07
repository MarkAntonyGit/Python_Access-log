import pandas 
import matplotlib
import matplotlib.pyplot as plt
import logparser
import ipstack

#--------------------------------------------------------------
#  Function for Sorting
#--------------------------------------------------------------

def hits(t):
    return t[1]

#--------------------------------------------------------------
#  Counter for date and IP
#--------------------------------------------------------------

counter_Date = {} 
counter_IP   = {}


log = open('access.log')

for line in log: 
    logdict = logparser.parser(line)
    date    = logdict['time'][0:11]
    ip      = logdict['host']
    
    if date not in counter_Date:
        counter_Date[date] = 1
    else:
        counter_Date[date] = counter_Date[date] + 1
    
    if ip not in counter_IP:
        counter_IP[ip] = 1
    else:
        counter_IP[ip] = counter_IP[ip] + 1   


#--------------------------------------------------------------
#  To get top 20 Hits per Date and Hits per IP by sorting
#--------------------------------------------------------------

date_sort_all = sorted(counter_Date.items() , key=hits , reverse=True)          
date_sort = date_sort_all[0:20]

ip_sort_all = sorted(counter_IP.items() , key=hits , reverse=True)          
ip_sort = ip_sort_all[0:20]


#--------------------------------------------------------------
#  Counter for Hits per Country
#--------------------------------------------------------------

counter_country   = {}
country_dict      = {}

for item in ip_sort_all[0:100]:
    ip,hit = item
    country = ipstack.get_country(ip=ip,key="431c6bcfd46934f061fe1c59660e82d1")
    country_dict = {"ip": ip,
                  "hit": hit,
                  "country": country}  
    if country_dict['country'] not in counter_country:
        counter_country[country] = country_dict['hit']                                       
    else:
        counter_country[country] = counter_country[country] + country_dict['hit']


#--------------------------------------------------------------
#  For Plotting the Hits per Date 
#--------------------------------------------------------------

Date_List    = []
Date_Hitlist = []

for item in date_sort:
     Date_List.append(item[0])
     Date_Hitlist.append(item[1])
    
    
plt.rcParams["figure.figsize"] = (15, 5)
df = pandas.DataFrame({'Hits': Date_Hitlist} , index=Date_List)  
ax = df.plot.bar(rot=90)
plt.title(label="Hits per Date", fontsize=20, color="green")


#--------------------------------------------------------------
#  For Plotting the Hits per IP 
#--------------------------------------------------------------

IP_List      = []
IP_Hitlist   = []

for item in ip_sort:
     IP_List.append(item[0])
     IP_Hitlist.append(item[1])
    
 
plt.rcParams["figure.figsize"] = (15, 5)
df = pandas.DataFrame({'Hits': IP_Hitlist} , index=IP_List)  
ax = df.plot.bar(rot=90)
plt.title(label="Hits per IP", fontsize=20, color="red")

#--------------------------------------------------------------
# For Plotting the Hits per Country
#--------------------------------------------------------------

country_list = []
country_hits = []

for key in counter_country:
    country_list.append(key)
    country_hits.append(counter_country[key])


plt.rcParams["figure.figsize"] = (15, 5)
df = pandas.DataFrame({'Hits': country_hits} , index=country_list)  
ax = df.plot.bar(rot=90)
plt.title(label="Hits per Country", fontsize=20, color="blue")