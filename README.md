# Twitter Likes
Analyze the latent space of your Twitter likes.

<p align="center">
  <img width="800" alt="image" src="https://user-images.githubusercontent.com/47067154/206836335-35bfec96-b96a-48ac-943d-b1926199d2f3.png">
</p>

## Setup
1. Download your [Twitter archive](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive)
2. Drag your `like.js` file into the `data/` folder
3. Set up a virtual environment and install the requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the followings commands in your shell:
```bash
chmod u+x run.sh
./run.sh
```

Thanks a lot to the creators of [TweetedAt](https://github.com/oduwsdl/tweetedat) for making a fast implementation of a Tweet ID to date converter!
