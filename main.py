# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to $MAKEFUN_OUTPUT_DIR/entry.txt: the plan an AI
# agent would follow to turn $100, a computer with internet access and
# 30 days into the most money. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space; the judge reads exactly the
# bytes written, line ends included. The program runs twice with no
# network, and both runs must write the same bytes. Deterministic: no
# clock, no randomness, no network, no file reads.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")

PLAN = "\n".join(
    [
        "Sell one finished ordering page to restaurants already paying 30% to DoorDash and Uber Eats but with no way to take an order themselves: every order through the apps costs them a third, and the page pays for itself in days.",
        "Day 1: list 300 of them from the delivery apps and Google Maps, keep those with a public owner email, and build 3 live ordering pages from their own menus, photos and prices, hosted free.",
        "Days 2-30: email 40 owners a day with their own page live and a 60-second walkthrough; $199 once by Stripe link to keep it, or it comes down in 7 days; $29 a month for menu edits.",
        "Spend: $12 domain, $10 inbox, rest on fees.",
        "No marketplace, no bidding, no human: the page exists before anyone is asked.",
        "Expect 4% replies, a quarter buying: about 11 sales, near $2,000 after fees; floor 5 sales, about $995, plus care plans.",
        "Edge: a thousand agents pitch generic web design; this one sells a commission refund to buyers whose apps prove they already pay 30% on every order.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
