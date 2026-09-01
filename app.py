from flask import Flask, render_template, request, session, redirect
from myplace import Myplace
from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_computing_terms", methods=["GET","POST"])
def add_one_computing_terms():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into computing_terms (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from computing_terms')


        return render_template("computing_termsform.html", computing_termss=user, one_user=one_user, the_title="add new computing_terms")


    user = query_db('select * from computing_terms')
    one_user = query_db("select * from computing_terms limit 1", one=True)
    return render_template("computing_termsform.html", computing_termss=user, one_user=one_user, the_title="add new computing_terms")

@app.route("/add_one_musical_pieces", methods=["GET","POST"])
def add_one_musical_pieces():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musical_pieces (title,style,composer,score,key_signature,time_signature,pic) values (:title,:style,:composer,:score,:key_signature,:time_signature,:pic)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from musical_pieces')


        file_pointer = open("./samplescoreexample.ly")
        contents = file_pointer.read()
        contents=contents.replace("KEYSCOREHERE", request.form["key_signature"].replace(" "," \\")).replace("TIMESCOREHERE", request.form["time_signature"]).replace("CONTENTSCOREHERE", request.form["score"])
        file_pointer = open("./static/scores/musical_pieces_score_sample_"+mylastrowid+".ly", "w")
        file_pointer.write(contents)
        file_pointer.close()
        file_pointer = open("./static/scores/musical_pieces_score_sample_"+mylastrowid+".html", "w")
        file_pointer.write("<lilypond staffsize=34>"+contents+"</lilypond>")
        file_pointer.close()
        subprocess.run(["lilypond-book", "static/scores/musical_pieces_score_sample_"+mylastrowid+".html", "-f", "html", "--output", "static/scores/samplescoremusical_pieces_score"+mylastrowid]) 

        try:
            f= open("static/scores/samplescoremusical_pieces_score"+mylastrowid+"/musical_pieces_score_sample_"+mylastrowid+".html")
            s = f.read()
            soup = BeautifulSoup(s)

            picvalue=dict({'pic': "static/scores/samplescoremyscore_mymusic"+mylastrowid+"/"+soup.find('img').get("src"), 'id': mylastrowid})
        except:
            picvalue=dict({'pic': "", "id": mylastrowid})
        print(picvalue)

        hello_there = query_db("update musical_pieces set pic = :pic where id = :id",picvalue, one=True)

        return render_template("musical_piecesform.html", musical_piecess=user, one_user=one_user, the_title="add new musical_pieces")


    user = query_db('select * from musical_pieces')
    one_user = query_db("select * from musical_pieces limit 1", one=True)
    return render_template("musical_piecesform.html", musical_piecess=user, one_user=one_user, the_title="add new musical_pieces")

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from musicalinstrument')


        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_profiles", methods=["GET","POST"])
def add_one_profiles():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        tousleshobbies= query_db("select * from hobbies")

        one_user = query_db("insert into profiles (name,f_or_m,musicalinstrument_id,hobbies_id) values (:name,:f_or_m,:musicalinstrument_id,:hobbies_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from profiles')


        return render_template("profilesform.html", profiless=user, one_user=one_user, the_title="add new profiles", touslesmusicalinstrument=touslesmusicalinstrument, tousleshobbies=tousleshobbies)


    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    tousleshobbies= query_db("select * from hobbies")

    user = query_db('select * from profiles')
    one_user = query_db("select * from profiles limit 1", one=True)
    return render_template("profilesform.html", profiless=user, one_user=one_user, the_title="add new profiles", touslesmusicalinstrument=touslesmusicalinstrument, tousleshobbies=tousleshobbies)

@app.route("/add_one_profilehascomputingtermlogs", methods=["GET","POST"])
def add_one_profilehascomputingtermlogs():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescomputing_terms= query_db("select * from computing_terms")

        touslesprofiles= query_db("select * from profiles")

        one_user = query_db("insert into profilehascomputingtermlogs (computing_terms_id,profiles_id,content) values (:computing_terms_id,:profiles_id,:content)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from profilehascomputingtermlogs')


        return render_template("profilehascomputingtermlogsform.html", profilehascomputingtermlogss=user, one_user=one_user, the_title="add new profilehascomputingtermlogs", touslescomputing_terms=touslescomputing_terms, touslesprofiles=touslesprofiles)


    touslescomputing_terms= query_db("select * from computing_terms")

    touslesprofiles= query_db("select * from profiles")

    user = query_db('select * from profilehascomputingtermlogs')
    one_user = query_db("select * from profilehascomputingtermlogs limit 1", one=True)
    return render_template("profilehascomputingtermlogsform.html", profilehascomputingtermlogss=user, one_user=one_user, the_title="add new profilehascomputingtermlogs", touslescomputing_terms=touslescomputing_terms, touslesprofiles=touslesprofiles)

@app.route("/add_one_profilehasscorelogs", methods=["GET","POST"])
def add_one_profilehasscorelogs():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusical_pieces= query_db("select * from musical_pieces")

        touslesprofiles= query_db("select * from profiles")

        one_user = query_db("insert into profilehasscorelogs (musical_pieces_id,profiles_id,content) values (:musical_pieces_id,:profiles_id,:content)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from profilehasscorelogs')


        return render_template("profilehasscorelogsform.html", profilehasscorelogss=user, one_user=one_user, the_title="add new profilehasscorelogs", touslesmusical_pieces=touslesmusical_pieces, touslesprofiles=touslesprofiles)


    touslesmusical_pieces= query_db("select * from musical_pieces")

    touslesprofiles= query_db("select * from profiles")

    user = query_db('select * from profilehasscorelogs')
    one_user = query_db("select * from profilehasscorelogs limit 1", one=True)
    return render_template("profilehasscorelogsform.html", profilehasscorelogss=user, one_user=one_user, the_title="add new profilehasscorelogs", touslesmusical_pieces=touslesmusical_pieces, touslesprofiles=touslesprofiles)

@app.route("/add_one_hobbies", methods=["GET","POST"])
def add_one_hobbies():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into hobbies (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from hobbies')


        return render_template("hobbiesform.html", hobbiess=user, one_user=one_user, the_title="add new hobbies")


    user = query_db('select * from hobbies')
    one_user = query_db("select * from hobbies limit 1", one=True)
    return render_template("hobbiesform.html", hobbiess=user, one_user=one_user, the_title="add new hobbies")

