#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect
app = Flask(__name__)

current_id = 4

events=[
{
	"id":0,
	"group": "Association of Filipino Scientists in America",
	"issue_tags": "environmental-justice",
	"name":"Environmental Rights are Human Rights!",
	"description": "In commemoration of the International Human Rights Day, the Association of Filipino Scientists "
	"in America (AFSA) will hold a seminar about the climate change issues in the Philippines and the world!<br>"
	"Speakers:<br>"
	"-Myla Ramirez, Environmental Health Researcher and Government Scientist <br>"
	"-Carla Bertulfo, PhD Biological Sciences Student at Columbia University <br>"
	"Come learn about the environmental issues and discuss how we could protect our environment!"
	"Happening on Dec 7 (Sat) from 3-5pm at Room 1000, Fairchild Building, Columbia University!",
	"facebook-link":"https://www.facebook.com/events/2481854395394044",
	"group-email":"afsa.official@gmail.com",
	"img":"/static/media/envfil.jpg",
	"when":"December 7th 3-5 PM",
	"location": "Room 1000 Fairchild Building"
},
{
	"id":1,
	"group": "Sunrise Columbia",
	"issue_tags": "environmental-justice",
	"name":"Climate Emergency Strike",
	"description": "We implored President Bollinger for over a month to sign Columbia onto" 
	"the UN’s letter declaring a climate emergency. After over 100 phone calls, 200 emails, & 1000 signatures,"
	"he let the signing deadline come and go without giving us an answer. <br>"
	"If Columbia won’t act, we will.<br>"
	"Join us on Friday at 2pm at the Sundial to demand that Columbia divest from fossil fuels. "
	"We will be joining over a dozen universities across the country in calling on our respective "
	"administrations to take real steps to protect our future and our planet. We hope to see you there.",
	"facebook-link":"https://www.facebook.com/events/2541467226136977/",
	"group-email":"team@sunrisemovement.org",
	"img":"/static/media/fossil.jpg",
	"when":"December 6th 2 PM",
	"location": "Sundial"
},
{
	"id":2,
	"group": "Native American Council & The Journal of Global Health",
	"issue_tags": "indigenous-rights",
	"name":"Health & Native American Communities",
	"description": "oin The Journal of Global Health and the Native American Council of Columbia University for"
	"an event exploring the effects of governmental policies, environmental injustice, and healthcare discrimination"
	" on Native American health. Light refreshments will be provided."
	"The following speakers will be at the event: <br>"
	"Ana Navas-Acien, MD MPH | Professor of Environmental Sciences at Mailman School of Public Health <br>"
	"Charles Whalen | New York Indian Council",
	"facebook-link":"https://www.facebook.com/events/462315477755539",
	"group-email":"nac.columbia@gmail.com",
	"img":"/static/media/health.jpg",
	"when":"December 4th 6-7PM",
	"location": "Lerner 568"
},
{
	"id":3,
	"group": "Native American Council",
	"issue_tags": "indigenous-rights",
	"name":"Food Sovereignty Feast and Zine Release",
	"description": "The entire Columbia community will be invited to join together for our closing dinner, which will"
	"celebrate the work of the month in addition to honoring the Native women faculty currently on campus. We will provide"
	" a meal in addition to a special tasting menu, prepared by Native students, of Indigenous foods and dishes from their communities. "
	"We will also use this community gathering to debut the zine that will contain Indigenous student contributions reflection on knowledge"
	" and art within their own home communities.",
	"facebook-link":"https://www.facebook.com/events/561210544717154/",
	"group-email":"nac.columbia@gmail.com",
	"img":"/static/media/food-sov.jpg",
	"when":"November 23rd 6:30-8:45 PM",
	"location": "Diana Center"
},
{
	"id":4,
	"group": "CU Multicultural Affairs ",
	"issue_tags": "indigenous-rights",
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
	"id":5,
	"group": "Barnard Student Life",
	"issue_tags": "environmental-justice",
	"name":"POC Meetup: Environmental Justice",
	"description": "Join us for a people of color community meet up where we will eat lunch and discuss environmental justice "
	"in relation to people of color. Who is usually left out of conversations about the environment? Why does environmental justice "
	"matter to people of color? Come for a casual discussion and free food!",
	"facebook-link":"https://www.facebook.com/events/704691723269876/",
	"group-email":"bsl@barnard.edu",
	"img":"/static/media/environ.jpg",
	"when":"November 22nd 12-1:30 PM",
	"location": "Barnard Student Life"
},
{
	"id":6,
	"group": "Black Students Organization",
	"issue_tags": "trans-rights",
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
}
]
	
@app.route('/')
def hello():
    return redirect("/home", code=302)

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
	issue_tags = json_data["issue_tags"]
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
		"issue_tags": issue_tags,
		"facebook-link": facebook_link,
		"img": img,
		"when": when,
		"location":location
	}
	events.append(new_event)

	return jsonify(events = events)

if __name__ == '__main__':
   app.run(debug = True)


