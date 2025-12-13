import requests
from github import Github
from config import apiKeys as cfg # modules imported
 
apiKey = cfg ["aprivateone"] # my private key

g = Github(apiKey)

repo = g.get_repo("lmacakova/api_integrations") # chosen repository

fileInfo = repo.get_contents("text.txt") # chosen file
# Chosen file
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile) # content of file
newContent = "Jana" # write something new
print (newContent) # new content
gitHubResponse=repo.update_file(fileInfo.path,"update_github", newContent, fileInfo.sha) # commit
print (gitHubResponse) 

