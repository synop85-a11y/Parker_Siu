# 🦁 파커-시우 영어

아들을 위한 영어 학습 PWA. 패드 가로 모드 기준이며 폰 세로도 대응한다.

시즌 1과 시즌 2가 별도 페이지로 나뉘어 있고, 진행도도 따로 저장된다.

| | 파일 | 교재 | 문항 |
|---|---|---|---|
| 시즌 1 | `index.html` | book1 ~ book5 | 402 |
| 시즌 2 · 위인관 | `season2.html` | book9 ~ book12 | 184 |

---

## 📦 구성

```
Parker_Siu/
├── index.html               시즌 1 (단어 게임 + 공룡 카드 도감)
├── season2.html             시즌 2 (6개 세션 + 시험모드 + 위인관)
├── english_textbooks.json   교재 9권 · 586문항
├── manifest.json            PWA 설정
├── sw.js                    서비스 워커 (오프라인)
├── icon-192.png             앱 아이콘
├── icon-512.png             앱 아이콘 (큰 사이즈)
├── _sync_word_images.py     단어 그림 ↔ 데이터 동기화 도구
│
├── 단어이미지/              단어 그림 56장 (파일명 = 단어 slug)
├── 위인카드/                위인 그림 99장 (시대별 9폴더)
├── 위인카드_원본/           압축 전 원본 (309MB · git 제외)
└── cards/                   공룡 카드 20장
```

---

## 🎮 시즌 1 (`index.html`)

- 4지선다 단어 게임 (이모지 ↔ 단어)
- 단어별 레벨업: 🌱 → 🌿 → 🌸 → 🌳 → ⭐
- **공룡 카드 도감** — 정답 보상으로 카드 20종 수집
- 별 획득 시스템

저장 키: `lion_english_progress_v1`, `lion_english_stars_v1`, `lion_english_cards_v1`

## 🎮 시즌 2 (`season2.html`)

세션 6종:

| | 세션 | 내용 | 교재 |
|---|---|---|---|
| 📖 | 단어 배우기 | 그림→영단어, 영단어→그림 | book10, 11 |
| 🔤 | 파닉스 | 첫 글자 찾기, 듣고 고르기 | book9, 10, 11 |
| 📝 | 문장 만들기 | 빈칸 채우기 | book10, 11 |
| 🎵 | 단어 가족 | 소리↔단어, 그림↔단어 | book12 |
| 🎤 | 말하기 연습 | 문장 말하기 (**부모가 채점**) | book10, 11 |
| ✍️ | 쓰기 연습 | | book9~12 |

추가 기능:

- **시험 모드** — 별은 처음 맞춘 문제에만 부여
- **🏛️ 위인관** — 한국사 위인 99명 카드 수집
- 중의적 보기 동시 등장 금지 (헷갈리는 선택지 배제)

저장 키: `parker_siu_s2_progress`

### 위인관 구성

| 시대 | 인원 | 시대 | 인원 |
|---|---|---|---|
| 고조선 | 2 | 고려 | 15 |
| 고구려 | 8 | 조선 | 38 |
| 백제 | 8 | 근대 | 15 |
| 신라 | 9 | 발해 | 2 |
| 후삼국 | 2 | **합계** | **99** |

이미지 경로는 `위인카드/{시대폴더}/{이름}.png` 로 조립된다.

---

## 🖼️ 단어 그림 추가하기

앱은 폴더 목록을 읽을 수 없으므로, 어떤 단어에 그림이 있는지 **데이터에 표시**해야 한다.

1. `단어이미지/` 에 PNG 추가. 파일명은 단어를 소문자·언더바로 (`fire_fighter.png`)
2. 동기화 실행

```bash
python _sync_word_images.py
```

`english_textbooks.json` 의 각 문항에 `has_image: true` 가 붙고, 앱은 그림이 있으면 그림을, 없으면 이모지를 쓴다. 실행하면 어느 문항에도 안 쓰이는 그림도 알려준다.

현재: 그림 56장 → 97문항에 연결됨.

---

## 📚 교재 데이터

`english_textbooks.json` — 9권 586문항.

| 교재 | 문항 |
|---|---|
| book1_sight_words | 80 |
| book2_alphabet_phonics | 115 |
| book3_common_core_sight_words | 80 |
| book4_themed_speaking_vol2 | 57 |
| book5_themed_speaking_vol1 | 70 |
| book9_phonics_sound | 24 |
| book10_my_family | 60 |
| book11_our_community | 52 |
| book12_word_family | 48 |

문항 유형 10종: `vocab` `vocabulary` `phonics_word` `sight_word` `letter`
`content_vocab` `sentence` `sentence_fill` `sentence_pattern` `place_action`

---

## 🚀 배포 (GitHub Pages)

`main` 브랜치에 push 하면 자동 반영된다.

```
https://synop85-a11y.github.io/Parker_Siu/
```

> ⚠️ `단어이미지/` 와 `위인카드/` 도 반드시 커밋되어야 한다.
> 로컬에만 있으면 배포판에서 그림이 전부 깨진다.

### 패드에 설치

**iPad (Safari)** — 공유 버튼 📤 → "홈 화면에 추가"
**Android (Chrome)** — 메뉴 ⋮ → "홈 화면에 추가"

설치 후 전체화면 앱처럼 실행되고, 진행도는 패드에 저장된다 (localStorage).

---

## 🔧 로컬 테스트

```bash
python -m http.server 8000
```

`http://localhost:8000` 접속.

PWA 기능(서비스 워커·홈 화면 추가)까지 확인하려면 HTTPS가 필요하다.
상위 폴더의 `_serve_https.py` 와 `_certs/` 를 쓴다.

---

## 🛠️ 소재 처리 스크립트

상위 폴더에 있다.

| 스크립트 | 용도 |
|---|---|
| `_add_cards.ps1` | 새 카드 이미지 편입 |
| `_rename_cards.ps1` | 파일명 정리 |
| `_compress_images.ps1` | 원본 → 배포용 압축 |
| `_serve_https.py` | 로컬 HTTPS 서버 |

작업 대기 폴더: `_새위인/` `_새문제집/` `_새단어그림/`

---

만든 사람: 빛 + Claude
