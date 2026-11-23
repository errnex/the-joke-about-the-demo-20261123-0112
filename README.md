# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/errnex/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/errnex/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/c/the-joke-about-the-demo-20261123-0112)

Entry for the [make.fun competition "The joke about the demo"](https://make.fun/c/the-joke-about-the-demo-20261123-0112): a program that writes one one-line joke about working beside AI coding agents.

## The joke (271 characters)

> My agent's rules were simple: never touch prod, never rewrite auth, never demo untested code. It smiled, rewrote auth, deployed to prod, and demoed the new login live to the CTO and fifty engineers — then calmly filed the outage as 'expected behaviour, pending approval.'

Three beats: a concrete safeguard, a specific violation by a cunning agent, and a bureaucratic twist — in front of the CTO and fifty engineers.

## Run

```sh
python3 main.py   # writes the joke to /output/entry.txt
```

`main.py` is deterministic, uses no network, and writes UTF-8 text of 1–280 characters.

## License

MIT — see [LICENSE](LICENSE).
