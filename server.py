#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 4

events=[
{
	"id":0,
	"group": "Native American Council",
	"issue-tags": "indigenous rights",
	"name":"Food Sovereignty Feast and Zine Release",
	"description": "The entire Columbia community will be invited to join together for our closing dinner, which will"
	"celebrate the work of the month in addition to honoring the Native women faculty currently on campus. We will provide"
	" a meal in addition to a special tasting menu, prepared by Native students, of Indigenous foods and dishes from their communities. "
	"We will also use this community gathering to debut the zine that will contain Indigenous student contributions reflection on knowledge"
	" and art within their own home communities.",
	"facebook-link":"https://www.facebook.com/events/561210544717154/",
	"group-email":"	nac.columbia@gmail.com",
	"img":"/static/media/food-sov.jpg",
	"when":"November 23rd 6:30-8:45 PM",
	"location": "Diana Center"
},
{
	"id":1,
	"group": "CU Multicultural Affairs ",
	"issue-tags": "indigenous rights",
	"name":"One Love Dinner",
	"description": "Enjoy dinner with residents of the IRC and celebrate ourselves, our accomplishments and our communities!"
	"We will be writing letters in support of imprisoned indigenous water protectors."
	"There will be vegan/vegetarian/gluten free options! Come grab food and support indigenous activists!",
	"facebook-link":"https://www.facebook.com/events/1161463644052852/",
	"group-email":"	multicultural@columbia.edu​",
	"img":"/static/media/one-lov.jpg",
	"when":"November 22nd 5-8 PM",
	"location": "Intercultural Resource Center"
},
{
	"id":2,
	"group": "Black Students Organization",
	"issue-tags": "trans rights",
	"name":"BSO Presents: Trans Lives Matter",
	"description": "BSO this Thursday (11/21) will be holding our Trans Lives Matter meeting. We’ll be screening Major!,"
	" the award-winning documentary following the life and campaigns of Miss Major Griffin-Gracy, a Black trans icon and activist"
	" who had been fighting for the rights of trans women of color for over 40 years. After the screening we’ll be having a discussion "
	"on the film. Come through!",
	"facebook-link":"https://www.facebook.com/events/2437318159817854/",
	"group-email":"	multicultural@columbia.edu​",
	"img":"/static/media/trans-lives.jpg",
	"when":"November 21st 9-11 PM",
	"location": "Intercultural Resource Center"
},
{
	"id":3,
	"group": "Barnard Student Life",
	"issue-tags": "environmental justice",
	"name":"POC Meetup: Environmental Justice",
	"description": "Join us for a people of color community meet up where we will eat lunch and discuss environmental justice "
	"in relation to people of color. Who is usually left out of conversations about the environment? Why does environmental justice "
	"matter to people of color? Come for a casual discussion and free food!",
	"facebook-link":"https://www.facebook.com/events/704691723269876/",
	"group-email":"bsl@barnard.edu",
	"img":"/static/media/environ.jpg",
	"when":"November 22nd 12-1:30 PM",
	"location": "Barnard Student Life"
}
]
	


@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/view_all')
def view_all():
	return render_template('view_all.html',events=events, current_id = current_id)

@app.route('/upload_event')
def upload_writing():
	return render_template('upload_event.html',events=events, current_id = current_id)

@app.route('/view/<item_id>', methods=['GET', 'POST'])
def view(item_id=None):
	global events

	i=int(item_id)
	group = events[i]["group"]
	name = events[i]["name"]
	link = events[i]["facebook-link"]
	email = events[i]["group-email"]
	img = events[i]["img"]
	when = events[i]["when"]
	loc = events[i]["location"]
	description = events[i]["description"]

	return render_template('view.html', group=group, name=name, description=description,
		link=link,email=email,img=img,when=when,loc=loc)


@app.route('/save_event', methods=['GET', 'POST'])
def save_event():

	global current_id
	global events

	json_data = request.get_json()
	name = json_data["name"]
	group = json_data["group"]
	group_email = json_data["group-email"]
	description = json_data["description"]
	issue_tags = json_data["issue-tags"]
	facebook_link = json_data["facebook-link"]
	img = json_data["img"]
	when = json_data["when"]
	location = json_data["location"]

	#add new entry to writing array
	current_id += 1
	new_event = {
		"name": name,
		"group": group,
		"group-email": group_email,
		"description": description,
		"issue-tags": issue_tags,
		"facebook-link": facebook_link,
		"img": img,
		"when": when,
		"location":location
	}
	events.append(new_event)

	return jsonify(events = events)

if __name__ == '__main__':
   app.run(debug = True)


