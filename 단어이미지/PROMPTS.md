# 단어 그림 — 남은 것 프롬프트

현재 **29장 확보 / 31장 남음**
(단어가족 17 + 문장빈칸 10 + 재작업 4. `vet`은 양쪽에 쓰여 한 번만 만들면 됨)

---

## 0. 규격

| 항목 | 값 |
|---|---|
| 생성 크기 | **1254 × 1254** (지금까지 중 결과가 제일 좋았던 크기) |
| 한 장에 | **4개까지** — 그 이상은 개당 화질이 떨어짐 |
| 배경 | **투명** 또는 순백. 둘 다 자동 처리됨 |
| 넣을 곳 | `파커시우\_새단어그림\` — 파일명 아무거나 |

라벨(`ham png` 같은 글자)은 자동으로 잘라내니 붙어 나와도 괜찮습니다. 다만 라벨 자리만큼 그림이 작아집니다.

---

## 1. 스타일 프리픽스 — 앞에 붙일 것

```
Flat vector illustration for a children's phonics workbook, single centered
object, simple bold shapes, bright friendly colors, thick clean outlines,
soft cel shading, front view, centered with even margins, plain transparent
background, no text, no letters, no words, no watermark, no border
```

## 2. 제약 — 반드시 같이 넣을 것 ⚠️

지난 4배치에서 **칸의 절반이 버려졌습니다.** AI가 비슷한 소리 단어로 알아서 뻗어나가서입니다.
(`plan` `den` `pot` `box` `fox` `sock` `top` `bus` `cup` `rug` `duck` `star` `cow` `pet` … 전부 폐기)

```
Draw ONLY the words I list. Do not add similar-sounding words.
Do not create variants of the same word (no pig_in_mud, no pan_fry).
One image per listed word, no duplicates.
```

---

# A. 단어 가족 — 17개

## 1장 · `-eg` + lap

| 파일명 | Subject |
|---|---|
| `leg.png` | a girl standing and lifting one leg forward, that raised leg highlighted |
| `keg.png` | a brown wooden barrel keg with metal hoops |
| `peg.png` | a single wooden clothespin peg, diagonal |
| `lap.png` | a boy sitting on a chair seen from the side, **the flat top of his thighs highlighted horizontally** |

> `lap` 은 재작업입니다. 지난번 것은 강조선이 **다리 옆선**을 따라 그려져서 `leg` 로 읽혔습니다.
> 허벅지 **윗면을 가로 방향**으로 강조해야 '무릎에 앉히는 그 lap' 이 됩니다.

## 2장 · `-en` + `-et`

| 파일명 | Subject |
|---|---|
| `ten.png` | the numeral 10 in big friendly blue 3D digits |
| `men.png` | **two** adult men standing side by side, smiling |
| `vet.png` | a veterinarian in a white coat holding a puppy, a cat sitting beside |
| `wet.png` | a boy soaking wet, water dripping off him, a puddle at his feet |

> `ten.png` 만 숫자가 필요합니다. **이 장은 프리픽스에서 `no numbers` 만 빼고** 생성하세요.
> (`no letters, no words` 는 그대로 둬야 나머지 3장에 글자가 안 들어옵니다.)
> `men` 은 반드시 두 명. 이미 있는 `man`(한 명)과 구별돼야 합니다.
> `vet` 은 반드시 동물과 함께. 동물이 없으면 그냥 의사입니다.

## 3장 · `-ig`

| 파일명 | Subject |
|---|---|
| `dig.png` | a boy digging a hole in brown soil with a shovel |
| `wig.png` | a brown curly wig on a wig stand |
| `big.png` | one huge red apple next to one tiny red apple, size contrast obvious |

> `big` 은 **비교 대상이 반드시 같이** 있어야 합니다. 큰 사과 하나만 그리면 그냥 `apple` 입니다.

## 4장 · `-ip`

| 파일명 | Subject |
|---|---|
| `lip.png` | a pair of red lips, close-up, on their own |
| `hip.png` | a boy standing with both hands on his hips, hip area marked with a red circle |
| `sip.png` | a boy sipping a drink through a straw from a cup |

> 이미 있는 `sit`(의자에 앉은 아이)과 `sip`(빨대로 마시는 아이)이 헷갈리지 않게,
> `sip` 은 **컵과 빨대가 확실히 보이게** 해주세요.

## 5장 · `-it`

| 파일명 | Subject |
|---|---|
| `kit.png` | a grey first aid kit box with a red cross on it |
| `hit.png` | a boy in a red cap swinging a baseball bat to hit |
| `pit.png` | a peach cut open showing the large brown pit stone inside |

> 이미 있는 `bat`(야구 방망이만)과 `hit`(방망이를 **휘두르는 아이**)의 차이가 보여야 합니다.

---

# B. 문장 빈칸 — 10개

`vet` 은 A의 2장에 있으니 여기서 또 만들지 마세요.
이쪽은 **문장에서 정답을 하나로 확정하는 역할**이라 애매하면 문제가 깨집니다.

## 6장 · 우선순위 높음

| 파일명 | Subject |
|---|---|
| `mail_carriers.png` | **four** mail carriers in blue uniforms with mail bags, standing in front of a post office |
| `cousin.png` | a simple family tree: two children connected to two sibling parents, the cousin child circled |
| `police_officer.png` | a police officer in a blue uniform with a badge and cap, waving |
| `fire_fighter.png` | a firefighter in a red helmet and yellow coat holding a hose |

> `mail_carriers` 는 반드시 **여러 명**. 지금 폴백인 📮(우체통)이 문장의 "at the post office" 와
> 겹쳐서 장소를 가리키는지 직업을 가리키는지 헷갈리는 게 원래 문제였습니다.
> `cousin` 은 '사촌'이 생김새가 아니라 **관계**라서 아이 한 명 그림으로는 특정이 안 됩니다. 관계도가 필요합니다.

## 7장 · 가족

| 파일명 | Subject |
|---|---|
| `family.png` | a family of four — father, mother, son, daughter — standing together, smiling |
| `sister.png` | one girl with long hair in a pink dress, waving |
| `brother.png` | one boy with short hair in a blue shirt, waving |

## 8장 · 장소

| 파일명 | Subject |
|---|---|
| `park.png` | a green park with trees, a bench, a slide and a swing |
| `gym.png` | an indoor gym with dumbbells, a treadmill and a blue exercise ball |
| `school.png` | a school building with a clock tower, a flag and a front yard |

---

# C. 재작업 — 4개 (급하지 않음)

첫 배치에서 온 저해상도입니다. 한 장에 6개를 넣어서 개당 300px 아래로 쪼그라들었습니다.

| 파일명 | 현재 | Subject |
|---|---|---|
| `can.png` | 172×276 | a silver aluminium tin can, plain, no label |
| `cat.png` | 268×274 | an orange tabby cat sitting, facing forward, smiling |
| `jam.png` | 272×240 | a glass jar of red strawberry jam next to a slice of bread spread with jam |
| `net.png` | 284×273 | a volleyball net stretched between two wooden posts on grass |

---

# 만들지 않는 것

- **`Ted`, `Meg`** — 고유명사라 그림으로 특정 불가. 남자아이를 그려도 그게 Ted인지 알 방법이 없고,
  워크북처럼 옷에 이름을 쓰면 파닉스 퀴즈에서 정답이 그대로 노출됩니다. 텍스트 모드로만 출제됩니다.
- **o / u 계열** (`box` `fox` `pot` `bus` `cup` `rug` …) — 이 워크북은 단모음 **a / e / i** 만 다룹니다.
  이미 만들어진 것들은 `_새단어그림` 에 남겨뒀으니 나중에 확장하면 씁니다.

---

# 완료된 것 (다시 만들지 마세요)

```
-am  ham jam dam ram          -at  bat cat hat mat
-an  can fan man pan          -ed  bed red wed
-ap  cap map nap              -in  bin fin pin win
-ig  pig    -ip  zip    -it  sit    -en  hen pen    -et  jet net
```
