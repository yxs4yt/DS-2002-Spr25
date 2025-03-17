# Lab 6 - NoSQL Databases
Welcome to Lab 6 of the DS-2002 course! This lab will take you through the fundamentals of the primary types of NoSQL Databases we have briefly covered in class:
- **Document**: Use MongoDB to explore Movie data to answer a few questions and practice querying.
- **Time-Series**
- **Graph**: Complete the Neo4j fundamentals certification and add it to your LinkedIn!
- **Vector**: Follow along some code where we build a basic Patient Disease Diagnosis tool from scratch!

## Part 0. Setting Up and What to Submit
**Create**:
- Create a [LinkedIn](https://www.linkedin.com/) profile if you have not already.
- Create a new GitHub Gist, the URL of which is what will be submitted to Canvas for this lab. 

**Submit to Canvas:**
- URL to your GitHub Gist, which will contain the following information (please copy and paste the example below and then add the information to your gist as you go):

```
Part 1 (Documents - MongoDB):
  - Query 1: 
  - Answer 1: 
  - Query 2: 
  - Answer 2: 
  - Query 3: 
  - Answer 3:
Part 2 (Key-Value): 
Part 3 (Wide-Column):
Part 4 (Time-Series):
Part 5 (Ledger):
Part 6 (Graphs - Neo4j):
  - LinkedIn Profile URL: <paste url here>
Part 7 (Vector - From Scratch)
```

<br>

## Part 1. Document Databases using MongoDB:
### MongoDB Atlas Free Tier:
- MongoDB Atlas offers a free tier that allows you to create a small cluster. While it's a cloud-hosted service, it's very easy to set up.
- You can find many public datasets that can be easily imported into your free cluster.
- MongoDB also provides interactive tutorials and documentation with sample data.
- If you have not already done so, please watch [this video](https://www.youtube.com/watch?v=9DbZ2ii01ew&ab_channel=NealMagee) to set up your account.

### Quick Help for MongoDB:
1. Open your free cluster, navigate to your `sample_mflix` database, and see your six (6) collections, each of which containing many documents:
  - comments, embedded_movies, movies, sessions, theaters, users
2. Click on your `movies` collection and use `Find` to query your movies documents
3. Open the [query documentation](https://www.mongodb.com/docs/manual/tutorial/query-documents/) for help for how to query using MongoDB.
  - (NOTE: The documentation allows you to select a language. By default it will use `Node.js`, switch this to `Compass`.)
4. Copy and paste this query and hit `Apply`:
```
{
"year": { $gt: 1990 },
"cast": "Tom Hanks",
"genres": "Comedy",
"imdb.rating": { $gt: 7.5 },
"metacritic": {$gt: 80}
}
```
  - This should return three documents which consist of the first three Toy Story Movies.
  - With this query, we are searching for any movies that meets these criteria, i.e. All Tom Hanks comedies made after 1990 with critical acclaim on both IMDB (>7.5) and MetaCritic (>80).
  - You may be wondering, "Hey, there were four Toy Stories! Does this mean there is no Toy Story 4 in this collection or did it not do as well, critically?"
5. Try running this:
```
{
"year": { $gt: 1990 },
"cast": "Tom Hanks",
"genres": "Comedy",
"title": { $regex: '^Toy' }
}
```
  - Here we introduce the use of `regex` or Regular Expression, to enhance our search to find all of the Comedic "Toy" movies Tom Hanks has been in since 1990.
  - There are many other ways we could look to prove this, maybe even by getting rid of the genre or year, but we can rest easy knowing that Toy Story 4 is simply not in this dataset.

### Instructions for MongoDB
Please use my natural language sentences to create a Compass query to search within the sample_mflix database. You will need to paste your query as well as provide the answer to the thing I am trying to find.
0. **FOR EXAMPLE**: If I were asking for "All Tom Hanks comedies made after 1990 with critical acclaim on both IMDB (>7.5) and MetaCritic (>80).", I would expect to see the following in your Gist (I will be lenient on formatting, but try to get it close, at least so it is easy to read.):
```
Part 1 (Documents - MongoDB):
  - Query 0:
            {
            "year": { $gt: 1990 },
            "cast": "Tom Hanks",
            "genres": "Comedy",
            "imdb.rating": { $gt: 7.5 },
            "metacritic": {$gt: 80}
            }
  - Answer 0: Toy Story, Toy Story 2, Toy Story 3
```
1. An award winning R-rated Sci-Fi movie starring Arnold Schwarzenegger consisting of a "hunt" in the full plot description that IMDB (>6) found favorable, and MetaCritic hated (<35).
2. A G-rated movie, exactly 100 minutes long that came out either after 1980 or before 1940 with at least one "dog" being part of the full plotline.
3. The theaterId of the most northern theater in Charlottesville.

<br>

## Part 4. Vector Databases
1. Download the `Lab_6_Vector_Database.ipynb` file from the Lab 6 Assignment page on Canvas.
2. Go to [Google Collab](https://colab.research.google.com/) and sign in.
3. Open the notebook you just downloaded.
4. Read through and run each cell in the notebook.
5. Answer the questions at the bottom.
6. Add your answers to your Gist file, like so:
```
Part 4 (Vector - From Scratch)

1. How many patients are diagnosed with:
  - Flu: <your answer>
  - Common Cold: <your answer>
  - Pneumonia: <your answer>
  - Migraine: <your answer>
  - Asthma: <your answer>

2. How many patients went undiagnosed? <your answer>

3. <your answer>

4a. <your answer>
4b. <your answer>

5. <your answer>
```
