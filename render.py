#imports
import os
from statyc_settings import settings
from markdown2 import markdown
from shutil import copytree, rmtree

#gets information from statyc_settings.py
baseURL = settings.baseURL + "/index.html"
siteTitle = settings.title
siteSubTitle = settings.subtitle
siteAuthor = settings.author
siteCopyrightInfo = settings.copyright
theme = settings.theme

#initializes a string in which the page will be stored
page = ""

#gets the working directory
dir = os.getcwd()

#opens the head template and inserts the site name
file = open(dir + "/themes/%s/templates/head.html" % theme, 'r')
head = file.read()
file.close()
head = head.format(title = siteTitle)
#appends the new head to the page
page += head

#opens the header template and inserts the site title and subtitle
file = open(dir + "/themes/%s/templates/header.html" % theme, 'r')
header = file.read()
file.close()
header = header.format(title = siteTitle, subtitle = siteSubTitle)
#appends the new head to the page
page += header

#gets list of files
files = os.listdir(dir + "/in/posts/")
#sorts the list of files
sortedFiles = sorted(files)
#reverses the list (latest comes first)
sortedFiles.reverse()


#loop to parse each blog post
for filename in sortedFiles:
    print(filename)

    #opens the post template
    file = open(dir + "/themes/%s/templates/article.html" % theme, 'r')
    postTemplate = file.read()
    file.close()

    #opens the body markdown and saves it to a variable
    file = open(dir + "/in/posts/" + filename, 'r')
    post = file.readlines()
    file.close()

    #extracts post information from the post
    articleName = filename
    articleName = articleName.strip(".md")

    postName = post[0]
    postAuthor = post[1]
    postDate = post[2]
    postContent = post[3:]
    postContent = ''.join(postContent)

    #converts the body markdown to html
    contentHTML = markdown(str(postContent), extras=['fenced-code-blocks'])


    #formats the post template using info
    renderedPost = postTemplate.format(articleName = articleName, articleTitle = postName, articleAuthor = postAuthor, articleDate = postDate, articleContent = contentHTML)

    #appends the body to the page
    page += renderedPost

#opens the footer template and inserts the name and copyright info
file = open(dir + "/themes/%s/templates/footer.html" % theme, 'r')
footer = file.read()
file.close()
footer = footer.format(author = siteAuthor, copyright = siteCopyrightInfo)
#appends the footer to the rest of the page
page += footer

#gets rid of the /docs folder for the new files to be copied
if os.path.isdir(dir + "/docs"):
    rmtree(dir + "/docs")
#copies the static resources from the specific theme to the /docs folder
fromDir = "themes/%s/static" % theme
toDir = dir + "/docs"
copytree(fromDir, toDir)
print("copied!")

#creates and writes the rendered page to the "out" folder
file = open(dir + "/docs/index.html", 'w')
file.write(page)
file.close()

