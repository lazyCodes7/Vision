import facebook
from SpeechHandling import *
TOKEN = "your graph-api token here"
def get_posts():
	graph = facebook.GraphAPI(access_token=TOKEN)
	friends = graph.get_connections(id='user_id', connection_name='friends')
	time.sleep(10)
	speak("Total number of friends are {}\n".format(friends['summary']['total_count']))
	query_string = 'posts?limit={0}'.format(6)
	posts = graph.get_connections(id, query_string)
	i = 0
	for post in posts['data']:
		i +=1
		speak("{}. {}.\n".format(i, post['message']))
		time.sleep(1)

