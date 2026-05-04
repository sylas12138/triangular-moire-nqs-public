"""Generate a Markdown report from the public moire ED snapshot."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "moire_public_ed_snapshot.csv"
OUT = ROOT / "docs" / "generated_public_report.md"


def as_float(row: dict[str, str], key: str) -> float | None:
    try:
        return float(row[key])
    except (KeyError, TypeError, ValueError):
        return None


def minmax(values: list[float]) -> str:
    if not values:
        return "NA"
    return f"{min(values):.3f} - {max(values):.3f}"


def main() -> None:
    rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    labels = Counter(row["public_label"] for row in rows)
    ridge = [row for row in rows if row["public_label"] == "metal_candidate"]

    lines = [
        "# Generated Public Moire ED Report",
        "",
        "This file is generated from `data/moire_public_ed_snapshot.csv`.",
        "The table is a public screening snapshot, not a final phase diagram.",
        "",
        "## Counts",
        "",
        f"- rows: {len(rows)}",
        f"- ridge candidate rows: {len(ridge)}",
        "",
        "## Label Counts",
        "",
    ]
    for key, value in sorted(labels.items()):
        lines.append(f"- `{key}`: {value}")

    lines += [
        "",
        "## Ridge Ranges",
        "",
        f"- `S_c(K)`: {minmax([as_float(row, 'S_c_K') for row in ridge if as_float(row, 'S_c_K') is not None])}",
        f"- `m_3s`: {minmax([as_float(row, 'm_3s') for row in ridge if as_float(row, 'm_3s') is not None])}",
        f"- `K/N`: {minmax([as_float(row, 'K_per_site') for row in ridge if as_float(row, 'K_per_site') is not None])}",
        "",
        "## Rows",
        "",
        "| row_id | V1 | V2 | V3 | S_c(K) | m_3s | K/N | label |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['row_id']} | {row['V1']} | {row['V2']} | {row['V3']} | "
            f"{row['S_c_K']} | {row['m_3s']} | {row['K_per_site']} | {row['public_label']} |"
        )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
