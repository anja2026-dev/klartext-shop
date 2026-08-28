# Digistore24-Produkttexte · „Mein 5-Sekunden-Tagesjournal (Klassenzimmer-Edition)"

Stand: 28.08.2026. Zum direkten Copy-Paste in die Digistore24-Eingabemaske beim Anlegen des neuen Produkts. Ablauf beim Anlegen wie in `Digistore24_Setup_Guide.md` beschrieben (Vendor-Ansicht → Meine Produkte → Produkt hinzufügen).

## 1. Produktdetails (Reiter „Produkt")

| Feld | Wert |
|---|---|
| Produktname | KLARTEXT · Mein 5-Sekunden-Tagesjournal (Klassenzimmer-Edition) |
| Produkttyp | Download-Produkt / eBook (PDF) — Einmalzahlung |
| Sprache | Deutsch |
| Verkaufspreis | 2,90 € (brutto, inkl. MwSt., Einmalzahlung) |
| Danke-Seite-URL | `https://klartext-app-8kl.pages.dev/BAROMETER_KIND.html?guest=true` |
| Auslieferung | Direkt-Weiterleitung auf die Gast-Version des digitalen Barometers (kein Login, keine Speicherung, DSGVO-konform) |

**Hinweis zur Danke-Seite:** Anders als bei deinen bisherigen Produkten (eigene `_Dankeseite.html` in klartext-shop, z. B. `Mobbing-App_Dankeseite.html`) leitest du hier laut deiner Vorgabe im Setup-Prompt direkt auf die App weiter. Ich habe das so übernommen. Falls dir eine eigene, gebrandete Dankeseite lieber ist (wie bei allen anderen Produkten), sag Bescheid — die baue ich dann zusätzlich, mit Link zur App als Call-to-Action.

## 2. Verkaufsstarker Werbetext (für die Digistore24-Bestellseite)

**Headline:** 5 Sekunden am Morgen. Ein Kreuz. Und ein Zustand, den dein Kind endlich zeigen kann, ohne ihn erklären zu müssen.

**Text:** Manche Kinder können morgens nicht in Worte fassen, wie es ihnen geht — aber ein Kreuz auf einer Farbe schaffen sie. Das 5-Sekunden-Tagesjournal macht genau das zum festen Ritual: eine Seite, fünf Farben, kein Schreibzwang.

- ✅ 1 Seite DIN A4, Hoch- oder Querformat — sofort ausdruckbar, kein Bastelaufwand
- 🎨 5-Stufen-Barometer in denselben Farben wie die KLARTEXT-App — Kind und Fachkraft sprechen dieselbe „Sprache", egal ob Papier oder Bildschirm
- ⚪ Eigene Stufe „Grau" für Erschöpfung und Rückzug — bewusst nicht mit „Rot" vermischt (fachliche Begründung siehe unten)
- 🌙 Feierabend-Reflexion mit 6 ankreuzbaren Karten — spielerisch statt therapeutisch, kein Schreibzwang
- ✍️ Eine Zeile für den Vorsatz für morgen — freiwillig, niedrigschwellig
- 📱 QR-Code zur kostenlosen digitalen Version — macht den Wochenverlauf sichtbar
- 🧩 Passt zu Grundschule, Förderschule, OGS, DaZ — auch bewährt bei ADHS und im Autismus-Spektrum

**Wissenschaftlich fundiert gestaltet:**
- Die farbcodierte Selbsteinschätzung folgt dem im Schulkontext etablierten Zones-of-Regulation-Prinzip (Kuypers, 2011)
- Die eigenständige Stufe „Grau" unterscheidet — nach Porges' Polyvagal-Theorie (2011) — bewusst zwischen unruhiger Überaktivierung und stiller Erschöpfung/Shutdown
- Das reizarme, kontrastreiche Layout orientiert sich an den Universal-Design-for-Learning-Leitlinien (CAST, 2018)

*Bewusste Formulierung „wissenschaftlich fundiert gestaltet" statt „wissenschaftlich nachgewiesen wirksam" — dein Konzeptpapier weist ausdrücklich darauf hin, dass die Quellen die Gestaltungsprinzipien belegen, nicht eine Wirksamkeitsstudie zum Tagesjournal selbst. Diese Unterscheidung sollte in der Digistore24-Bestellseite erhalten bleiben.*

## 3. Wichtiger Hinweis zur Prompt-Vorlage

Der Setup-Prompt nannte als wissenschaftliche Basis „GFK nach Rosenberg, Zones of Regulation, Polyvagal-Theorie". Gewaltfreie Kommunikation (Rosenberg) taucht in deinem eigenen Konzeptpapier `eduki_produkt1_Tagesjournal_Konzept.md` aber gar nicht auf. Die dort tatsächlich zitierten Quellen sind Kuypers (Zones of Regulation), Porges (Polyvagal-Theorie), Lieberman et al. (Affect Labeling) und CAST (Universal Design for Learning). Ich habe mich an dein Konzeptpapier gehalten statt an die Prompt-Vorlage, damit hier nichts Unbelegtes im Werbetext landet.

## 4. Volle Quellenangaben

1. Kuypers, L. (2011). *The Zones of Regulation: A Curriculum Designed to Foster Self-Regulation and Emotional Control.* Think Social Publishing.
2. Porges, S. W. (2011). *The Polyvagal Theory: Neurophysiological Foundations of Emotions, Attachment, Communication, and Self-Regulation.* W. W. Norton & Company. (Porges ist mit den Ausgaben 1994 und 2011 bereits in deinem `KLARTEXT_Quellenverzeichnis.html` gelistet.)
3. Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). Putting Feelings Into Words: Affect Labeling Disrupts Amygdala Activity in Response to Affective Stimuli. *Psychological Science*, 18(5), 421–428.
4. CAST (2018). *Universal Design for Learning Guidelines, Version 2.2.* Wakefield, MA: CAST.

Kuypers, Lieberman und CAST stehen noch nicht in deinem zentralen `KLARTEXT_Quellenverzeichnis.html` (nur Porges ist schon drin) — sag Bescheid, falls ich sie dort ergänzen soll.

## 5. Auslieferung der PDF-Datei

Die fertige PDF liegt bereits lokal unter `klartext-app/eduki_outputs/KLARTEXT_tagesjournal.pdf` (erzeugt via `generate_eduki_material.py`). Für eine zusätzliche automatische Digistore24-Auslieferung per E-Mail (Reiter „Lieferung" → Download-Produkt hochladen) kannst du diese Datei direkt hochladen. Das mache ich erfahrungsgemäß nicht per Chrome-Automation für dich (Datei-Uploads scheitern dabei zuverlässig) — bitte manuell hochladen.

## 6. Offener Punkt (nicht geprüft, außerhalb dieses Auftrags)

Die Gast-Version (`BAROMETER_KIND.html?guest=true`) ist als reines Barometer-Tool gebaut. Ob dort aktuell auch ein direkter „PDF herunterladen"-Button sichtbar ist — wie im Setup-Prompt beschrieben („wo er das PDF sofort herunterladen … kann") — habe ich nicht geprüft, weil das eine Änderung an `klartext-app` wäre, nicht an den Shop-Dateien. Sag Bescheid, falls ich das ergänzen soll.

## 7. Status: bereits bei Digistore24 angelegt (28.08.2026)

Produkt ist live im Vendor-Dashboard angelegt (Produkt-ID **727179**, Downloads-Typ, 2,90 € Einmalzahlung EUR, Verkaufsseite- und Danke-Seite-URL eingetragen wie oben). Checkout-Link: `https://www.checkout-ds24.com/product/727179` — bereits in `Tagesjournal_Verkaufsseite.html` eingetragen.

**Noch offen, bevor der Kaufen-Button live gehen kann:**
1. **`klartext-shop`-Repo pushen/deployen** — die Verkaufsseiten-URL (`https://klartext-mentoring.de/Tagesjournal_Verkaufsseite.html`), die bei Digistore24 hinterlegt ist, existiert erst live, sobald du die neuen/geänderten Dateien pushst.
2. **Rückgaberegelung fehlt komplett** — dein Digistore24-Konto hat aktuell (Stand heute) gar keine Rückgabe-Regelung hinterlegt, auch nicht bei deinen anderen laufenden Produkten. Das ist ein rechtlicher Punkt (Widerrufsfrist vs. Verzicht nach § 356 Abs. 5 BGB) — das lege ich bewusst nicht selbst fest, das solltest du (ggf. mit kurzem Check bei einer Steuerberatung/Fachanwalt) entscheiden und selbst im Reiter „Rückgabe-Regelungen" anlegen.
3. **Datei-Auslieferung** (Reiter „Ausliefern") steht auf „Keine Dateien ausliefern" — die PDF wird stattdessen über die Gast-App auf der Dankeseite bereitgestellt. Falls du zusätzlich den automatischen Digistore24-Dateiversand willst, müsstest du `KLARTEXT_tagesjournal.pdf` selbst im Download-Tresor hochladen (Chrome-Automation scheitert dabei erfahrungsgemäß zuverlässig).
4. Noch nicht gemacht: Testkauf. Wie besprochen bestätige ich diesen Schritt erst nach deiner ausdrücklichen Bestätigung im Chat.
