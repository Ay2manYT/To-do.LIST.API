import requests

BASE_URL = "http://127.0.0.1:8000"


def post_note(title, text):
    res = requests.post(f"{BASE_URL}/notat", json={
        "title": title,
        "text": text
    })
    print(res.status_code)


def get_notes():
    res = requests.get(f"{BASE_URL}/notat")
    print(res.json())


def get_note(note_id):
    res = requests.get(f"{BASE_URL}/notat/{note_id}")
    print(res.json())

inn = -1
while inn != "4":
	inn = input("1. Nytt notat\n2. Se notater\n3. hent spesefikk notat\n4. avslutt\n: ")
	if inn  == "1":
		post_note(input("tittel: "), input("tekst: "))
	elif inn == "2":
		print(get_notes())
	elif inn == "3":
		get_note(input("skriv inn id: "))
