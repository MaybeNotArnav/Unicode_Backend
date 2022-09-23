# Unicode_Backend
 Django tasks for Unicode
 
 Hello! My name is Arnav and this is my attempt at the Django Backend Tasks.This project was very difficult as I had to start from scratch learning both Python and Django. Nevertheless this project was fun to work on because I like a good challenge.
 
 I also did not know how Git really worked so I apologize for having all the task in one commit.
 
 Quirks and kinks:
 Since I didn't know much about how Django projects worked, I might have gone for some unconventional naming in the project :)
 I have named the virtual environment made as 'test' and it is outside the project folder.You can run the environment before you start the sever.
 The project is named 'imscared' because I didn't really know what I was doing when I started doing it.
 The app inside said project is called 'testapp'
 
 Basic rundown of the project:
 1) There is a home page with my personal info with a link to the app that has all the tasks.
 2) When in the app you see a Twitter username search (since I used a Twittter API) which searches for a Twitter username based on userid.
 3) On the same page, using dynamic url you can access the task 1 (which cover both task 1 and 2)
 4) There is also a link to the database query which is the 4th task.
 5) The database query is very similar to the previous username search and has a link to the top three queries (I could have printed the top three queries on the same page but the view function was getting too long so I decided to  make a new view)
 6) The database query is a username search while the API uses userid to give back username.
 7) The link takes you to a page which shows top 3 queries.

Places to be optimized:
1) The API used gives a different dictionary if the userid sent isn't present so I made a 'error 404' case, which I think can be polished a bit.
2) I made another query object for when you query while I could've just updated the entry stored when performing the username search but this was a personal choice to differentiate the API searching for username and us searching our database for usernames.
3) The code is very rough since I think it might take more time to master this language and I didn't have a lot of time to complete the tasks.

Some working userid and username:
@elonmusk => 44196397
@jerma985 => 344980006
@maybenotarnav => 1412000446651125763 (Self plug hehe)
@markiplier => 517077573
@peachpitmusic => 2866196621 (Best band frfr)

TLDR:
This project is very shoddy but I have tried my best to polish the code (you do not want to see the original files).
Virtual Environment :- 'test' (.\test\Scripts\activate)
Project Name :- 'imscared'
App Name :- 'testapp'



