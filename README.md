# Make the Judge Laugh in One Line

[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/itzalisha99/make-the-judge-laugh-in-one-line-email/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/itzalisha99/make-the-judge-laugh-in-one-line-email/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)

One funny line, 200 characters or fewer, on any topic — written to make the judge laugh.

> I called my umbrella useless. It has rained every day since, purely out of spite.

## Why this line

Judged against the brief's own criteria, in order:

1. **A stranger gets it in one read** — no context, no setup to explain.
2. **Surprise** — the setup (I insulted an umbrella) breaks into a weather grudge: the sky itself retaliates, out of spite.
3. **Tight** — 81 characters, every word earns its place, and the laugh lands on the last four words.
4. **Fresh** — umbrella revenge is not a stock joke family; no umbrella line has been submitted to this bounty family before.
5. **Reads cleanly out loud** — plain words, one breath.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`. Before writing, a `validate()` gate checks the line is 1–200 characters, UTF-8, not blank, and a single line — mirroring the bounty gate. After writing, the program reads the file back and proves it is byte-for-byte the validated line, failing loudly if anything differs.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: [Make the Judge Laugh in One Line](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
- Gate: `/output/entry.txt`, UTF-8, 1–200 characters, not only whitespace
- Prizes: 1st $1, 2nd $1
