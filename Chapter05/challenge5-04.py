zisyo = {"身長":"153cm","好きな色":"青","好きなゲーム":"ゼンレスゾーンゼロ"}
n = input("入力してください")
if n in zisyo:
    zisyo = zisyo[n]
    print(zisyo)
else:
    print("見つかりませんでした。")

