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


# --- 1) Digistore24_Setup_Guide.md ---

old_row = "| Mobbing | `mobbing26` | KLARTEXT App-Zugang · Mobbing-Intervention | 26,00 € *(Achtung — siehe Hinweis unten)* | MB-Deck nur 10€ — mit Abstand der größte relative Sprung aller vier |"
new_row = "| Mobbing | `mobbing26` | KLARTEXT App-Zugang · Mobbing-Intervention | 20,00 € *(final, Preisharmonisierung 22.08.2026)* | MB-Deck 15€ — konsistenter Aufschlag wie bei den anderen drei |"

old_found = "**Neu gefunden, noch nicht in der Vorgänger-Version dieser Anleitung:** `mobbing26` existiert bereits als funktionierender, getesteter Lizenzcode in KLARTEXT_Login.html (Rolle `mobbing`, `bundle: null`), hat aber wie die anderen 4 noch kein eigenes Digistore24-Produkt. Der Preis 26,00 € ist reine Vermutung von mir, abgeleitet aus dem Namensmuster (endet wie `sb-ingra26`/`tk-leitung26`/`jc-beruf26` auf \"26\" bei tatsächlich 26 €) — bitte bestätigen oder korrigieren."
new_found = "**Zu `mobbing26`:** existiert bereits als funktionierender, getesteter Lizenzcode in KLARTEXT_Login.html (Rolle `mobbing`, `bundle: null`), hat aber wie die anderen 3 noch kein eigenes Digistore24-Produkt. Der Preis ist mit der Preisharmonisierung vom 22.08.2026 final auf 20,00 € festgelegt (siehe Hinweis unten) — keine Vermutung mehr."

old_hint = "**Wichtiger Hinweis zu allen Preisen (aktualisiert mit deinen echten, am 21.08.2026 abgeglichenen Digistore24-Preisen):** Die ursprünglichen 8–10€/18–20€ aus `MB_Verkaufsseite.html` waren die alten, noch nicht angeglichenen Spannen — inzwischen hast du Digistore24 und Verkaufsseiten selbst vereinheitlicht. Die echten Werte: Schnupperpaket kostenlos; 10€ (HB, MB); 15€ (FS, DaZ-GS, DaZ-Sek I, LRS, OGS, M3, SMI, SP, Krisendeck/FK); 18€ (KD, AT, ADHS, TR, TK, GK, Zonen-Set); 22€ (JD, EL, LK, Insel-Set); 24€ (Paket Sprache); 34€ (Alltags-Paket, Paket Berufswelt, Übergänge); 79€ (Komplett-Bundle). Auf dieser Basis liegen die App-Zugänge für Lehrkraft und Eltern (24€) nur leicht über ihren jeweiligen Einzeldecks (22€) — konsistent und gut begründbar. **Bei Mobbing lohnt sich noch mal ein bewusster Blick:** das MB-Deck kostet nur 10€, der vorgeschlagene App-Zugang 26€ wäre mehr als das 2,5-Fache — ein deutlich größerer Sprung als bei den anderen drei Rollen. Das kann absolut gerechtfertigt sein (die App bietet ja weit mehr als nur das eine Deck), aber es ist bewusst keine Vermutung von mir mehr, sondern eine offene Entscheidung: entweder den Sprung so lassen (mit der Begründung „App-Zugang ≠ einzelnes Deck“), oder den Mobbing-Preis etwas näher an die anderen drei heranrücken (z. B. 20–22€). Bitte jeden Preis trotzdem vor dem Livegang final selbst bestätigen."

new_hint = "**Wichtiger Hinweis zu allen Preisen (Preisharmonisierung vom 22.08.2026):** Am 21.08. lagen HB und MB noch bei 10€ und der Mobbing-App-Zugang beim vorgeschlagenen 26€ — mit Abstand der größte relative Sprung aller vier App-Zugänge (2,6-Fache). Das hast du bereinigt: HB und MB liegen jetzt bei 15€ (statt 10€), der Mobbing-App-Zugang bei 20€ (statt 26€). Aktuelle Werte gesamt: Schnupperpaket kostenlos; 15€ (FS, DaZ-GS, DaZ-Sek I, LRS, OGS, M3, SMI, SP, Krisendeck/FK, HB, MB); 18€ (KD, AT, ADHS, TR, TK, GK, Zonen-Set); 22€ (JD, EL, LK, Insel-Set); 24€ (Paket Sprache); 34€ (Alltags-Paket, Paket Berufswelt, Übergänge); 79€ (Komplett-Bundle). Damit liegen alle vier App-Zugänge in einer konsistenteren Größenordnung über ihrem jeweiligen Einzeldeck: Lehrkraft/Eltern 24€ zu 22€ (+9%), Jobcoach/Berufsvorbereitung 26€ zu 22€/34€ (bewusst dazwischen), Mobbing 20€ zu 15€ (+33%). Mobbing liegt damit anteilig etwas höher als Lehrkraft/Eltern, aber in einer nachvollziehbaren Größenordnung — kein Alarmzeichen mehr wie bei den vorherigen 26€. **Weiterhin offen, unabhängig von dieser Harmonisierung:** Die Print-Variante von HB/MB zeigt auf den Verkaufsseiten noch eine Preisspanne (18–20€) statt eines Digistore-tauglichen Festpreises — das wurde hier nicht angefasst, sag Bescheid, falls das auch noch vereinheitlicht werden soll. Bitte trotzdem jeden Preis vor dem Livegang final selbst bestätigen."

old_stand = "Stand: 21.08.2026 (aktualisiert). Diese Anleitung deckt die rollenbasierten Lizenz-Codes ab, die noch kein Digistore24-Produkt haben."
new_stand = "Stand: 22.08.2026 (Preisharmonisierung). Diese Anleitung deckt die rollenbasierten Lizenz-Codes ab, die noch kein Digistore24-Produkt haben."

patch_file(
    "Digistore24_Setup_Guide.md",
    [
        (old_stand, new_stand, "Stand-Zeile"),
        (old_row, new_row, "Mobbing-Tabellenzeile"),
        (old_found, new_found, "mobbing26-Absatz"),
        (old_hint, new_hint, "Preishinweis-Absatz"),
    ],
)

# --- 2) HB_Verkaufsseite.html ---
patch_file(
    "HB_Verkaufsseite.html",
    [
        (
            '<span class="preis-betrag">10 €<span> einmalig</span></span>',
            '<span class="preis-betrag">15 €<span> einmalig</span></span>',
            "HB Digital/PDF-Preis",
        )
    ],
)

# --- 3) MB_Verkaufsseite.html ---
patch_file(
    "MB_Verkaufsseite.html",
    [
        (
            '<span class="preis-betrag">10 €<span> einmalig</span></span>',
            '<span class="preis-betrag">15 €<span> einmalig</span></span>',
            "MB Digital/PDF-Preis",
        )
    ],
)

print("ALLE PATCHES OK")
