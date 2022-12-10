#!/bin/bash

echo "
 __| |_______________________________| |__
(__   _______________________________   __)
   | |                               | |
   | |                               | |
   | |         Twitter Likes         | |
   | |                               | |
   | |                               | |
 __| |_______________________________| |__
(__   _______________________________   __)
   | |                               | |"

# Copy the like.js file to a new file called generate_likes.js
echo -e "\nParsing like.js...\n"
cp data/like.js data/generate_likes.js

# Replace window.YTD.like.part0 with tweets in generate_likes.js
sed -i '' 's/window\.YTD\.like\.part0/tweets/g' data/generate_likes.js

# Append a line to stringify the tweets array and write it to likes.json
echo -e '\n\nconst fs = require("fs"); fs.writeFileSync("data/likes.json", JSON.stringify(tweets));' >> data/generate_likes.js

# Run the generate_likes.js file
node data/generate_likes.js
echo -e "Generated likes.json!\n"

# Run the main Python file
echo -e "Analyzing your Tweets...\n"
python3 main.py
