import random

history = {"グー":0, "チョキ":0, "パー":0}

def get_computer_hand():
    if sum(history.values()) == 0:
        return random.choice(["グー", "チョキ", "パー"])
    
    else:
        most_common_hand = max(history, key=history.get)
        counter_hand = {"グー": "パー", "チョキ": "グー", "パー": "チョキ"}
        return counter_hand[most_common_hand]
    
def update_history(user_hand):
    if user_hand in history:
        history[user_hand] += 1
