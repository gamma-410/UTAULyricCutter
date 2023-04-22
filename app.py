from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        lyric = request.form.get("lyric")
        lyricCut = lyric.split()
        lyricData = []
        x = 0

        for i in lyricCut:
            if x == 0:
                lyricData.append(["-", i])

            if x >= 1:
                if lyricData[x-1][1] in ["あ", "か", "が", "さ", "ざ", "た", "だ", "な", "は", "ば", "ぱ", "ま", "や", "ら", "わ"]:
                    lyricData.append(["a", i])

                elif lyricData[x-1][1] in ["い", "き", "ぎ", "し", "じ", "ち", "ぢ", "に", "ひ", "び", "ぴ", "み", "い", "り", "い"]:
                    lyricData.append(["i", i])

                elif lyricData[x-1][1] in ["う", "く", "ぐ", "す", "ず", "つ", "づ", "ぬ", "ふ", "ぶ", "ぷ", "む", "ゆ", "る", "う"]:
                    lyricData.append(["u", i])

                elif lyricData[x-1][1] in ["え", "け", "げ", "せ", "ぜ", "て", "で", "ね", "へ", "べ", "ぺ", "め", "え", "れ", "え"]:
                    lyricData.append(["e", i])

                elif lyricData[x-1][1] in ["お", "こ", "ご", "そ", "ぞ", "と", "ど", "の", "ほ", "ぼ", "ぽ", "も", "よ", "ろ", "を"]:
                    lyricData.append(["o", i])

                elif lyricData[x-1][1] == "ん":
                    lyricData.append(["-", i])

            x += 1

        utau_lyrics = ""

        for note in lyricData:
            utau_lyrics += '"' + note[0] + " " + note[1] + '" '

        utau_lyrics = utau_lyrics.strip()

        return render_template("output.html", lyric=utau_lyrics)


if __name__ == "__main__":
    app.run(debug=True)
