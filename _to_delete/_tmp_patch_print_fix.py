# -*- coding: utf-8 -*-

def patch_file(path, replacements):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    for old, new, label in replacements:
        cnt = content.count(old)
        assert cnt == 1, f"{path} / {label}: erwartet 1 Treffer, gefunden {cnt}"
        content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {path} aktualisiert ({len(replacements)} Ersetzung/en)")


patch_file(
    "HB_Verkaufsseite.html",
    [
        (
            '<span class="preis-betrag">18–20 €<span> einmalig</span></span>',
            '<span class="preis-betrag">24 €<span> einmalig</span></span>',
            "HB Print-Preis",
        )
    ],
)

patch_file(
    "MB_Verkaufsseite.html",
    [
        (
            '<span class="preis-betrag">18–20 €<span> einmalig</span></span>',
            '<span class="preis-betrag">24 €<span> einmalig</span></span>',
            "MB Print-Preis",
        )
    ],
)

old_open = "**Weiterhin offen, unabhängig von dieser Harmonisierung:** Die Print-Variante von HB/MB zeigt auf den Verkaufsseiten noch eine Preisspanne (18–20€) statt eines Digistore-tauglichen Festpreises — das wurde hier nicht angefasst, sag Bescheid, falls das auch noch vereinheitlicht werden soll. Bitte trotzdem jeden Preis vor dem Livegang final selbst bestätigen."

new_open = "**Ergänzung (22.08.2026):** Die Print-Variante von HB/MB ist jetzt ebenfalls vereinheitlicht — statt der alten Preisspanne (18–20€) gilt jetzt ein fester Preis von 24€, passend zum shopweiten Muster (Digital-Preis + rund 9€ Print-Aufschlag, wie bei den anderen 15€-Digital-Decks FS, LRS, OGS, SP etc.). Bitte trotzdem jeden Preis vor dem Livegang final selbst bestätigen."

patch_file(
    "Digistore24_Setup_Guide.md",
    [(old_open, new_open, "Weiterhin-offen-Satz")],
)

print("ALLE PATCHES OK")
