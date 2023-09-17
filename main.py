import requests
import re

myRequest = requests.get('https://hellhades.com/champions-sitemap.xml') #Goes to the requested website and retrieves all data on the webpage
print(myRequest) #Prints html status code
content = str(myRequest.content) #Converts all data into one large string

#This creates the bounds of the list of champion links
main_limit_1 = 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
main_limit_2 = '</urlset>'

main_limit_index_1 = content.index(main_limit_1) #Lower Index
main_limit_index_2 = content.index(main_limit_2) #Upper Index

content_result = content[main_limit_index_1 + len(main_limit_1) : main_limit_index_2] 
split_content_result = content_result.split('\\n') #Splits the data into seperate rows using newline
link_list = [] #Initializes array for links

#Adds entries to new array only if it contains a link
for index in range(len(split_content_result)):
    #print(split_content_result[index],"\n")
    if "https://hellhades.com/champions" in split_content_result[index]:
        link_list.append(split_content_result[index])

#Gets rid of useless data on the sides of each link
for index in range(len(link_list)):
    link_list[index] = link_list[index].replace("\\t\\t<loc>","")
    link_list[index] = link_list[index].replace("</loc>","")
    #print(link_list[index])

#Further breaks down the list of links into a list of champion names and capitalizes every word
champion_list = []

for index in range(len(link_list)):
    champion_list.append(link_list[index].replace("https://hellhades.com/champions/",""))
    champion_list[index] = champion_list[index].replace("/","")
    champion_list[index] = champion_list[index].replace("-"," ")
    champion_list[index] = champion_list[index].title()   
    #print(champion_list[index])

#Defines a 2d array to add the information of the champions into
champion_table = []

for index in range(len(link_list)):
    champion_table.append([])
    champion_table[index].append(champion_list[index])
    champion_table[index].append(link_list[index])
    print(champion_table[index])

