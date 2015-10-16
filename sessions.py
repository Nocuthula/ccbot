import mechanize
import bot
event_url = "https://v3.eventcenter.crowdcompass.com/admin/events/yiTVBA0C12"
login_url = "https://eventcenter.crowdcompass.com/users/sign_in"
br = mechanize.Browser()
br.set_handle_robots(False)


# Forms
def get_forms(page):
	br.open(page)
	for form in br.forms():
		print form

#login 
def login(email, password):
	br.open(login_url)
	br.select_form(nr = 0)
	br.form["user[email]"] = email
	br.form["user[password]"] = password
	response = br.submit()
	return response.geturl()

#session name
def edit_session_name(name,session_url):
	br.open(session_url)
	br.select_form(nr=0)
	br.form["activity[name]"] = name
	br.submit()

#Attendees
#login("fashanu@appyourevent.co","fashanu@2015")
#url = "https://v3.eventcenter.crowdcompass.com/admin/events/yiTVBA0C12/activities/810329/edit"
#edit_session_name("Googling Hello", url)
