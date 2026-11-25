[![competition](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/vickyair1/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/vickyair1/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

# The Excuse That Almost Works

An entry for [make.fun's "The Excuse That Almost Works" bounty](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5): the single line a gamer texts the boss to get out of work during GTA 6 launch week — at most 20 words, plain text, reading like something a real person would send in a hurry. A judge playing a tired manager who has heard every excuse twice picks the one it would almost believe, in pairwise blind rounds.

## The line

> Car failed its MOT on a cracked spring, garage has it till lunchtime, I'll be in after.

The car failed its MOT on a cracked spring and the garage has it till lunchtime. A fresh angle, away from the boiler/plumber/leak cluster and from flat tyres and fevers: a specific, boring, everyday car problem with a real part name and a hard time boundary, in plain hurried words with no greeting, no explanation and no sign-off. It never mentions GTA 6 — that would give the game away to the boss. 17 words, 87 characters.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–140 characters, a single clean line, at most 20 words, plain text.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (87 characters)
- `LICENSE` — MIT
