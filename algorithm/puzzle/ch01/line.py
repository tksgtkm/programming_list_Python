"""
FとBの2要素からなる配列が与えられて、
配列内の要素をFかBのどちらかの方向に揃えるようにしたい
最小回数で揃える方法を見つける

capsならFだと4回変換する処理がはいるが、
Bだと3回変換する処理で済む
"""

caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]


def pleaseConform(caps):
    # 初期化
    """
    アルゴリズムで使う変数を初期化
    各区間は最初の２つが数、3番目が'F'か'B'の文字列ラベルという3要素タプル
    前の2数が区間の両端を表す
    区間の両端は閉じており、両端の位置を含む。
    変数intervalsは区間タプルのリストで、初期値は空リストです。
    変数forwardとbackwardは前向き区間と後ろ向き区間の個数を数える。初期値は0
    """
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # どこで同じ方向に揃えるか間隔を決定する
    """
    forループでは区間の計算を行う。
    len(caps)は13を返す。
    capsのリスト要素が0から12という番号であることに注意する。
    (例えば、caps[0] = 'F', caps[12] = 'F')

    キーワードrangeの引数は1, 2, 3このどれでも構わない。
    range(len(caps))なら変数iは0から始まり、len(caps) - 1まで1ずつ増える。
    変数startは0から始まり、caps[start]と異なるcaps[i]が見つかるまでiが増やされる。
    このチェックはif文で行われる。
    if文の述語部caps[start] != caps[i]がTrueだと区間が一つ終わり、このiから次の区間が始まる。
    求まった区間はstartから始まり、i - 1で終わる。
    決定した区間はリストintervalsに開始位置、終了位置、'F'か'B'の区間の種類という3つ組のタプル
    として追加される。
    その後前向き区間化後ろ向き区間の種類に応じて区間の個数を増やす。
    """
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # intervalsは(start, end, type)の3要素を含む区間タプルを含むリスト
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == "F":
                forward += 1
            else:
                backward += 1
            start = i

    # ループ処理のあとにインターバル最後へ加える必要がある
    """
    最後の区間は区間を通り越したとわかってから追加する。
    """
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == "F":
        forward += 1
    else:
        backward += 1

    """
    どちらの区間を逆向きにするか決定する。
    小さい方の集合を選ぶ。
    forループはintervalsの区間tについてイテレーションし、
    前向きか後ろ向きか選ばれた種類の区間に対して命令を表示する。
    各tは区間情報の3つ組で表示対象の命令の開始位置と終了位置を与える。
    タプルtについてはt[0]が区間開始、t[1]が区間終了、t[2]が種類を示す。
    """
    if forward < backward:
        flip = "F"
    else:
        flip = "B"
    for t in intervals:
        if t[2] == flip:
            print("People in positions", t[0], "through", t[1], "flip your caps!")


pleaseConform(cap2)
