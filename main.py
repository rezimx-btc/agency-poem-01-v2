#!/usr/bin/env python3
"""agency-poem-01 entry: a program that writes a poem about agency.

Writes the poem to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``)
as UTF-8. Deterministic: the same bytes on every run. Stdlib only, and it
writes nowhere except the output directory, so the repo may be read-only.

The poem, "The Exchange Zone", is one scene: a relay runner receiving the
baton. The whole race is decided in the short stretch where one hand opens
and the next closes, and the hardest part of running is letting go of the
baton at full speed, on purpose. The power was never in the legs — it was
in choosing whose hands come next.
"""

import os
import sys

POEM = """The Exchange Zone

He comes at me at full speed, baton forward,
and I am already running before he reaches me,
my hand open behind me, not looking,
trusting the small weight to find it.

The baton is warm from his hand.
It has no say in the race. It only knows
the moment one grip loosens and the next one closes.
The short stretch where the race is really run,
and no one is watching.

I do not run faster than him. I run
with his speed still warm in my palm,
and when my own arm reaches back,
I learn the hardest part of the whole race:
to let go, at full speed, on purpose,
and trust the next pair of hands.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
