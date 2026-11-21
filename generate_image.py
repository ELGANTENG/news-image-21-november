#!/usr/bin/env python3
"""Draw the 21 November 2026 world-news front page.

Deterministic: no timestamps, no randomness, fixed font sizes and
coordinates, so every run writes byte-identical PNG output.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

PAPER = (248, 244, 233)
INK = (25, 23, 19)
MUTED = (96, 90, 80)
RED = (164, 31, 31)
BLUE = (31, 78, 121)
TEAL = (18, 110, 105)
GOLD = (176, 124, 28)
SKY = (214, 231, 240)
SAND = (238, 226, 198)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, lines, f, fill=INK, leading=None, align="left"):
    lh = leading or int(f.size * 1.25)
    for ln in lines:
        if align == "center":
            lx = x - d.textlength(ln, font=f) / 2
        else:
            lx = x
        d.text((lx, y), ln, font=f, fill=fill)
        y += lh
    return y


def rule(x0, y, x1, width=2, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- masthead
MX = 26
CW = W - 2 * MX  # 972

d.text((W / 2, 30), "THE WORLD IN ONE IMAGE",
       font=SERIF_B(52), fill=INK, anchor="ma")
rule(MX, 96, W - MX, 3)
d.text((W / 2, 104), "SATURDAY  21  NOVEMBER  2026",
       font=SANS_B(25), fill=RED, anchor="ma")
d.text((W / 2, 134), "SEVEN STORIES FROM AROUND THE GLOBE  ·  ONE PAGE",
       font=SANS(15), fill=MUTED, anchor="ma")
rule(MX, 158, W - MX, 2)

# ------------------------------------------------------------------- hero
HX, HY, HW, HH = MX, 170, CW, 296
d.rectangle([HX, HY, HX + HW, HY + HH], outline=INK, width=2)
d.rectangle([HX + 2, HY + 2, HX + HW - 2, HY + HH - 2], outline=RED, width=1)

# hero illustration: Andean quake, left half
ix, iy, iw, ih = HX + 4, HY + 4, 500, HH - 8
d.rectangle([ix, iy, ix + iw, iy + ih], fill=SKY)
# mountains
d.polygon([(ix, iy + ih), (ix + 110, iy + 60), (ix + 220, iy + ih)], fill=(122, 138, 150))
d.polygon([(ix + 60, iy + ih), (ix + 170, iy + 90), (ix + 150, iy + 70),
           (ix + 190, iy + 110), (ix + 280, iy + ih)], fill=(96, 112, 126))
d.polygon([(ix + 250, iy + ih), (ix + 390, iy + 40), (ix + 500, iy + ih)], fill=(139, 152, 160))
# snow caps
d.polygon([(ix + 152, iy + 102), (ix + 170, iy + 88), (ix + 188, iy + 102)],
          fill=(255, 255, 255))
d.polygon([(ix + 374, iy + 54), (ix + 390, iy + 40), (ix + 406, iy + 54)],
          fill=(255, 255, 255))
# ground + crack
gy = iy + ih - 46
d.rectangle([ix, gy, ix + iw, iy + ih], fill=(196, 172, 128))
crack = [(ix + 60, gy), (ix + 95, gy + 14), (ix + 80, gy + 26),
         (ix + 120, gy + 38), (ix + 105, gy + 46)]
d.line(crack, fill=INK, width=4)
d.line([(ix + 300, gy), (ix + 330, gy + 18), (ix + 315, gy + 34),
        (ix + 350, gy + 46)], fill=INK, width=4)
# tilted houses
for bx, tilt in ((ix + 150, -8), (ix + 210, 10), (ix + 400, -6)):
    d.rectangle([bx, gy - 34 + tilt, bx + 34, gy], outline=INK, width=2, fill=(232, 214, 178))
    d.polygon([(bx - 3, gy - 34 + tilt), (bx + 17, gy - 48 + tilt),
               (bx + 37, gy - 34 + tilt)], fill=RED)
# seismograph trace across the sky (left part only; label sits top right)
pts = []
for k in range(0, 44):
    px = ix + 10 + k * 8
    py = iy + 34 + (math.sin(k * 0.9) * 6 if k < 20 else
                    math.sin(k * 2.1) * 20 * math.exp(-abs(k - 30) / 10))
    pts.append((px, py))
d.line(pts, fill=RED, width=3)
d.text((ix + iw - 96, iy + 10), "M 6.8", font=SANS_B(22), fill=RED)

# hero text, right side
tx = HX + 528
d.text((tx, HY + 16), "PERU  ·  EARTHQUAKE", font=SANS_B(17), fill=RED)
text_block(tx, HY + 44,
           wrap("6.8 QUAKE SHAKES PERU", SANS_B(40), HW - 540),
           SANS_B(40), leading=44)
text_block(tx, HY + 140,
           wrap("A magnitude 6.8 earthquake strikes Junín in the Andes. "
                "Tremors are felt in Lima, about 320 km away, Peru's "
                "Geophysical Institute says.", SANS(19), HW - 540),
           SANS(19), leading=25)
d.text((tx, HY + HH - 34), "HERO STORY", font=SANS_B(14), fill=MUTED)

# -------------------------------------------------------------------- grid
stories = [
    dict(kicker="CLIMATE  ·  COP31", tint=(226, 238, 226),
         head="CLIMATE TALKS RUN OVERTIME",
         body="COP31 in Antalya drags past its deadline as nearly 200 "
              "nations split over fossil fuels.",
         art="cop"),
    dict(kicker="INDIA  ·  WEATHER", tint=(214, 231, 240),
         head="CYCLONE AKVAN HITS ODISHA",
         body="The storm crosses the coast near Gopalpur with strong "
              "winds and heavy rain.",
         art="cyclone"),
    dict(kicker="IRAN  ·  DIPLOMACY", tint=(238, 226, 198),
         head="IRAN SEEKS TALKS, TRUMP SAYS NO",
         body="Tehran's foreign minister says Iran wants diplomacy to "
              "end the war; Trump calls the terms unacceptable.",
         art="flags"),
    dict(kicker="BUSINESS  ·  AI", tint=(232, 226, 240),
         head="ANTHROPIC CLOSES $119.5BN IPO",
         body="The AI firm's record listing — a $93.5bn IPO plus a "
              "$26bn placement — tops SpaceX's June debut.",
         art="ipo"),
    dict(kicker="NEW YORK  ·  USA", tint=(240, 226, 222),
         head="RIKERS TO CLOSE BY 2032",
         body="Mayor Mamdani unveils a plan to shut the jail complex — "
              "five years past the 2027 legal deadline.",
         art="rikers"),
    dict(kicker="SPORT  ·  CRICKET", tint=(226, 238, 226),
         head="RAHUL COMPLETES THE SENA SET",
         body="A century in Wellington makes him the first Indian "
              "opener with Test tons in all four SENA countries.",
         art="cricket"),
]


def draw_art(kind, ax, ay, aw, ah):
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(255, 255, 255))
    cx, cy = ax + aw / 2, ay + ah / 2
    if kind == "cop":
        # globe + rising thermometer
        d.ellipse([cx - 52, cy - 52, cx + 52, cy + 52], fill=(150, 196, 222),
                  outline=BLUE, width=3)
        d.ellipse([cx - 34, cy - 40, cx - 2, cy - 8], fill=(96, 168, 96))
        d.ellipse([cx + 4, cy + 6, cx + 38, cy + 40], fill=(96, 168, 96))
        d.ellipse([cx + 14, cy - 44, cx + 40, cy - 20], fill=(96, 168, 96))
        d.rounded_rectangle([ax + aw - 34, ay + 10, ax + aw - 18, ay + ah - 34],
                            radius=8, outline=RED, width=3)
        d.line([(ax + aw - 26, ay + ah - 40), (ax + aw - 26, ay + 26)],
               fill=RED, width=6)
        d.ellipse([ax + aw - 34, ay + ah - 46, ax + aw - 18, ay + ah - 30],
                  fill=RED)
    elif kind == "cyclone":
        # spiral + rain
        for r in range(8, 62, 9):
            d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300,
                  fill=BLUE, width=4)
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=BLUE)
        for k in range(6):
            rx = ax + 14 + k * 46
            d.line([(rx, ay + ah - 34), (rx - 8, ay + ah - 12)],
                   fill=TEAL, width=3)
    elif kind == "flags":
        # two flags facing each other, dashed line between
        for fx, cols in ((ax + 26, [(178, 34, 52), (255, 255, 255), (0, 122, 61)]),
                         (ax + aw - 116, [(178, 34, 52), (255, 255, 255),
                                          (31, 78, 121)])):
            d.line([(fx, ay + 14), (fx, ay + ah - 26)], fill=INK, width=3)
            for i, c in enumerate(cols):
                d.rectangle([fx, ay + 16 + i * 20, fx + 88, ay + 36 + i * 20],
                            fill=c, outline=INK, width=1)
        d.line([(ax + 130, cy), (ax + aw - 130, cy)], fill=GOLD, width=3)
        for k in range(5):
            d.line([(ax + 138 + k * 12, cy - 4), (ax + 144 + k * 12, cy + 4)],
                   fill=GOLD, width=2)
    elif kind == "ipo":
        # rising bars + arrow
        bars = [26, 44, 38, 62, 84]
        for i, bh in enumerate(bars):
            bx = ax + 22 + i * 52
            d.rectangle([bx, ay + ah - 22 - bh, bx + 34, ay + ah - 22],
                        fill=TEAL if i < 4 else GOLD, outline=INK, width=1)
        d.line([(ax + 22, ay + ah - 30), (ax + 90, ay + 62),
                (ax + 150, ay + 74), (ax + 236, ay + 22), (ax + 268, ay + 14)],
               fill=RED, width=4)
        d.polygon([(ax + 268, ay + 14), (ax + 244, ay + 12), (ax + 262, ay + 34)],
                  fill=RED)
        d.text((ax + 16, ay + 6), "$119.5bn", font=SANS_B(20), fill=INK)
    elif kind == "rikers":
        # island, water, bars, calendar
        d.rectangle([ax, ay + ah - 26, ax + aw, ay + ah], fill=(150, 196, 222))
        d.ellipse([cx - 78, cy - 18, cx + 78, cy + 34], fill=(196, 172, 128),
                  outline=INK, width=2)
        for k in range(7):
            bx = cx - 60 + k * 20
            d.line([(bx, cy - 52), (bx, cy + 6)], fill=INK, width=4)
        d.rectangle([cx - 66, cy - 58, cx + 66, cy - 50], fill=INK)
        d.text((ax + 14, ay + 8), "2032", font=SANS_B(24), fill=RED)
    elif kind == "cricket":
        # pitch, stumps, bat, ball
        d.rectangle([ax + 30, ay + 14, ax + aw - 30, ay + ah - 14],
                    fill=(196, 172, 128), outline=INK, width=2)
        for k in range(3):
            sx = cx - 14 + k * 14
            d.line([(sx, cy - 8), (sx, cy + 26)], fill=GOLD, width=5)
        d.line([(cx - 74, cy + 34), (cx - 46, cy - 26)], fill=(139, 90, 43),
               width=10)
        d.ellipse([cx + 52, cy - 40, cx + 68, cy - 24], fill=RED,
                  outline=INK, width=2)
        d.text((ax + 14, ay + 8), "100", font=SANS_B(24), fill=TEAL)


GW = (CW - 2 * 12) // 3   # 316
GH = 240
GY0 = 478
for i, s in enumerate(stories):
    col, row = i % 3, i // 3
    px = MX + col * (GW + 12)
    py = GY0 + row * (GH + 12)
    d.rectangle([px, py, px + GW, py + GH], outline=INK, width=2)
    d.rectangle([px + 2, py + 2, px + GW - 2, py + GH - 2],
                outline=s["tint"], width=1)
    ax, ay, aw, ah = px + 4, py + 4, GW - 8, 96
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=s["tint"])
    draw_art(s["art"], ax, ay, aw, ah)
    ty = py + 112
    d.text((px + 12, ty), s["kicker"], font=SANS_B(13), fill=RED)
    text_block(px + 12, ty + 20,
               wrap(s["head"], SANS_B(21), GW - 24), SANS_B(21), leading=24)
    n_head = len(wrap(s["head"], SANS_B(21), GW - 24))
    text_block(px + 12, ty + 20 + n_head * 24 + 4,
               wrap(s["body"], SANS(14), GW - 24), SANS(14), leading=18)

# ------------------------------------------------------------------- footer
rule(MX, 984, W - MX, 1)
d.text((W / 2, 990), "Drawn programmatically  ·  Sources: NYT, Reuters, AP, BBC, UN News",
       font=SANS(13), fill=MUTED, anchor="ma")

img.save(OUT, format="PNG")
print("wrote", OUT, img.size)
