# ArCTFurious
A simple QR-code based capture-the-flag.

# Description
The aim is to have a user find and scan a number of QR codes scattered around
an event hall. Upon finding a code, the user will scan the code and be taken
to this web application.

Here, if the user has NOT signed up already, they will be prompted to register 
an email address, name and a handle to display on the scoreboard. The score 
for the code they found will then be added to their total.

If the user HAS signed up already, then they should have a cookie present on 
their device, set at signup. This cookie will allow the webapp to detect which
user has found the code, and add the code score to their total.

# Implementation
A simple webapp will be created using Python3, sqlite3 and hug. There will be
three main pages:

- Scoreboard
- Signup page
- QR code hidden page 

## Scoreboard
The scoreboard will present a list of users who have engaged in the game, 
by displaying their handle and their score, by descending order of highest
score.

## Signup page
The signup page will capture the email, name and handle of any new player/user
wanting to join the game. 

## QR code hidden page
The QR code hidden page is one endpoint, /ctf. Each QR code will link to this
page with a different 'code' parameter. Each of these QR codes will be worth
a certain amount of points, depending on how hard the QR code is to find.

If a user is not yet signed in when accessing this page (if they haven't got
a cookie) then they will be redirected to the signup page.

A visit to this page with a valid code and a valid user (somebody signed up
and scanned a legit QR code) will result in a randomly-selected 'You win!'
screen being displayed. Alternatively, each success page could be determined
based on the code given.

A visit to this page without a valid cookie will result in a redirect to the
signup page, regardless of whether the code supplied is valid.
