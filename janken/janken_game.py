import じゃんけん_ai


def main():
    hands = ["グー", "チョキ", "パー"]
    while True:
        user_hand = input ("グー・チョキ・パーを入力（終了するには 'q' ）: ").strip().replace("ｑ", "q")
        if user_hand == "q":
            break
        if user_hand not in hands:
            print("無効な入力です。もう一度試してください。")
            continue

        computer_hand = じゃんけん_ai.get_computer_hand()
        print(f"コンピュータの手:{computer_hand}")

        if user_hand == computer_hand:
            print("引き分け")
        
        elif (user_hand == "グー" and computer_hand == "チョキ") or\
             (user_hand == "チョキ" and computer_hand == "パー")or\
             (user_hand == "パー" and computer_hand == "グー"):
            print("あなたの勝ち")

        else:
            print("コンピュータの勝ち")

        じゃんけん_ai.update_history(user_hand)

if __name__ == "__main__":
    main()
