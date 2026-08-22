# Digistore24-Setup-Guide · App-Portale (Rollen-Lizenzen)

Stand: 22.08.2026 (Preisharmonisierung). Diese Anleitung deckt die rollenbasierten Lizenz-Codes ab, die noch kein Digistore24-Produkt haben. Die bereits laufenden Produkte (Themen-Bundles Alltag/Berufswelt/Sprache + Komplett-Bundle, Codes `anker26`/`w2tfn1`/`sprache24`/`komplett79`) sind davon nicht betroffen.

## 0. Aktuelle Prioritäts-Entscheidung (21.08.2026)

Anja setzt zunächst **4 der 6 möglichen Produkte** um: Jobcoach, Lehrkraft, Eltern, Mobbing. **INGRA (`sb-ingra26`) und Teamkoordination (`tk-leitung26`) werden erstmal komplett zurückgestellt** — weder bei Digistore24 noch bei eduki gelistet. Diese Anleitung ist entsprechend in "Jetzt" und "Zurückgestellt" sortiert.

## 1. Jetzt einzurichten — 4 Produkte

| Zielgruppe | Code | Vorschlag Produktname | Preis-Idee | Vergleichbares Kartendeck (echter, von dir bestätigter Preis) |
|---|---|---|---|---|
| Jobcoach | `jc-beruf26` | KLARTEXT App-Zugang · Berufsvorbereitung (Jobcoach) | 26,00 € | JD-Deck 22€ / Paket Berufswelt-Bundle 34€ — 26€ liegt bewusst dazwischen |
| Lehrkraft | `lehrkraft24` | KLARTEXT App-Zugang · Lehrkraft | 24,00 € | LK-Deck 22€ — kleiner, konsistenter Aufschlag |
| Eltern | `eltern-anker` | KLARTEXT App-Zugang · Eltern | 24,00 € *(Vorschlag, gleiche Logik wie Lehrkraft — du entscheidest)* | EL-Deck 22€ |
| Mobbing | `mobbing26` | KLARTEXT App-Zugang · Mobbing-Intervention | 20,00 € *(final, Preisharmonisierung 22.08.2026)* | MB-Deck 15€ — konsistenter Aufschlag wie bei den anderen drei |

**Namensänderung Jobcoach → "Berufsvorbereitung":** Auf deinen Wunsch umbenannt, da der Inhalt inhaltlich im Kern Berufsvorbereitung ist. Den Rollen-Code selbst (`jc-beruf26`) und die Rolle in KLARTEXT_Login.html (`jobcoach`) musst du dafür NICHT ändern — nur der nach außen sichtbare Produktname/die Verkaufsseiten-Formulierung ändert sich.

**Zu `mobbing26`:** existiert bereits als funktionierender, getesteter Lizenzcode in KLARTEXT_Login.html (Rolle `mobbing`, `bundle: null`), hat aber wie die anderen 3 noch kein eigenes Digistore24-Produkt. Der Preis ist mit der Preisharmonisierung vom 22.08.2026 final auf 20,00 € festgelegt (siehe Hinweis unten) — keine Vermutung mehr.

**Wichtiger Hinweis zu allen Preisen (Preisharmonisierung vom 22.08.2026):** Am 21.08. lagen HB und MB noch bei 10€ und der Mobbing-App-Zugang beim vorgeschlagenen 26€ — mit Abstand der größte relative Sprung aller vier App-Zugänge (2,6-Fache). Das hast du bereinigt: HB und MB liegen jetzt bei 15€ (statt 10€), der Mobbing-App-Zugang bei 20€ (statt 26€). Aktuelle Werte gesamt: Schnupperpaket kostenlos; 15€ (FS, DaZ-GS, DaZ-Sek I, LRS, OGS, M3, SMI, SP, Krisendeck/FK, HB, MB); 18€ (KD, AT, ADHS, TR, TK, GK, Zonen-Set); 22€ (JD, EL, LK, Insel-Set); 24€ (Paket Sprache); 34€ (Alltags-Paket, Paket Berufswelt, Übergänge); 79€ (Komplett-Bundle). Damit liegen alle vier App-Zugänge in einer konsistenteren Größenordnung über ihrem jeweiligen Einzeldeck: Lehrkraft/Eltern 24€ zu 22€ (+9%), Jobcoach/Berufsvorbereitung 26€ zu 22€/34€ (bewusst dazwischen), Mobbing 20€ zu 15€ (+33%). Mobbing liegt damit anteilig etwas höher als Lehrkraft/Eltern, aber in einer nachvollziehbaren Größenordnung — kein Alarmzeichen mehr wie bei den vorherigen 26€. **Ergänzung (22.08.2026):** Die Print-Variante von HB/MB ist jetzt ebenfalls vereinheitlicht — statt der alten Preisspanne (18–20€) gilt jetzt ein fester Preis von 24€, passend zum shopweiten Muster (Digital-Preis + rund 9€ Print-Aufschlag, wie bei den anderen 15€-Digital-Decks FS, LRS, OGS, SP etc.). Bitte trotzdem jeden Preis vor dem Livegang final selbst bestätigen.

## 2. Zurückgestellt — nicht jetzt einrichten

| Zielgruppe | Code | Status |
|---|---|---|
| Schulbegleiter/INGRA | `sb-ingra26` | Zurückgestellt, weder Digistore24 noch eduki |
| Teamkoordination | `tk-leitung26` | Zurückgestellt, weder Digistore24 noch eduki |

## 3. Pro Produkt: Schritt für Schritt anlegen

Wiederhole das für jedes der 4 Produkte aus Abschnitt 1:

1. **Vendor-Ansicht → Meine Produkte → Produktliste → "Produkt hinzufügen"**
2. Produktname eintragen (aus der Tabelle oben, oder eigene Formulierung), Sprache Deutsch, Produkttyp **Software** wählen (passt am besten zu einem App-Lizenzzugang – kein Mitgliederbereich, kein Webinar).
3. Reiter **"Zahlungspläne"**: Preis eintragen, Zahlungsart "Einmalzahlung" (keine Abo-Logik nötig, da der Lizenzcode dauerhaft gültig ist und nicht pro Zeitraum abläuft).
4. Reiter **"Bestellformular"**: Ein responsives Formular über den Baukasten erstellen oder ein bestehendes Formular (z. B. von `komplett79`) duplizieren und verlinken – spart Zeit, da Design/Wording gleich bleiben kann.
5. Reiter **"Rückgabe"**: Rückgabefrist setzen. Da es sich um digitale Inhalte mit sofortigem Zugriff handelt, brauchst du entweder (a) die reguläre 14-Tage-Widerrufsfrist, oder (b) eine ausdrückliche Verzichtserklärung des Käufers auf das Widerrufsrecht bei sofortigem Zugriff (§ 356 Abs. 5 BGB) – dein bestehendes `SHOP_KLARTEXT_Widerrufsbelehrung.html` regelt das bereits für die anderen Produkte, am besten dieselbe Formulierung/Checkbox-Logik übernehmen. *(Ich bin kein Anwalt – bei Unsicherheit lohnt sich hier einmal ein kurzer Check, z. B. bei deiner Steuerberatung oder einem Fachanwalt für IT-/Vertragsrecht, gerade weil es mehrere neue Produkte auf einmal sind.)*

## 4. Lizenzschlüssel-Zustellung: zwei funktionierende Wege

Ich habe die aktuelle Digistore24-Doku dazu geprüft (Stand 21.08.2026, siehe Quellen unten). Wichtig zu wissen: **Digistore24s eingebaute "Lizenzschlüssel"-Funktion ist für pro Käufer EINZIGARTIGE Schlüssel gebaut** (automatisch generiert, über einen eigenen Lizenzserver, oder aus einer hochgeladenen Liste, die Zeile für Zeile abgearbeitet und dabei aufgebraucht wird). Eine Option "an alle Käufer denselben Code" gibt es in der Doku nicht explizit als eigenes Feature – dein System braucht das aber auch nicht anders, weil dein Code ja bewusst pro Rolle fest und gleich ist (kein Pro-Nutzer-Tracking). Zwei Wege, die damit trotzdem funktionieren:

**Weg A – empfohlen, weil du das Muster schon nutzt:** Eigene Dankeseite pro Produkt (genau wie bei deinen bestehenden Produkten, z. B. `Komplett_Dankeseite.html` oder `MB_Dankeseite.html`). Digistore24 leitet nach Kauf auf die von dir hinterlegte "Danke-Seite-URL" weiter (Reiter "Produkt" bzw. "Lieferung"). Auf dieser Seite schreibst du den festen Code direkt als Text hinein (er ist ja für alle Käufer dieses Produkts identisch) plus Link zur App und kurze Login-Anleitung. Das ist technisch am einfachsten und du hast die volle Kontrolle über Text/Design.

**Weg B – falls du den Code zusätzlich direkt auf Digistore24s eigener Bestellbestätigungsseite/-Mail sehen willst:** Reiter "Lieferung" → Lizenzschlüssel-Typ "Schlüsselliste" wählen und eine Liste hochladen, die **denselben Code mehrfach wiederholt** (z. B. 500 Zeilen mit `jc-beruf26`). Digistore24 vergibt Zeile für Zeile – bei identischem Inhalt bekommt technisch jeder denselben Wert, auch wenn das Feature eigentlich für eindeutige Schlüssel gedacht ist. Funktioniert, ist aber ein Workaround, kein offiziell dokumentiertes Verhalten.

**Offener Punkt, den ich nicht zuverlässig aus der Doku beantworten konnte:** Ob und wie du den *Inhalt* der automatischen Digistore24-Bestellbestätigungsmail selbst anpassen kannst (eigener Text-Baustein, Link, Code), ist in der öffentlichen Hilfe-Doku nicht eindeutig beschrieben. Es gibt laut Digistore24-Hilfe-Center eine separate Sektion "E-Mails, die Digistore24 an Kunden sendet" — die beschreibt aber nur, WAS automatisch verschickt wird, nicht ob/wie du das Autoresponder-Wording änderst. **Bitte einmal direkt in deinem Digistore24-Dashboard nachsehen (Produkt → Reiter "E-Mails" oder "Autoresponder", falls vorhanden) oder kurz den Digistore24-Support fragen** – dafür kann ich dir keine zuverlässige Anleitung schreiben, ohne es selbst im Dashboard gesehen zu haben.

## 5. Reihenfolge-Empfehlung

1. Ein Produkt (z. B. `lehrkraft24`) komplett testweise anlegen inkl. Dankeseite + Rückgaberichtlinie.
2. Mit einer kleinen Testzahlung (Digistore24 "Testkauf"-Funktion) einmal komplett durchklicken – so siehst du selbst, was in der Mail/auf der Bestätigungsseite ankommt, bevor du es 3× weiter wiederholst (Eltern, Mobbing, Jobcoach/Berufsvorbereitung).
3. Erst nach dem erfolgreichen Testkauf die anderen 3 Produkte nach demselben Muster anlegen.
4. INGRA und Teamkoordination erst angehen, wenn du dazu bereit bist — kein Zeitdruck, da bewusst zurückgestellt.

## Hinweis zu "eduki"

Du hast erwähnt, INGRA und Teamkoordination sollen auch bei eduki komplett rausbleiben. Ich habe zu einer eduki-Einrichtung bisher keine Dateien in euren Repos gefunden (nur der Platzhalter-Name "eduki-Profil" taucht als Beispiel-Kategorie in Portale.html auf) — falls du dort ebenfalls Produkte listen willst, sag Bescheid, dann schauen wir uns das als eigenen Schritt an, sobald klar ist, was eduki technisch von dir braucht.

## Quellen (Digistore24 Help Center, abgerufen 21.08.2026)

- [Deliver software licenses automatically](https://help.digistore24.com/hc/en-us/articles/23901096742161-Deliver-software-licenses-automatically)
- [Set up digital product](https://help.digistore24.com/hc/en-us/articles/23461791915537-Set-up-digital-product)
- [Deliver download products automatically](https://help.digistore24.com/hc/en-us/articles/23901109541009-Deliver-download-products-automatically)
- [Emails sent by Digistore24 to customers](https://help.digistore24.com/hc/en-us/articles/23635826058513-Emails-sent-by-Digistore24-to-customers)
