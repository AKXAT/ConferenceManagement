# Django based - Conference Management System 

This is a Django based - Conference Management System. Below are all the funtionalities that you can perform. By Defaul it lets you login as a Main Admin. 

1. You are allowed to add new conference and delete the existing one
2. a single conference can have multiple talks , you can add multiple talks and delete the existing one 
3. each talk can have n number of speakers and listeners/participants 
4. you are allowed to add new speaker/participants and delete the existig ones


### Models 
1. The first Model is for Conference with the following properties -> Title , Description , Start & End Date
2. The second Model is for Talks with the following properties -> Title , Description , Duration , Date and Time 
3. Third Model is for the Speaker/Participants with the following properties -> A speaker/participant is defined by their username & email.


### APIs

1. create/edit a conference
2. add/edit a talk
3. add/remove speaker/participant from a talk.
4. list talks in a conference
5. list conferences.


# Here are the screenshots from the Project.
## Home Page
![1](ScreenShots\1.png)

## When we click on add a New conference 
![2](ScreenShots\2.png)

## When we select one of the conference  
![3](ScreenShots\3.png)

## When we click on add a new talk 
![4](ScreenShots\4.png)

## When we select one of the Talks to see members  
![4](ScreenShots\5.png)
