Youtube-Emailer
===============

Email family and friends when you upload a new video to youtube. 

Most of the third party service do not work great with your unlisted youtube videos, so here is a simple bash script which polls youtube gdata endpoint periodically to check for new videos and email family and friends. 

You will need to get Auth token from Youtube using ClientLogin as specified here 
https://developers.google.com/youtube/2.0/developers_guide_protocol_clientlogin

Run the following command from the terminal 

curl --silent 'https://www.google.com/accounts/ClientLogin' --data-urlencode Email=youremail.com --data-urlencode Passwd='yourpassword' -d accountType=GOOGLE -d source=SO -d service=youtube | grep Auth

The output should look something like 

"Auth=DQAAALIAAACZcKNRJ8jYKOsTlK7rtaHcUmR14gKvhf6tlHYmoxL-oYD4K2vrozRcc4cpv4NWw7h8Cl2hLzIE_PeuMLpmqTnOkyXzPMmeUGy6cTP_6HvZiflQCC2nDdxGvDpe7uwTSasdBesI7-QAmrrCaWM2dK85D5rFJS2yxGoNUpJnPlwNwtAv_bBzOZTPVeWW_EcBz_FusgbirXqVMsgfwammF0JZHjct0TE7XYH8avpmpTVj8Snq9YBStUyfOH21SJNa7wdBDac"

Use this in the youtube.py and change it accordingly to include sender's and receipients email address.

Execute the mailer.sh script and you are good to go. 

