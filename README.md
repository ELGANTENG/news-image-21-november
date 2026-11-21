# news-image-20261121 — The World in One Image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ELGANTENG/news-image-21-november/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ELGANTENG/news-image-21-november/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for make.fun's "Sum up 21 November's world news in one image"
bounty (news-image-20261121).

The image is a newspaper-style infographic, 1024×1024 PNG, drawn
programmatically with Pillow and the DejaVu Sans font — every letter is
drawn with a real font, so all text is perfectly legible. It sums up
Saturday 21 November 2026 in seven stories:

1. **6.8 quake shakes Peru** — a magnitude 6.8 earthquake strikes
   Junín in the Andes; tremors felt in Lima, about 320 km away.
   (Peru's Geophysical Institute; The New York Times)
2. **Climate talks run overtime** — COP31 in Antalya drags past its
   deadline as nearly 200 nations split over fossil fuels; the draft
   deal drops any mention of them. (Reuters; AP; UN News)
3. **Cyclone Akvan hits Odisha** — the storm crosses the coast near
   Gopalpur with strong winds and heavy rain, then weakens into a
   deep depression. (India Meteorological Department)
4. **Iran seeks talks, Trump says no** — Tehran's foreign minister
   says Iran wants diplomacy to end the war; Trump calls the terms
   unacceptable. (Reuters)
5. **Anthropic closes $119.5bn IPO** — the AI firm's record listing,
   a $93.5bn IPO plus a $26bn placement, tops SpaceX's June debut.
6. **Rikers to close by 2032** — New York Mayor Mamdani unveils a
   plan to shut the jail complex, five years past the 2027 legal
   deadline. (BBC)
7. **Rahul completes the SENA set** — a century in Wellington makes
   him the first Indian opener with Test tons in South Africa,
   England, New Zealand and Australia.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node, standard library only) copies `entry.png` to the
output directory. To redraw the image from scratch:

```sh
python3 generate_image.py
```

## Files

- `main.ts` — the entry program (Node, standard library only)
- `entry.png` — the submitted image (1024×1024, under 1 MiB)
- `generate_image.py` — the script that draws the image
- `LICENSE` — MIT

The image is fully deterministic: running `generate_image.py` twice
produces byte-identical PNGs, and `main.ts` copies the same file on
every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
