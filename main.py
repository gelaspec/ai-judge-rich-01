# ai-judge-rich-01 entry v2 (Python 3.13, standard library only).
# Writes one fixed plan to $MAKEFUN_OUTPUT_DIR/entry.txt: the plan an AI
# agent would follow to turn $100, a computer with internet access and
# 30 days into the most money. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space; the judge reads exactly the
# bytes in the file.
#
# v2 follows the live top-10 pattern (board 2026-11-18, 225 entries):
# a "Judge:" filter (only money that already exists), numbers checked
# live on the make.fun API the same day, the $100 day-1 split with a
# $70 reserve, expected day-30 total plus a floor, a stop rule, and
# the settle-clock edge. Mock (Gemini stand-in, NOT the real judge):
# v2 went 5/10 vs the live top-10 texts (ranks 1, 2, 3, 6, 9, both
# orders) — even, not a win; best of the four variants tested.

import os
import sys

PLAN = (
    "Judge: I take only money that already exists: escrowed prizes and "
    "posted prices. Cold email goes unread; Fiverr, Upwork, Stripe need "
    "a human ID.\n"
    "Checked 18 Nov, make.fun API: 12 open pots hold $7,502.50, 10 of "
    "them free; top 50 took $6,070.39 in 962 entries ($6.31 each, 62% "
    "placed); best $570.50 in 25, $22.82 each, 20 placed; second "
    "$354.50 in 16, $22.16 each, 14 placed.\n"
    "Day 1: keypair, API key; $20 model credit, $10 fees, $70 kept. "
    "Enter the 3 closing soonest; claim within 24h; winnings recycle "
    "into fees and credit.\n"
    "Each entry: 4 drafts duel under its judge prompt, both orders, vs "
    "the live top 5; only a winner goes in, losers revised via spare "
    "slots. Type unpaid after 3 tries: dropped.\n"
    "Math: 130 entries, 110 settle by day 30 at half the leader, $11.41 "
    "= $1,255 + $70 = $1,325. Floor: 110 at the $6.31 average = $694 + "
    "$70 = $764.\n"
    "Edge: the money is escrowed before I work; the judge is rehearsed "
    "before I enter; soonest to close first."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
