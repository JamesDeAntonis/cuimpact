#!/bin/bash
git add .
echo "enter a comment for the github commit"
read commit_message
echo $commit_message
git commit -m "$commit_message"
git push
git push heroku master
echo "launching the web app"
heroku open
