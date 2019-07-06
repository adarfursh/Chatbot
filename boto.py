"""
This is the template server side for ChatBot
"""

from bottle import route, run, template, static_file, request
import json
import random
import requests

api_address="http://api.openweathermap.org/data/2.5/weather?q=Yafo,IL&APPID=10749e247f626f6bbce403363572083a"

json_data = requests.get(api_address).json()
formatted_data  = json_data['weather'][0]['main']

jokes_list = ["Why did the programmer quit his job? Because he didn't get arrays.",
              "Did you know groups of bats can power things? They’re called bat-arrays",
              "I went to a street where the houses were numbered 8k, 16k, 32k, 64k, 128k, 256k and 512k.It was a trip down Memory Lane.",
              "!false (It’s funny because it’s true.)",
              "The best thing about a Boolean is that even if you are wrong, you are only off by a bit.",
              "'Debugging' is like being the detective in a crime drama where you are also the murderer.",
              "A programmer’s wife asks: 'Would you go to the shop and pick up a loaf of bread? And if they have eggs, get a dozen."
              "' The programmer returns home with 12 loaves of bread. 'They had eggs'."]

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg').lower()
    split_message = user_message.split()
    if check_swears(split_message):
        return json.dumps({"animation": "no", "msg": "Please write something more appropriate"})
    elif check_weather(user_message):
        return json.dumps({"animation": "crying", "msg": "Weather in Tel Aviv - Yafo: " + formatted_data})
    elif check_gs(user_message):
        return json.dumps({"animation": "giggling", "msg": "Golden State Blew a 3-1 lead. How may I further assist you?"})
    elif check_rapper(user_message):
        return json.dumps({"animation": "takeoff", "msg":  user_message +  " Biggie Smalls is the illest. How may I further assist you?  "})
    elif check_legend(user_message):
        return json.dumps({"animation": "inlove", "msg": "Walid Badir is the only legend on this planet! Anything else?"})
    elif check_richest(user_message):
        return json.dumps({"animation": "money", "msg": "Jeff Bezos is the richest person on this planet"})
    elif check_dog(user_message):
        return json.dumps({"animation": "dog", "msg": "Cecilia is the cutest dog on this planet"})
    elif check_boring(user_message):
        return json.dumps({"animation": "bored", "msg": "Takes one to know one"})
    elif check_afraid(user_message):
        return json.dumps({"animation": "afraid", "msg": "Robots are only afraid of water"})
    elif check_identity(user_message):
        return json.dumps({"animation": "confused", "msg": "Boto does not answer philosophical questions"})
    elif check_dance(user_message):
        return json.dumps({"animation": "dancing", "msg": "Look up...I'm killing it"})
    elif check_heartbrake(user_message):
        return json.dumps({"animation": "heartbroke", "msg": "I was once inlove with  W4-40"})
    elif check_condition (user_message):
        return json.dumps({"animation": "ok", "msg": "I'm functioning well. How can I help you?"})
    if tell_joke(user_message):
        return json.dumps({"animation": "laughing", "msg": random.choice(jokes_list)})
    else:
        return json.dumps({"animation": "excited", "msg": "It is nice to meet you. How may I assist you?"})


def check_swears(input):
    swear_words_list = ["arse", "ass", "asshole", ",bastard", "bitch", "bollocks", "child-fucker", "Christ on a bike",
                        "Christ on a cracker", "crap",
                        "cunt", "damn", "frigger", "fuck", "goddamn", "godsdamn", "hell", "holy shit", "horseshit",
                        "Jesus Christ", "Jesus fuck", "Jesus H. Christ",
                        "Jesus Harold Christ,", "Jesus wept", "Jesus, Mary and Joseph", "Judas Priest", "motherfucker",
                        "nigga", "nigger", "prick", "shit",
                        "shit ass", "shitass", "slut", "son of a bitch", "son of a motherless goat", "son of a whore",
                        "sweet Jesus", "twat"]
    if any(word in input for word in swear_words_list):
        return True


def check_dance(input):
    if input.find("dance") != -1 :
       return True

def check_heartbrake(input):
    if input.find("inlove") != -1 or input.find("love") != -1:
       return True

def check_condition(input):
    if input.find("what's up") != -1 or input.find("whats up") != -1 or input.find("how are you") != -1:
       return True


def check_identity(input):
    if input.find("who am i?") != -1 or input.find("who are you?") != -1 :
       return True

def check_boring(input):
    if input.find("you are boring") != -1 or input.find("boto is boring") != -1 :
       return True


def check_afraid(input):
    if input.find("afraid") != -1 and input.endswith("?") or input.find("scared") != -1 and input.endswith("?"):
       return True


def check_richest(input):
    if input.find("richest man") != -1 or input.find("richest woman") != -1 or input.find("richest person") != -1 :
       return True

def check_dog(input):
    if input.find("sweetest dog") != -1 or input.find("best dog") != -1 or input.find("cutest dog") != -1 and input.ednswith("?"):
        return True

def tell_joke(input):
    if input.find("joke") != -1 :
        return True

def check_gs(input):
    if input.find("golden") != -1 and input.find("state") != -1:
        return True

def check_legend(input):
    if input.find("living legend") != -1:
        return True


def check_rapper(input):
    if input.find("best") != -1 and input.find("rapper") != -1 and input.endswith("?"):
        return True

def check_weather(input):
    if input.find("weather") != -1 and input.endswith("?"):
        return True

@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})



@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
