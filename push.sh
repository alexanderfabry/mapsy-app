#!/bin/bash

echo 'something'

git st
git add .
git ci
git push heroku master
git push origin master
