import csv

# csvファイルに国名、カウントを記入する
def update_favorite_place_count(favorite_place):
    countries = {}
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # ファイルが空でないか確認する
            try:
                next(reader)  # ヘッダー行をスキップ
            except StopIteration:
                # ファイルが空の場合、ここでエラーが発生する
                pass
            for row in reader:
                country, count = row
                countries[country] = int(count)
    except FileNotFoundError:
        # ファイルが存在しない場合
        pass

    # カウントを更新する
    countries[favorite_place] = countries.get(favorite_place, 0) + 1

    # CSVファイルに書き戻す
    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['country_name', 'count'])  # ヘッダー行を書き込む
        for country, count in countries.items():
            writer.writerow([country, count])


# ユーザー入力を受け取るコード
name = input("あなたの名前を入力してください: ")
name = name.strip()
if name != "":
    print(f"こんにちは{name}さん！")
    while True:
        favorite_place = input(f"{name}さん、好きな国はどこですか？：")
        favorite_place = favorite_place.strip()
        
        # 入力が空でなく、文字列であることを確認
        if favorite_place != "" and not favorite_place.isdigit():
            # 各単語の最初の文字を大文字にする
            favorite_place = favorite_place.title()
            # CSVファイルにカウントを記録する
            update_favorite_place_count(favorite_place)
            print("答えてくれてありがとう！")
            break
        else:
            print("空白か数値が入っています！正しい国名を入力してください！")
else:
    print("名前が入力されてません！。再度お試しください！")




