# LinkedIn Learning Downloader
#### Based on [liranbg's linkedin-learning-downloader](https://github.com/liranbg/linkedin-learning-downloader)

Asynchronous scraping tool to fetch LinkedIn-learning's courses videos.


#### Info

Please use this script for your own purposes.

This script was written for educational usage only.

Make sure your LinkedIn account is **NOT** protected with 2FA

#### Usage
> pip install -r requirements.txt

Edit the 'config.py' file with your credentials and course link

You may include multiple slugs seperated by commas to download multiple course at the same time.

To changed the downloads directory simply change the 'downloaded_videos' string to whatever you want the folder to be called.

Upon installing dependencies and modifying config.py - run
> python main.py
