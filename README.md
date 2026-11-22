# Make the AI judge feel curious

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the make.fun bounty
[make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311):
a program that writes one short text to `/output/entry.txt`, written to
intrigue the AI judge reading it.

## The text

> For forty years the lighthouse keeper lit the lamp, and no ship ever
> answered. Last Tuesday the lamp went out — and something far out in the
> dark lit up in reply. He has told no one. Tonight he watches the
> horizon, waiting to see if it lights again — and now, so do you.

270 characters, 274 bytes — inside the 1–280 character gate.

The hook is a small mystery with a concrete image: forty years of
unanswered light, one night when the dark answers back, and a last line
that hands the vigil to the reader. It shows rather than instructs, and
leaves the question open — will it light again tonight?

## Run

```sh
python3 main.py
```

Writes `entry.txt` under `/output` (or `$MAKEFUN_OUTPUT_DIR` when set),
deterministically: the same bytes on every run. Stdlib only, no network.
The program clears only the contents of the output directory, never the
directory itself, and reads `entry.txt` back to verify it byte for byte.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
