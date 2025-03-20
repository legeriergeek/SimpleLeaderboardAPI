import hug
import json

with open("data.json", "r") as f:
    data = json.load(f)

@hug.get('/add_player')
def add_player(username, score:hug.types.number=1):
    """Adds player to the 'db'"""
    new_user = {"username": username, "score": score}
    data["users"].append(new_user)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return("User succesfully added!")

@hug.get('/get_users')
def get_users():
    """Gets all users in the 'db'"""
    return(data)

@hug.get('/get_user_info')
def get_user_info(username):
    """Gets user info based on the username"""
    user_info = next((user for user in data["users"] if user["username"] == username), None)
    return(user_info)

@hug.get('/get_player_score')
def get_player_score(username):
    """Gets specified player's score"""
    user_info = next((user for user in data["users"] if user["username"] == username), None)
    return(user_info["score"])

@hug.get('/get_player_score')
def get_player_score(username):
    """Gets specified player's score"""
    user_info = next((user for user in data["users"] if user["username"] == username), None)
    return(user_info["score"])
    

@hug.get('/update_player_score')
def get_player_score(username, score:hug.types.number=1):
    """Gets specified player's score"""
    user_info = next((user for user in data["users"] if user["username"] == username), None)
    user_info["score"] = score
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return("Score modified sucessfully!")

@hug.get('/remove_user')
def remove_user(username):
    """Removes specified user"""
    user_info = next((user for user in data["users"] if user["username"] == username), None)
    data["users"].remove(user_info)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return("User sucessfully removed!")





