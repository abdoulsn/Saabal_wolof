# Wolof language scraping

-----------------------------------------------------------------------------------------------------------------------------

## Tasks 1: Crawl and scrape
- 1.  Crawle urls of actegorie news leading to articles in saabla website. Each url content multiple article to scrape.
- 2.  Once 1.  is done, retrive all title and link_ref( will use this to get twolof text) for every category of news.
- 3.  Scrape text of each articles (last counted 112 articles) and store it in dataset as csv. 

once these step done,  will'll end with csv(raw data)  file like this: 

| titles                                | Link_to_content  | textes         | categories   |
| :------------------------------------ | :--------------: | -------------: | -----------: |
|  Ma tënkal la tuuti ci Saamóori Ture! | https//www       | [Niki bisub... |    politig   |
| . ..                                  | ...              | ...            |              |

- 4.  Split (by sentences)  each paragraph in row form this raw csv to multiple rows.  NB in this step (we'll duplicate other rows to not loos information correspondance.
then `textes` will end up into multiple row as many as number of items in one given row. otheres columns will be duplicated as to have as many rows as `len()` of one list textes in one row. 

## Recap
In step 3. we've this: 

![alt text](https://github.com/abdoulsn/wolof/blob/master/image1.png)

In step 4.  w'il end up with this.  

![alt text](https://github.com/abdoulsn/wolof/blob/master/image2.png)

--------------------------------------------------------------------------------------------------------------------------

## Task 2: Process text (delete emoji,  delete unusful row containing un wanted data)


