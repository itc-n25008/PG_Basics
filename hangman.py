    if "__"not in board:
        print("あなたの勝ち")

    if not win:
        print("\n".join(stages[0:wrong]))
        print("あなたの負け！正解は{}.".format(word))

    hangman("cat")
