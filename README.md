---
 titile: glucolog2csv
---

# これは何？

@flameeyes さんの glucometerutils で出力したログを日ごとのCSVに変換します
自分がWindows10ユーザなので、Windows10のコマンドラインでしか試していません...

# 使い方

```
 # 予めglucometerutils でログを出力します
 @python3 glucometer.py --driver fsprecisionneo dump > somefile.txt

 # 出力したログを取り込みます
 python glucolog2csv.py somefile.txt
 ```
