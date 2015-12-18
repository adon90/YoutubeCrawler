#!/bin/bash
curl --silent https://www.youtube.com/watch?v=SYdGDH1KrnM | egrep "watch-view|yt-uix-button-content" | tr -s " " "\n" | egrep "watch-view|yt-uix-button-content" | tr -s ">|<" "\n" | grep ^[0-9] | tr -s "\n" " " | cut -d " " -f1,2,4 | tr -s " " "\n"
