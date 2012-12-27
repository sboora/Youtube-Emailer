import commands
import json
from datetime import datetime,tzinfo,timedelta

query ='curl --silent --header "Authorization: GoogleLogin {auth cookie}" "https://gdata.youtube.com/feeds/api/users/{username}/uploads?alt=json"'
response = commands.getoutput(query)
videos = json.loads(response)
entries = videos['feed']['entry']
currentDate = datetime.now()
print "Checking for new videos at " + str(currentDate) + "\n\n"
message = "New videos uploaded to Youtube. Click on the links below.\n\n"
hasNew = False
for entry in entries:
    #Based on PST, change it accordingly
    publishedDate = datetime.strptime(entry['published']['$t'], "%Y-%m-%dT%H:%M:%S.000Z" ) - timedelta(days=0, hours=8)
    href = entry['link'][0]['href'].split('&')[0]
    delta = (currentDate - publishedDate)
    if delta < timedelta(minutes=15):
        message = message + entry['title']['$t'] + " - " + href + "\n\n"
        hasNew = True
if hasNew:
    message = message + "Enjoy!"
    print "sending mail"
    emailCommand = 'echo "' + message + '" | mail -s "New videos uploaded to Youtube" Receipients@gmail.com   -- -f Sender@gmail.com' 
    print emailCommand
    commands.getoutput(emailCommand)
