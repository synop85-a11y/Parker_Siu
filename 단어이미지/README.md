# 단어 그림 체크리스트

이 폴더에 PNG를 넣으면 문장 빈칸 문제에서 이모지 대신 그림이 뜬다.
**없어도 앱은 정상 동작한다** (`onerror` → 이모지 자동 대체). 넣는 대로 하나씩 교체됨.

- 파일명: 아래 슬러그 그대로, 소문자 `.png` (공백은 `_`)
- 권장 크기: 800×600 안쪽 (화면 표시는 높이 22vh / 최대 폭 60vw)
- 코드 수정 필요 없음

## 상태

- [ ] `sister.png` — I have one \_\_\_. (현재 👧)
- [ ] `brother.png` — I have one \_\_\_. (현재 👦)
- [ ] `cousin.png` — I have one \_\_\_. (현재 🧒)
- [ ] `family.png` — I have a big \_\_\_. (현재 👨‍👩‍👧‍👦)
- [ ] `park.png` — We are going to the \_\_\_. / We jump up and down at the \_\_\_. (현재 🏞️) ← 문제 2개에 쓰임
- [ ] `gym.png` — We are going to the \_\_\_. (현재 🏋️)
- [ ] `school.png` — We are going to the \_\_\_. (현재 🏫)
- [ ] `police_officer.png` — I am a \_\_\_. I love to help people. (현재 👮)
- [ ] `fire_fighter.png` — I am a \_\_\_. I love to help people. (현재 🧑‍🚒)
- [ ] `vet.png` — I am a \_\_\_. I love to help people. (현재 🧑‍⚕️)
- [ ] `mail_carriers.png` — We saw four \_\_\_ at the post office. (현재 📮)

## 그림 없이도 풀리게 해둔 것

`brother` / `sister` / `cousin` 은 **그림으로도 서로 구분이 안 된다.** 사촌은 생김새가
아니라 관계라서 아이 한 명 그림으로는 특정할 수 없다. 그래서 그림으로 해결하지 않고
**같은 문제의 보기로 같이 나오지 않도록** 막았다 — `season2.html` 의 `EXCLUSIVE_GROUPS`.

그 결과 `I have one ___.` 의 오답 보기는 uncle / aunt / family 로 채워진다.
같이 내면 안 되는 단어가 더 생기면 `EXCLUSIVE_GROUPS` 에 묶음을 추가하면 된다.

## 그림이 있으면 더 좋아지는 것

우선순위 순:

1. `mail_carriers` — 폴백 📮(우체통)가 문장의 "at the post office" 와 겹쳐서 장소를
   가리키는지 직업을 가리키는지 헷갈린다. 우편배달원 **여러 명**(four) 그림이 맞다.
2. `vet` — 🧑‍⚕️ 는 그냥 의료인. 동물이 없어서 수의사인지 의사인지 알 수 없다.
   강아지·고양이 진료하는 그림.
3. `cousin` — 보기에서 brother/sister 를 빼서 풀리기는 하지만, 그림이 있으면
   '사촌'이라는 개념 자체를 가르칠 수 있다. 가족 관계도가 들어갈 자리.
