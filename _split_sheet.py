# -*- coding: utf-8 -*-
"""생성 시트(한 장에 여러 그림)를 칸별로 잘라 개별 PNG 로 만든다.

    python _split_sheet.py <시트파일> <이름1> <이름2> ...

이름은 왼쪽 위 -> 오른쪽, 그다음 줄 순서로 붙는다. 건너뛸 칸은 `-` 를 준다.
결과는 `_cut/` 에 저장되고, 확인한 뒤 `Parker_Siu/단어이미지/` 로 옮기면 된다.

투명 배경과 흰 배경을 모두 처리하고, 아래쪽 라벨 글자는 잘라낸다.
"""
import os
import sys

import cv2
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_cut")


def to_bgr_alpha(img):
    """(bgr, alpha) 로 정규화. 흰 배경이면 흰색을 투명으로 간주한다."""
    if img.shape[2] == 4:
        return img[:, :, :3], img[:, :, 3]
    bgr = img[:, :, :3]
    # 흰색에 가까우면 배경
    near_white = (bgr > 243).all(axis=2)
    alpha = np.where(near_white, 0, 255).astype(np.uint8)
    return bgr, alpha


def runs(mask, gap):
    """True 가 이어지는 구간을 [(시작, 끝)] 으로. gap 이하의 끊김은 이어붙인다."""
    idx = np.nonzero(mask)[0]
    if len(idx) == 0:
        return []
    out = [[idx[0], idx[0]]]
    for i in idx[1:]:
        if i - out[-1][1] <= gap:
            out[-1][1] = i
        else:
            out.append([i, i])
    return [(a, b) for a, b in out]


def strip_label(bgr, alpha):
    """
    칸 아래에 붙어 나온 파일명 라벨을 잘라낸다.

    라벨은 그림과 빈 줄로 떨어져 있고, 글자라서 세로로 얇다.
    아래쪽 40% 안에서 빈 줄이 나타나면 거기서 자른다.
    """
    h = alpha.shape[0]
    filled = (alpha > 40).any(axis=1)

    # 내용 덩어리들을 위에서부터 나열한다
    blocks = []
    y = 0
    while y < h:
        if filled[y]:
            s = y
            while y < h and filled[y]:
                y += 1
            blocks.append((s, y - 1))
        else:
            y += 1
    if len(blocks) < 2:
        return bgr, alpha

    # 가장 두꺼운 덩어리가 그림이다. 1~2픽셀짜리 노이즈 줄에 속으면 안 된다.
    main = max(blocks, key=lambda b: b[1] - b[0])
    main_end = main[1]
    below = sum(e - s + 1 for s, e in blocks if s > main_end)
    if main_end > h * 0.45 and 0 < below < h * 0.35:
        return bgr[:main_end + 1], alpha[:main_end + 1]
    return bgr, alpha


def split(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise SystemExit(f"읽기 실패: {path}")
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    bgr, alpha = to_bgr_alpha(img)
    H, W = alpha.shape
    solid = alpha > 40

    cells = []
    for y0, y1 in runs(solid.any(axis=1), max(8, H // 40)):
        band = solid[y0:y1 + 1]
        if (y1 - y0) < H * 0.04:      # 라벨 글자 줄
            continue
        for x0, x1 in runs(band.any(axis=0), max(8, W // 40)):
            if (x1 - x0) < W * 0.04:
                continue
            cells.append((x0, y0, x1, y1))
    return bgr, alpha, cells


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    path, names = sys.argv[1], sys.argv[2:]
    bgr, alpha, cells = split(path)
    os.makedirs(OUT, exist_ok=True)

    print(f"{os.path.basename(path)} → 칸 {len(cells)}개")
    if not names:
        print("이름을 주지 않아 미리보기만 합니다. 순서:")
        for i, (x0, y0, x1, y1) in enumerate(cells, 1):
            print(f"  {i}. x{x0}~{x1} y{y0}~{y1}  ({x1-x0}x{y1-y0})")
        return

    for (x0, y0, x1, y1), name in zip(cells, names):
        if name == "-":
            continue
        pad = 6
        x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
        x1, y1 = min(bgr.shape[1], x1 + pad), min(bgr.shape[0], y1 + pad)
        crop = bgr[y0:y1, x0:x1]
        a = alpha[y0:y1, x0:x1]
        crop, a = strip_label(crop, a)
        rgba = np.dstack([crop, a])
        dst = os.path.join(OUT, f"{name}.png")
        cv2.imwrite(dst, rgba)
        print(f"  {name:14s} {x1-x0:4d}x{y1-y0:<4d} → {dst}")


if __name__ == "__main__":
    main()
