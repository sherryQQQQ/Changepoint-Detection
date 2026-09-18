"""Small algebra/document audit; not a detector benchmark or theorem proof.

Run with Python 3, standard library only. Does not access the network.
"""
from itertools import combinations
from math import isclose
from pathlib import Path
import json
import random
import re

ROOT = Path(__file__).resolve().parent


def link_targets(text):
    """Read balanced Markdown targets, including parentheses in DOI URLs."""
    for match in re.finditer(r"\]\(", text):
        start = match.end()
        depth = 1
        for i in range(start, len(text)):
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
                if not depth:
                    yield text[start:i]
                    break
        else:
            raise AssertionError("Unclosed Markdown link")


def document_checks():
    refs = json.loads((ROOT / "sources.json").read_text())
    expected = {f"R{i:02d}" for i in range(1, 35)}
    expected |= {f"S{i:02d}" for i in range(1, 5)}
    ids = [r["id"] for r in refs]
    assert len(ids) == len(set(ids)) == 38
    assert set(ids) == expected
    for record in refs:
        for field in ("authors", "year", "title", "venue", "url",
                      "type", "sections", "summary"):
            assert record[field], (record["id"], field)
        assert record["url"].startswith("https://")
    bib = (ROOT / "references.bib").read_text()
    assert set(re.findall(r"@\w+\{([^,]+),", bib)) == expected
    assert bib.count("{") == bib.count("}")
    annotations = (ROOT / "references.md").read_text()
    for record in refs:
        assert f'id="{record["id"].lower()}"' in annotations
        assert record["title"] in annotations
        assert record["url"] in annotations
        assert record["url"] in bib
    review = (ROOT / "review.md").read_text()
    assert [int(n) for n in re.findall(r"^## (\d+)\.", review, re.M)] == list(range(1, 16))
    assert r"\(" not in review and r"\)" not in review
    for file in ROOT.glob("*.md"):
        text = file.read_text()
        assert text.count("$$") % 2 == 0, file.name
        for target in link_targets(text):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            local = target.split("#", 1)[0]
            assert (file.parent / local).exists(), (file.name, target)


def reset_mass_check():
    """Check a consequence of the stated recursion, without a detector."""
    rng = random.Random(41)
    for size in (1, 2, 7, 25):
        for h in (0.001, 0.01, 0.2):
            w = [rng.random() for _ in range(size)]
            w = [v / sum(w) for v in w]
            q = [0.01 + 3 * rng.random() for _ in range(size)]
            reset = sum(a * b * h for a, b in zip(w, q))
            growth = [a * b * (1 - h) for a, b in zip(w, q)]
            evidence = reset + sum(growth)
            assert isclose(reset / evidence, h, abs_tol=1e-14)


def conjugate_check():
    """Independent batch vs sequential Normal–Inverse-Gamma arithmetic."""
    xs = [-1.4, 0.2, 2.1, 0.7, -0.8, 4.3]
    m0, k0, a0, b0 = 0.3, 0.4, 2.5, 1.7
    m, k, a, b = m0, k0, a0, b0
    for x in xs:
        kp = k + 1
        b += k * (x - m) ** 2 / (2 * kp)
        m = (k * m + x) / kp
        k = kp
        a += 0.5
    n = len(xs)
    mean = sum(xs) / n
    expected = (
        (k0 * m0 + n * mean) / (k0 + n),
        k0 + n,
        a0 + n / 2,
        b0 + sum((x - mean) ** 2 for x in xs) / 2
        + k0 * n * (mean - m0) ** 2 / (2 * (k0 + n)),
    )
    assert all(isclose(x, y, rel_tol=1e-12) for x, y in zip((m, k, a, b), expected))
    scale2 = b * (k + 1) / (a * k)
    nu = 2 * a
    predictive_variance = scale2 * nu / (nu - 2)
    assert isclose(predictive_variance, b / (a - 1) * (1 + 1 / k))
    assert not isclose(predictive_variance, scale2)


def segmentation_check():
    """Unpruned DP vs exhaustive partitions; finite SSE pruning examples."""
    rng = random.Random(17)
    for n in range(2, 10):
        ys = [rng.gauss(0, 1) + (2 if i >= n // 2 else 0)
              for i in range(n)]

        def cost(a, b):
            values = ys[a:b]
            mean = sum(values) / len(values)
            return sum((v - mean) ** 2 for v in values)

        for penalty in (0.3, 1.0, 4.0):
            f = [-penalty]
            for t in range(1, n + 1):
                f.append(min(f[s] + cost(s, t) + penalty for s in range(t)))
            brute = float("inf")
            for count in range(n):
                for cuts in combinations(range(1, n), count):
                    edges = (0,) + cuts + (n,)
                    total = sum(cost(a, b) for a, b in zip(edges, edges[1:]))
                    brute = min(brute, total + count * penalty)
            assert isclose(f[n], brute, abs_tol=1e-10)
            for s in range(n):
                for t in range(s + 1, n):
                    if f[s] + cost(s, t) >= f[t] - 1e-12:
                        for u in range(t + 1, n + 1):
                            assert f[t] + cost(t, u) <= f[s] + cost(s, u) + 1e-10


if __name__ == "__main__":
    for label, check in (
        ("Reference, section and local-link consistency", document_checks),
        ("Constant-hazard reset-mass identity", reset_mass_check),
        ("NIG batch/sequential update and predictive-variance identities", conjugate_check),
        ("Short-sequence DP/brute-force and SSE dominance examples", segmentation_check),
    ):
        check()
        print("PASS:", label)
    print("Scope: document/algebra audit only; no empirical benchmark was run.")
