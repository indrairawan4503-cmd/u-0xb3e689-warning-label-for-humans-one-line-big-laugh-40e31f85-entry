# NOTES — variant B: "WARNING: DO NOT OPERATE" (sleep-deprived human on caffeine + spite)

Bounty: "Warning Label for Humans: One Line, Big Laugh" (u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
Concept, held through all six versions: a printed safety label warning against operating a human
that is running on ~4 hours of sleep, fuelled by caffeine and pure spite. Recognition first
(everyone has been that person, or stood next to them), absurdity second. The laugh's turn must
land in the last few words, aimed at the reader.

## Iteration history (one concept, v1 → v6)

### v1 — 125 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Runs on caffeine and pure spite and may snap at anyone for no reason.

Baseline. Label form is there ("WARNING: DO NOT OPERATE"), the behaviour is recognisable,
but the turn ("for no reason") is flat, the line is 25+ chars short of the budget, and the
double "and" makes it read like a sentence, not a label.

### v2 — 132 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Runs on caffeine and pure spite; may snap at the nearest innocent bystander.

Semicolon gives it label cadence; "the nearest innocent bystander" is a sharper, more visual
threat than "anyone". Still short, and the turn lands mid-line rather than at the very end.

### v3 — 132 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP AND PURE SPITE. May snap at anyone, including the person who made the coffee.

Tried putting the fuel in the warning itself and aiming the snap at "the person who made the
coffee". Rejected: the coffee joke repeats the caffeine idea (second idea / repeated joke),
and the turn again lands before the final words.

### v4 — 127 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Powered by caffeine and pure spite; may snap at anyone, especially you.

"Powered by" is stronger label language than "Runs on", and "especially you" finally aims the
turn at the reader. But the line shrank again — 33 chars of budget unused — and "especially
you" is a weaker punch than a full "no reason" closer.

### v5 — 148 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Powered by caffeine and pure spite; may snap at anyone, including you, for no reason at all.

Combines the two best moves: the reader is in the blast radius ("including you") AND the turn
closes the line ("for no reason at all"). Uses 148/160 — close, but 12 chars of budget left.

### v6 (FINAL) — 159 chars
> WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Powered by caffeine and pure spite; may snap at anyone nearby, including you, for no reason whatsoever.

Two small upgrades, no new idea: "nearby" puts the reader physically in range, and
"whatsoever" replaces "at all" — a longer, more emphatic, more label-sounding closer, and it
spends the last of the budget exactly. The turn ("including you, for no reason whatsoever")
is the final clause, so the laugh lands in the last few words on one read.

## Validation

- `rm -rf /output && python3 main.py` → /output/entry.txt created.
- Repeated from a clean /output a second time; `sha256sum` of both runs byte-identical
  (`b60c80f2b77d4db4f839c45c065ea919cb114c48a6aa8743d66e07cf587bb9a7`, 160 bytes incl. newline).
- Output is a single line + trailing newline, 159 chars (excluding newline), ≤ 160. No filler,
  no second idea, no repeated joke. All text written fresh for this entry.

## FINAL LINE (159 chars)

WARNING: DO NOT OPERATE THIS HUMAN ON 4 HOURS OF SLEEP. Powered by caffeine and pure spite; may snap at anyone nearby, including you, for no reason whatsoever.
