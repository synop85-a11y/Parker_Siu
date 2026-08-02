# 단어 그림 — 남은 것 프롬프트

**시즌2(book9~12) 기준. 15장.**

기존 A/B 배치(단어가족·문장빈칸)는 완료됐습니다. 이번 건은 **이모지로는 원리적으로
구분이 안 되는 단어들**입니다. 방은 유니코드에 이모지 자체가 없고, 나머지는
서로 같은 이모지를 씁니다.

| 단어 | 현재 이모지 | 무엇과 겹치나 |
|---|---|---|
| bedroom | 🛏️ | `bed` (그림 있음) 와 같은 침대 |
| living room / sofa | 🛋️ | 둘 다 소파 |
| bathroom | 🚽 | 변기 ≠ 욕실 |
| room | 🚪 | 문 ≠ 방 |
| kitchen | 🍳 | 프라이팬 ≠ 부엌 |
| father / dad | 👨 | 서로, 그리고 `man`(그림 있음) 과도 |
| mother | 👩 | `mom` 과 |
| princess / queen | 👸 | 서로 |
| chair | 🪑 | `desk` 와 |
| crown | 👑 | `king` 과 |
| bug | 🐛 | `worm` 과 |
| rabbit | 🐰 | `bunny` 와 |

---

## 0. 규격

| 항목 | 값 |
|---|---|
| 생성 크기 | **1254 × 1254** |
| 한 장에 | **4개까지** |
| 배경 | **투명** 또는 순백 |
| 넣을 곳 | `파커시우\_새단어그림\` — 파일명 아무거나 |

라벨 글자는 자동으로 잘라냅니다.

## 1. 스타일 프리픽스 — 앞에 붙일 것

```
Flat vector illustration for a children's phonics workbook, single centered
object, simple bold shapes, bright friendly colors, thick clean outlines,
soft cel shading, front view, centered with even margins, plain transparent
background, no text, no letters, no words, no watermark, no border
```

## 2. 제약 — 반드시 같이 넣을 것 ⚠️

```
Draw ONLY the words I list. Do not add similar-sounding words.
Do not create variants of the same word.
One image per listed word, no duplicates.
```

---

# 1장 · 방 (4개) 🔴 최우선

방은 **가구 하나가 아니라 방 전체**가 보여야 합니다. 침대만 그리면 `bed` 가 되고,
소파만 그리면 `sofa` 가 됩니다. 정면에서 잘라낸 단면(cutaway) 구도로 요청하세요.

프리픽스에서 `single centered object` 를 빼고 아래를 씁니다.

```
Flat vector illustration for a children's phonics workbook, simple bold shapes,
bright friendly colors, thick clean outlines, soft cel shading, plain
transparent background, no text, no letters, no words, no watermark, no border

Draw ONLY the words I list. Do not add similar-sounding words.
Do not create variants of the same word. One image per listed word, no duplicates.

Draw these 4 as cutaway room interiors seen straight from the front, showing
the WHOLE room with its walls, floor and furniture together:

1. bedroom - bed with pillow and blanket, nightstand with a lamp, window
2. living room - sofa, TV on a stand, rug, floor lamp
3. bathroom - bathtub, sink with mirror, toilet
4. kitchen - counter, sink, stove with a pot, refrigerator
```

> 각 방에 **가구가 2개 이상** 있어야 "방"으로 읽힙니다.
> 하나만 크게 그리면 그 가구 이름이 되어버립니다.

# 2장 · room + 가족 (4개) 🔴

```
[프리픽스 + 제약]

1. room - a simple empty room interior seen from the front, with a door on the
   wall, one window, wooden floor and plain walls, no furniture
2. father - a smiling adult man wearing a shirt, holding the hand of a small
   child who stands beside him, full body
3. mother - a smiling adult woman wearing a blouse, holding a baby in her arms,
   full body
4. chair - a single wooden chair with four legs and a tall backrest, seen at a
   three-quarter angle, nothing else
```

> `father` 는 **아이와 함께** 있어야 `man`(혼자 선 남자)과 구별됩니다.
> `mother` 도 마찬가지로 아기가 있어야 그냥 여자가 아닙니다.
> `chair` 는 등받이가 확실히 보여야 `desk` 와 갈립니다.

# 3장 · 왕실 + 사물 (4개) 🟠

```
[프리픽스 + 제약]

1. princess - a young girl in a pink ball gown with a small tiara, smiling,
   full body, no throne
2. queen - a grown woman in a long purple robe with a large golden crown,
   holding a scepter, sitting on a throne, full body
3. crown - a golden crown with red jewels resting on a purple velvet cushion,
   no person wearing it
4. sofa - a long three-seat couch with cushions, seen from the front,
   nothing else around it
```

> `princess`(어린 소녀·작은 티아라)와 `queen`(어른·큰 왕관·왕좌)의 차이를
> 나이와 소품으로 확실히 벌려야 합니다.
> `crown` 은 **아무도 쓰고 있지 않아야** `king`/`queen` 과 안 겹칩니다.

# 4장 · 동물 + dad (3개) 🟡

```
[프리픽스 + 제약]

1. bug - a round ladybug with red shell and black spots, six legs, seen from
   above
2. rabbit - a white rabbit with long upright ears sitting on grass, side view
3. dad - a young smiling father in casual clothes carrying a small child on his
   shoulders, full body
```

> `bug` 는 **무당벌레처럼 다리 있는 곤충**이어야 `worm`(다리 없는 지렁이)과 갈립니다.
> `dad` 는 `father` 와 다른 구도로 (목말 태우기) 해야 둘 다 살릴 수 있습니다.

---

## 받은 뒤 처리

시트를 `_새단어그림\` 에 넣고 알려주시면 제가 잘라서 넣습니다. 직접 하시려면:

```bash
# 칸 위치 미리보기
python _split_sheet.py "_새단어그림/파일.png"

# 왼쪽위 → 오른쪽 → 다음 줄 순서로 이름 지정, 건너뛸 칸은 -
python _split_sheet.py "_새단어그림/파일.png" bedroom living_room bathroom kitchen

# _cut/ 확인 후 옮기고 동기화
cp _cut/*.png Parker_Siu/단어이미지/
cd Parker_Siu && python _sync_word_images.py
```
