import csv

# CSVファイルから国名とカウントを読み込む
def read_country_counts():
    countries = {}
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # ヘッダー行をスキップ
            for row in reader:
                country, count = row
                countries[country] = int(count)
    except FileNotFoundError:
        pass
    return countries

# CSVファイルに国名とカウントを更新する
def update_country_count(favorite_place, countries):
    countries[favorite_place] = countries.get(favorite_place, 0) + 1
    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['country_name', 'count'])
        for country, count in countries.items():
            writer.writerow([country, count])

# 最もカウントが多い国を取得する
def get_most_favorite_country(countries):
    return max(countries, key=countries.get, default=None)

# ユーザー入力を受け取るコード
name = input("あなたの名前を入力してください: ")
name = name.strip()
if name != "":
    print(f"こんにちは{name}さん！")

        # CSVファイルから国名とカウントを読み込む
    countries = read_country_counts()
    most_favorite = get_most_favorite_country(countries)

    if most_favorite:
        while True:

            response = input(f"お勧めの国は{most_favorite}です。{name}さんも{most_favorite}は好きですか？ (yes/no)：").strip().lower()
            if response == "yes":
                update_country_count(most_favorite, countries)
                print("答えてくれてありがとう！")
                exit()  # プログラムを終了する
            elif response == "no":
                # カウントが同数の国を探す
                max_count = countries[most_favorite]
                same_count_countries = [country for country, count in countries.items() if count == max_count and country != most_favorite]
                if same_count_countries:
                    for country in same_count_countries:
                        while True:
                            response = input(f"{name}さんは{country}は好きですか？ (yes/no)：").strip().lower()
                            if response == "yes":
                                update_country_count(country, countries)
                                print("答えてくれてありがとう！")
                                exit()
                            elif response == "no":
                                break
                            else:
                                print("yesかnoで答えてください!")
                    break  # すべての国を尋ねた後にループを抜ける
                else:
                    break  # 同数の国がない場合にループを抜ける
            else:
                print("yesかnoで答えてください！")



    
    while True:
        favorite_place = input(f"{name}さん、好きな国はどこですか？：")
        favorite_place = favorite_place.strip()
        
        # 入力が空でなく、文字列であることを確認
        if favorite_place != "" and not favorite_place.isdigit():
            # 各単語の最初の文字を大文字にする
            favorite_place = favorite_place.title()
            # CSVファイルにカウントを記録する
            update_country_count(favorite_place,countries)
            print("答えてくれてありがとう！")
            break
        else:
            print("空白か数値が入っています！正しい国名を入力してください！")
else:
    print("名前が入力されてません！。再度お試しください！")




