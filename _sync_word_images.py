# -*- coding: utf-8 -*-
"""단어이미지/ 폴더를 훑어서 english_textbooks.json 의 각 문항에 has_image 를 표시한다.

앱은 폴더 목록을 읽을 수 없으므로, 어떤 단어에 그림이 있는지 데이터로 알려줘야
'그림이 있으면 그림, 없으면 이모지' 를 요청 없이 즉시 판단할 수 있다.

그림을 추가/삭제한 뒤 이 파일을 다시 실행하면 된다:
    python _sync_word_images.py
"""
import json, os, shutil, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(ROOT, "english_textbooks.json")
IMGD = os.path.join(ROOT, "단어이미지")


def slug(w):
    return str(w or "").lower().strip().replace(" ", "_")


have = {os.path.splitext(f)[0] for f in os.listdir(IMGD) if f.lower().endswith(".png")}

with open(JSON, encoding="utf-8") as f:
    d = json.load(f)

shutil.copy2(JSON, JSON + ".bak3")

on = off = 0
for it in d["items"]:
    it.pop("no_image", None)          # 예전 표시는 has_image 로 통합
    if it.get("word") and slug(it["word"]) in have:
        it["has_image"] = True
        on += 1
    else:
        it.pop("has_image", None)
        off += 1

d["meta"]["word_images"] = {"files": len(have), "items_with_image": on}

with open(JSON, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"그림 파일 {len(have)}장")
print(f"has_image 표시: {on}문항 / 없음 {off}문항")
by = collections.Counter(i.get("book") for i in d["items"] if i.get("has_image"))
for k, v in sorted(by.items()):
    print(f"  {k}: {v}")
unused = sorted(have - {slug(i.get("word")) for i in d["items"]})
if unused:
    print(f"어느 문항에도 안 쓰이는 그림: {unused}")
