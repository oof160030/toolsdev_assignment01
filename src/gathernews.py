#Description: Scrape and summarize entertainment news articles
import nltk
import newspaper

def search_news_article(word, web_url):
    paper_1 = newspaper.build(web_url, memoize_articles=False)
    article_list = []
    var = 0
    maxvar = 10
    
    foundvar = 0
    foundmaxvar = 5
    
    for article in paper_1.articles:
        if var < maxvar and foundvar < foundmaxvar:
            var = var +1
            article.download()
            article.parse()
            article.nlp()
            if var < maxvar and word != "" and word in article.keywords:
                #print("Article Found!")
                article_list.append(article)
                foundvar = foundvar + 1
            elif var < maxvar and word == "":
                #print("Article Found!")
                article_list.append(article)
                foundvar = foundvar + 1
    
    return article_list
    '''
    if word != "":
        for article in paper_1.articles:
            if var < 10
                article.download()
                article.parse()
                if word in article.keywords:
                    article_list.append(article)
    else:
        for article in paper_1.articles:
            article.download()
            article.parse()
            article_list.append(article)
        
    return article_list
    '''        
            

def write_news_summary(articles):
    #open news_summary file
    news_sum = open("news_summary.txt","w+")
    #Clear/truncate file
    news_sum.truncate(0)
    #Write "NEWS SUMMARY" followed by date
    news_sum.write("===NEWS SUMMARY=== \n")
    #for each file, parse title and authors
    #then parse summary
    #write both to file
    for article in articles:
        author_list = ""
        for author in article.authors:
            author_list += (" " + author + ",")
        author_list = author_list[:-1]
        article_shorttext = article.text
        article_shorttext = "\"" + article_shorttext[:100] + "...\""
        
        news_sum.write("\"" +article.title + "\" -" + author_list + "\n" + article_shorttext + "\n\n")
    #at end of for loop, close file
    news_sum.close()

#anim_mag_paper = newspaper.build('https://www.animationmagazine.net/', memoize_articles=False)
#anim_world_paper = newspaper.build('https://www.pcgamer.com/news/')
#pc_gaming_paper = newspaper.build('https://www.awn.com/')

#for article in anim_mag_paper.articles:
#   print(article.url)

userinput = input("Please enter any keyword (press enter to continue):")
article_feed = []

print("Input recieved. Starting news search...")

article_feed.extend(search_news_article(userinput, 'https://www.animationmagazine.net/'))
article_feed.extend(search_news_article(userinput, 'https://www.pcgamer.com/news/'))
article_feed.extend(search_news_article(userinput, 'https://www.awn.com/'))

print("Completed article reading. Compiling news summary...")

for article in article_feed:
    print("[" + str(article_feed.index(article)) + "] - " + article.title)

write_news_summary(article_feed)

userinput = ""
userinput = input("Open article in browser? Enter number of desired article, or press enter to cancel:")
while userinput.isdigit():
    if int(userinput) >= 0 and int(userinput) < len(article_feed):
        import webbrowser
        url = article_feed[int(userinput)].url
        webbrowser.open_new_tab(url)
        userinput = input("Open another article in browser? Enter number of desired article, or press enter to cancel:")
    else:
        userinput = input(userinput + " is not a valid option! Open another article in browser? Enter number of desired article, or press enter to cancel:")

print("News search concluded. Ending operation. Thank you!")
#for article in article_feed:
#    print(article.title)