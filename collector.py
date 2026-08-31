import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

from playwright.sync_api import sync_playwright


# ============================================================
# CONFIG
# ============================================================

SITE_URL = "https://www.playdeltaforce.com/events/hq/en/"

MAIN_PY = Path("main.py")

JSON_FILE = Path("codes.json")

PAGE_TIMEOUT = 30_000


# ============================================================
# MAP NAMES
# ============================================================

MAP_NAMES = [
    "Zero Dam",
    "Layali Grove",
    "Brakkesh",
    "Space City",
    "Tide Prison",
    "AZ3",
]


# ============================================================
# TODAY
# ============================================================

def get_today():

    return datetime.now().strftime(
        "%Y/%m/%d"
    )


# ============================================================
# LOAD OLD DATA
# ============================================================

def load_previous_data():

    if not JSON_FILE.exists():

        return {
            "date": None,
            "codes": {}
        }

    try:

        with open(
            JSON_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return {
            "date": data.get("date"),
            "codes": data.get(
                "codes",
                {}
            )
        }

    except Exception as e:

        print(
            f"WARNING: Could not read "
            f"{JSON_FILE}: {e}"
        )

        return {
            "date": None,
            "codes": {}
        }


# ============================================================
# SAVE DATA
# ============================================================

def save_codes(
    codes,
    date
):

    data = {
        "date": date,
        "codes": codes
    }

    with open(
        JSON_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# COLLECT CODES
# ============================================================

def collect_codes():

    print()
    print("=" * 60)
    print("Opening Delta Force HQ...")
    print("=" * 60)

    collected = {}

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.set_default_timeout(
            PAGE_TIMEOUT
        )

        # ----------------------------------------------------
        # OPEN SITE
        # ----------------------------------------------------

        page.goto(
            SITE_URL,
            wait_until="domcontentloaded"
        )

        # ----------------------------------------------------
        # Wait for JavaScript
        # ----------------------------------------------------

        page.wait_for_timeout(5000)

        # ----------------------------------------------------
        # Find password lists
        # ----------------------------------------------------

        password_lists = page.locator(
            ".password-list"
        )

        list_count = password_lists.count()

        print(
            f"Found {list_count} password lists."
        )

        # ----------------------------------------------------
        # Read all password lists
        # ----------------------------------------------------

        for list_index in range(
            list_count
        ):

            password_list = (
                password_lists.nth(
                    list_index
                )
            )

            items = password_list.locator(
                ":scope > div"
            )

            item_count = items.count()

            print(
                f"Checking password list "
                f"{list_index + 1}: "
                f"{item_count} entries"
            )

            for i in range(
                item_count
            ):

                item = items.nth(i)

                try:

                    title_locator = (
                        item.locator("p")
                    )

                    code_locator = (
                        item.locator(
                            "span.bold"
                        )
                    )

                    if (
                        title_locator.count()
                        == 0
                    ):
                        continue

                    if (
                        code_locator.count()
                        == 0
                    ):
                        continue

                    title = (
                        title_locator
                        .first
                        .inner_text()
                        .strip()
                    )

                    code = (
                        code_locator
                        .first
                        .inner_text()
                        .strip()
                    )

                except Exception:

                    continue

                title = " ".join(
                    title.split()
                )

                code = "".join(
                    code.split()
                )

                # ------------------------------------------------
                # Only our six maps
                # ------------------------------------------------

                if title not in MAP_NAMES:
                    continue

                # ------------------------------------------------
                # Code must be 4 digits
                # ------------------------------------------------

                if not re.fullmatch(
                    r"\d{4}",
                    code
                ):

                    print(
                        f"WARNING: Invalid code "
                        f"for {title}: {code}"
                    )

                    continue

                collected[title] = code

        browser.close()

    # ========================================================
    # VALIDATE
    # ========================================================

    missing = [
        name
        for name in MAP_NAMES
        if name not in collected
    ]

    print()

    print(
        f"Successfully collected "
        f"{len(collected)} / "
        f"{len(MAP_NAMES)} maps."
    )

    for name in MAP_NAMES:

        if name in collected:

            print(
                f"  {name:<20}"
                f" -> "
                f"{collected[name]}"
            )

        else:

            print(
                f"  {name:<20}"
                f" -> NOT FOUND"
            )

    if missing:

        raise RuntimeError(
            "Could not collect all 6 maps.\n"
            f"Missing: {', '.join(missing)}"
        )

    return collected


# ============================================================
# COMPARE
# ============================================================

def find_changes(
    old_codes,
    new_codes
):

    changes = {}

    for name in MAP_NAMES:

        old = old_codes.get(name)
        new = new_codes.get(name)

        if old != new:

            changes[name] = {
                "old": old,
                "new": new
            }

    return changes


# ============================================================
# GENERATE IMAGE
# ============================================================

def generate_image():

    print()
    print("=" * 60)
    print("Generating image...")
    print("=" * 60)

    result = subprocess.run(
        [
            sys.executable,
            str(MAIN_PY)
        ],
        check=False
    )

    if result.returncode != 0:

        raise RuntimeError(
            f"{MAIN_PY} failed with "
            f"exit code {result.returncode}"
        )

    print(
        "Image generation completed."
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("DELTA FORCE DAILY CODE COLLECTOR")
    print("=" * 60)

    # --------------------------------------------------------
    # Today's date
    # --------------------------------------------------------

    today = get_today()

    print()
    print(
        f"Today's date: {today}"
    )

    # --------------------------------------------------------
    # Previous data
    # --------------------------------------------------------

    previous = load_previous_data()

    old_date = previous["date"]

    old_codes = previous["codes"]

    print()

    print(
        f"Previous saved date: "
        f"{old_date}"
    )

    # --------------------------------------------------------
    # Collect
    # --------------------------------------------------------

    new_codes = collect_codes()

    # --------------------------------------------------------
    # Compare
    # --------------------------------------------------------

    changes = find_changes(
        old_codes,
        new_codes
    )

    date_changed = (
        old_date != today
    )

    # --------------------------------------------------------
    # No changes
    # --------------------------------------------------------

    if not changes and not date_changed:

        print()
        print("=" * 60)
        print("NO CHANGES")
        print("=" * 60)

        print(
            "Codes are unchanged."
        )

        print(
            "Date is unchanged."
        )

        print(
            "Image was not regenerated."
        )

        return

    # --------------------------------------------------------
    # Changes
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("UPDATE REQUIRED")
    print("=" * 60)

    if changes:

        print()
        print("Code changes:")

        for name, change in (
            changes.items()
        ):

            old = change["old"]

            new = change["new"]

            if old is None:
                old = "NONE"

            print(
                f"  {name:<20}"
                f"{old} -> {new}"
            )

    else:

        print()
        print(
            "No code changes."
        )

    if date_changed:

        print()

        print(
            f"Date change: "
            f"{old_date} -> {today}"
        )

    # --------------------------------------------------------
    # Save JSON
    # --------------------------------------------------------

    save_codes(
        new_codes,
        today
    )

    print()

    print(
        f"Updated {JSON_FILE}"
    )

    # --------------------------------------------------------
    # Generate image
    # --------------------------------------------------------

    generate_image()

    # --------------------------------------------------------
    # Done
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()