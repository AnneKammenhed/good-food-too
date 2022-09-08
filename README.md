<h1>Remember</h1>

python3 manage.py makemigrations --dry-run

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


<h1>Background</h1>
This app is built as the fourth project of my full stack development course that i started in the beginning of May 2022. It is for a restaurant to book a table for max 8 persons online and to give information about any allergies.

During the project some of the harder parts was to get the urls in order and the original repo, with connections to Heroku from the beginning didn't work with the amouyt of adjustments that i made to the model(-s).

<h1>Functions</h1>
The model allows for anyone to book a table. However it does not allow for the same e-mail adress to book exactly the same day and time.  

<h1>Testing</h1>
I did some testing before I handed in the project.


<h1>Credits</h1>  
This project is built on the Code Institute student template for Gitpod with preinstalled tools. I followed the django blog walkthrough project for parts of the build. 