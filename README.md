# Mechine-_learning_project
This is first ml project


creating vitual env commend

conda create -p venv python==3.7 -y 
Here -p means virtual  enivironmrnt will create same project folder. If we keep -n venv will create in anaconda folder.

How to activate conda env
conda activate venv/--CMD 

how to create requirements.txt file --> pip install -r requirements.txt

addig files in git repository 

git status --> when we excute the this command we can see whcih files are not tracked or the files are not updated in git rep 

git add filename,filenam1,---filenamen

git add . ---> it will add all files at a time 

git remove filename ---> it will remove file git rep

git commit --- > This create version in git rep 

git log--> it will show you the previous version 

to send chnages to git ---> git push origin main 

to check remote url --> git remote -v 

how to find branch --> git branch 

To setup cicd pipeline we need three information 
Heroku Email id=bollineniramesh.informatica@gmail.com
Heroku API key: d827328b-b49c-4da1-8646-9baebad37123
Heroku APP name= ml_regresion_app

How to create Docker file.

right click the project create file 
We nned to keep this instrucations in Docker file 

FROM python:3.7
COPY . /app  Here . indicates current directory 
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT 
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

How to check docker version ---> docker --version 

BUILD docker img---> docker build -t <img name>:<tagname> . --> .Means location of the file 

To list docker images ---> docker images 

To run the docker image ---> docker run -p 5000:5000 -e PORT=5000 imageid [Here imageid we can see from above comand ]

To check running continers in docker ---> docker ps 

To stop any continer --> docker stop continerid

We have to create folder .github 

Within .github folder we need to create one more folder workflows 

In the workflows folder we need to create one yaml file line main.yaml file  





