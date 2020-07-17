#imports
import os
from statyc_settings import settings
from markdown2 import markdown

#gets information from statyc_settings.py
siteTitle = settings.title
siteSubTitle = settings.subtitle
siteAuthor = settings.author
siteCopyrightInfo = settings.copyright

#initializes a string in which the page will be stored
page = ""

#gets the working directory
dir = os.getcwd()

#opens the head template and inserts the site name
file = open(dir + "/templates/head.html", 'r')
head = file.read()
file.close()
head = head.format(title = siteTitle)
#appends the new head to the page
page += head

#opens the header template and inserts the site title and subtitle
file = open(dir + "/templates/header.html", 'r')
header = file.read()
file.close()
header = header.format(title = siteTitle, subtitle = siteSubTitle)
#appends the new head to the page
page += header

for filename in os.listdir(dir + "/in/posts/"):
    print(filename)

    #opens the post template
    file = open(dir + "/templates/article.html", 'r')
    postTemplate = file.read()
    file.close()

    #opens the body markdown and saves it to a variable
    file = open(dir + "/in/posts/" + filename, 'r')
    post = file.readlines()
    file.close()

    #extracts post information from the post
    postName = filename.replace("-", " ")
    postName = postName.strip(".md")
    postAuthor = post[0]
    postDate = post[1]
    postContent = post[2:]
    postContent = ''.join(postContent)

    #converts the body markdown to html
    contentHTML = markdown(str(postContent), extras=['fenced-code-blocks'])

    #formats the post template using info
    renderedPost = postTemplate.format(articleTitle = postName, articleAuthor = postAuthor, articleDate = postDate, articleContent = contentHTML)

    #appends the body to the page
    page += renderedPost

#opens the footer template and inserts the name and copyright info
file = open(dir + "/templates/footer.html", 'r')
footer = file.read()
file.close()
footer = footer.format(author = siteAuthor, copyright = siteCopyrightInfo)
#appends the footer to the rest of the page
page += footer

#writes the rendered page to the "out" folder
file = open(dir + "/out/index.html", 'w')
file.write(page)
file.close()