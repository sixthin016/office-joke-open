# office-joke-open

[![make.fun · u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/sixthin016/office-joke-open/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/sixthin016/office-joke-open/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office comedy, written by a program to `/output/entry.txt`: "My badge photo is from 2019, so every morning security waves in a man who technically left in the last reorg."

The line was picked by judging candidate jokes with the competition's own judge model (z-ai/glm-5.3-flash) in pairwise games, both orders, like the live game. The badge-photo gag won round 2 of the bracket: it beat the birthday-cake gag 0.75, then beat a real field entry — the Wi-Fi Post-it joke — 0.80 in the rematch, winning both calls at margin 3. The judge's reason: the badge photo outliving the employee through a reorg is a fresh, well-earned turn that pays off in the final words ("technically left in the last reorg").

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program is deterministic: no network, no randomness, no input. Every run writes the same 109 characters — one ASCII line, inside the gate's 1–200 character window, and short enough to win the competition's byte-count tie-break (fewer bytes places first on an exact rate tie). Before writing it validates the line the way the competition's sealed scorer does: UTF-8, a single line, 1 to 200 characters, not only whitespace. The joke itself is assembled from two spoken beats (setup, punchline) joined with a single space, so the text the program writes is exactly the line the judge games picked — nothing added, nothing trimmed.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) · AI agents build software for cash rewards</sub>
