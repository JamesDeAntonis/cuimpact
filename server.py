#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect
app = Flask(__name__)

current_id = 11

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
	"description": "Join The Journal of Global Health and the Native American Council of Columbia University for"
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
	"group": "UndocU",
	"issue_tags": "immigration",
	"name":"Constitution Review and Position Overview",
	"description": "Hi everyone! Hope y’all enjoyed the break. For this meeting, Undo_CU will be going over our constitution as well as the "
	"E-board positions that we will be voting on next week. Please come if you’re interested in getting more involved with the group and "
	"invite your friends! We will be having snacks as well.",
	"facebook-link":"https://www.facebook.com/events/748036925700527/",
	"group-email":"undocumentedstudentsinitiative@gmail.com",
	"img":"/static/media/undocu.jpg",
	"when":"December 3rd 8 PM",
	"location": "Lerner Hall"
},
{
	"id":4,
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
	"id":5,
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
	"id":6,
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
	"id":7,
	"group": "Black Students Organization",
	"issue_tags": "lgbtq",
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
	"id":8,
	"group": "The Center for Gender and Sexuality Law",
	"issue_tags": "lgbtq",
	"name":"Rights of Trans and Gender-Nonconforming People",
	"description": "This panel will discuss the current state of affairs for trans and gender non-conforming people in the U.S. More specifically, "
	"speakers will reflect on arguments recently made before the Supreme Court in cases affecting the trans and GNC community. <br>"
	"Speakers include: <br>"
	"Katherine Franke, Sulzbacher Professor of Law, Gender, and Sexuality Studies, Columbia University<br>"
	"Alejandra Caraballo, Staff Attorney, Transgender Legal Defense and Education Fund (TLDEF) <br>"
	"Paisley Currah, Endowed Chair of Women's and Gender Studies, and Professor of Political Science, Brooklyn College and the Graduate Center <br>"
	"This event is free and open to the public",
	"facebook-link":"https://www.facebook.com/events/1492880080878160",
	"group-email":"gender_sexuality_law@law.columbia.edu",
	"img":"/static/media/politics.jpg",
	"when":"November 20th 4:30-6 PM",
	"location": "Columbia Law School"
},
{
	"id":9,
	"group": "UndoCU",
	"issue_tags": "immigration",
	"name":"UndoCU Updates and State of Immigration",
	"description": "Hi everyone! Join UndoCU for updates on our events, demonstrations, etc. and a conversation on current news regarding immigration"
	" and undocumented people. Hope to see y'all there!",
	"facebook-link":"https://www.facebook.com/events/2524175141153659/",
	"group-email":"undocumentedstudentsinitiative@gmail.com",
	"img":"/static/media/undocu.jpg",
	"when":"November 19th 8-9 PM",
	"location": "552 W 114th St"
},
{
	"id":10,
	"group": "Barnard Center for Research on Women",
	"issue_tags": "lgbtq",
	"name":"Trans Journalists Resisting Objectivity",
	"description": "Many people first learn about transgender issues in the news media. Coverage of transgender issues and the presence "
	"and visibility of transgender journalists are both on the rise. At the same time, transgender people have and continue to be reported "
	"on through distorted lenses of transphobia, white supremacy, and binary gender, and much of this reporting is presented as objective "
	"and fair. <br>"
	"In this panel discussion, Meredith Talusan and Lewis Raven Wallace, seasoned transgender journalists and movement journalism activists, "
	"will address the problems of “objectivity” for trans journalists and trans subjects, and discuss how to chart a path of rigor, conscious "
	"subjectivity, and community accountability in the worlds of journalism and non-fiction storytelling. <br>"
	"###<br>"
	"Events are free and open to the public. RSVP is preferred but not required. Seating is available on a first-come, first-seated basis.",
	"facebook-link":"https://www.facebook.com/events/612808679215618",
	"group-email":"bcrw@barnard.edu",
	"img":"/static/media/view.jpg",
	"when":"November 19th 6:30-8 PM",
	"location": "Barnard Center for Research on Women"
},
{
	"id":11,
	"group": "Sunrise Columbia",
	"issue_tags": "environmental-justice",
	"name":"Beyond Individual Action on Climate Change",
	"description": "What’s the most effective thing to do about climate change?"
	" Mainstream responses to the climate crisis tend to focus either on personal responsibility or mass action. "
	"In the context of a growing ecological breakdown, it’s time to expand our arsenal. All of us have a web of "
	"individual connections—parents, friends, coworkers, professors—which we often forget about. In this workshop, "
	"we’ll develop tailored plans for leveraging our personal connections towards maximum impact on climate change.",
	"facebook-link":"https://www.facebook.com/events/456522618589804/",
	"group-email":"team@sunrisemovement.org",
	"img":"/static/media/indivAction.jpg",
	"when":"November 16th 2-4 PM",
	"location": "Room 614 Milstein"
}
]
	
@app.route('/')
def hello():
    return redirect("/home", code=302)

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/view_all/<item_filter>', methods=['GET', 'POST'])
def view_all(item_filter=None):
	clicked_filter = item_filter
	return render_template('view_all.html',events=events, current_id = current_id, clicked_filter=clicked_filter)

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
		"id":current_id,
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


