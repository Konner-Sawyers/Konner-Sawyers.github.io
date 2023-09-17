import requests
import re

myRequest = requests.get('https://hellhades.com/champions/kael/') #Goes to the requested website and retrieves all data on the webpage
print(myRequest) #Prints html status code
content = str(myRequest.content) #Converts all data into one large string
#content = "lol <try me>"

content = re.sub('<!DOC.+?Skills', '', content)
content = re.sub('Grading\\sis\\scalculated.+', '', content)
content = re.sub('Overall\\sGrading\\*:</span>\\s.+?</p>','break_here', content)
content = content.replace("b'",'')

content = content.replace("break_here",'\\n')
content_list = content.split('\\n')

for index in range(len(content_list)):
    content_list[index] = re.sub('<.+?>',' ',content_list[index])
    content_list[index] = re.sub(' +',' ',content_list[index])
    content_list[index] = content_list[index].strip()
    #print(content_list[index])

list_length = len(content_list)

for index in range(list_length-1,list_length-4,-1):
    content_list.pop(index)

parsed_content = []
for index in range(len(content_list)):
    first_word = content_list[index].split(' ')
    if (first_word[0] != 'Level' and first_word[0] != 'Aura'):
        print(first_word[0])
        #print(content_list[index])
        

#for index in range(len(content_list)):
#    print(content_list[index])
