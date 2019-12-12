ANYOUT by Team Otherwise

- Khoa Tran : kttran@bu.edu
- Abdel Hussein : ahussein@bu.edu
- Haoxuan Li : harryli@bu.edu
- Haocun Wang : haocunw@bu.edu
- Jiwon Park : jiwonp98@bu.edu

Anyout is an event exploration web application. The goal of the app is to allow hosts to spread word about their events to students and faculty around BU campus. Functions of the app include:

- Hosting events
- Browsing events with Google Maps
- Account authorization
- Communication between hosts and interested attendees

Anyout showcases all the features of a fullstack web application. The frontend and backend are separate and isolated where the only form of connection between the two are http requests. The frontend centers around the Vue js framework and Google Cloud Api services while the backend uses flask and python and mongodb for storage.

HOW TO RUN THE PROJECT:
Both the backend and frontend must run stimultaneously for proper connection. The instructions below show how one can run both servers at the same time. The instructions are only for macOS devices.

- Clone this repo
  1. run `git clone https://github.com/khoatran2320/any-out.git`
- Starting the frontend:
  1. Make sure the device has npm and vue installed
  2. cd into the client folder
  3. run `npm install`
  4. run `npm run serve`
  5. open browser and go to `http://localhost:8080/`

- Starting the backend:
  1. Make sure the device has pip3, python3, mongodb and the mongodb command line is accessible
  2. open the terminal and access the mongo shell with the command `mongo`
  3. run `use anyout` to create a database for the project on the local machine
  4. run `db.createCollection("users")` to create a collection for the users
  5. run `db.createCollection("events")` to create a collection for the events
  6. run `show collections` and ensure that the collections are created properly
  7. open a new terminal and cd into the server folder
  8. run `pip3 install virtualenv`
  9. run `python3 -m venv env`
  10. run `source env/bin/activate`
  11. run `pip3 install -r requirements.txt`
  12. run `python3 app.py`
  13. the backend should now run on `http://localhost:4000/`

**Make sure the backend and frontend are both run simultaneously on separate terminals**
