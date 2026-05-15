# 🦁 라이언 영어 (Lion English)

아들을 위한 영어 학습 PWA 게임. 패드 가로 모드 최적화.

## 📦 포함 파일

```
lion-english/
├── index.html              # 게임 메인
├── manifest.json           # PWA 설정
├── sw.js                   # 서비스 워커 (오프라인)
├── english_textbooks.json  # 5권 교재 데이터
├── icon-192.png            # 앱 아이콘
└── icon-512.png            # 앱 아이콘 (큰 사이즈)
```

---

## 🚀 GitHub Pages 배포 방법

### 1. GitHub 계정에 로그인 후 새 저장소 생성
- 저장소 이름: 자유 (예: `lion-english`)
- **Public**으로 설정 (Private은 GitHub Pages 무료 안 됨)

### 2. 파일 6개 전부 업로드
- GitHub 저장소 페이지에서 "Add file" → "Upload files"
- 위의 6개 파일을 드래그해서 올림
- 하단에 "Commit changes" 클릭

### 3. GitHub Pages 활성화
- 저장소 페이지 상단 **Settings** 탭 클릭
- 왼쪽 메뉴에서 **Pages** 클릭
- "Source" 섹션에서:
  - Branch: `main` (또는 `master`)
  - Folder: `/ (root)`
  - **Save** 클릭
- 1~2분 후 페이지 새로고침하면 URL이 나옴
  - 형식: `https://[계정명].github.io/[저장소명]/`

### 4. 패드에서 앱처럼 설치

**iPad (Safari):**
1. Safari로 위 URL 접속
2. 하단 공유 버튼 (📤) 탭
3. "홈 화면에 추가" 선택
4. 이름 확인 후 "추가"
5. 홈 화면에 🦁 라이언 영어 아이콘 생성됨

**Android 태블릿 (Chrome):**
1. Chrome으로 URL 접속
2. 우측 상단 메뉴 (⋮) 탭
3. "홈 화면에 추가" 선택
4. 홈 화면에 아이콘 생성됨

설치 후 아이콘 탭하면 전체화면 앱처럼 실행됨. 진행도는 패드에 자동 저장 (localStorage).

---

## 🎮 게임 기능

- **5권 교재** 297개 단어/문장 수록
- **레벨업 시스템**: 단어마다 정답 누적 → 🌱→🌿→🌸→🌳→⭐
- **4지선다**: 이모지↔단어 매칭
- **자동 저장**: 패드를 꺼도 진행도 유지
- **오프라인 지원**: 한번 접속하면 인터넷 없어도 동작
- **사운드**: BGM + 효과음 (우측 상단 토글로 끄기/켜기)

## 🔧 로컬에서 테스트 (개발용)

배포 전에 PC에서 테스트하려면:

```bash
cd lion-english
python3 -m http.server 8000
```

브라우저로 `http://localhost:8000` 접속.

---

## 💾 진행도 데이터

- 저장 위치: 패드의 브라우저 localStorage
- 키: `lion_english_progress_v1`
- 형식:
  ```json
  {
    "b1_u1_vocab_pig": { "attempts": 5, "correct": 4, "level": 2 },
    ...
  }
  ```
- 데이터 초기화: 브라우저 설정에서 사이트 데이터 삭제

## 📝 데이터 구조

`english_textbooks.json`은 다음 5권 정보 포함:
1. Sight Words 워크북 (1권)
2. 알파벳 파닉스 워크북 (2권)
3. Common Core Sight Words (3권)
4. Themed Speaking Vol.2 - Spring & Colors (4권)
5. Themed Speaking Vol.1 - My School Is Fun (5권)

각 단어/문장에 고유 ID와 진행도 필드 포함.

---

게임 만든 사람: 빛 + Claude
