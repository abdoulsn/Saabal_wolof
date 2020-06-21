# Wolof language scraping

-----------------------------------------------------------------------------------------------------------------------------

## Tasks: 
- 1.  Crawle urls of actegorie news leading to articles in saabla website. Each url content multiple article to scrape.
- 2.  Once 1.  is done, retrive all title and link_ref( will use this to get twolof text) for every category of news.
- 3.  Scrape text of each articles (last counted 112 articles) and store it in dataset as csv. 

once these step done,  will'll end with csv(raw data)  file like this: 

| titles                                | Link_to_content  | textes         | categories   |
| :------------------------------------ | :--------------: | -------------: | -----------: |
|  Ma tënkal la tuuti ci Saamóori Ture! | https//www       | [Niki bisub... |    politig   |
| . ..                                  | ...              | ...            |              |

- 4.  Split (by sentences)  each paragraph in row form this raw csv to multiple rows.  NB in this step (we'll duplicate other rows to not loos information correspondance.
then `textes` 
