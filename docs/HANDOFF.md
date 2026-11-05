# HANDOFF – DDD Mlčoch web
datum: 2026-11-05 · předává: krok 01 (návrhy) · přebírá: krok 02 (stavba webu)

## Stav jednou větou
Rozpracováno – hotový základ, 10 log a texty; pokračují designy.

## Průběh (odškrtávej po každém kroku, pak commit + push)
- ☑ Krok 0 – základ repozitáře
- ☑ Krok 1 – 10 log
- ☑ Krok 2 – texty + ověření právních bodů
- ☐ Krok 3 – 5 designů
- ☐ Krok 4 – galerie
- ☐ Krok 5 – kontrola v prohlížeči
- ☐ Krok 6 – dokončení předávky
Rozpracováno: krok 3 – 5 designů v `navrhy/designy/`.

## Hotovo
- Loga: (doplní se)
- Designy: (doplní se)
- Struktura složky `navrhy/`: (doplní se)

## Licence
- Písma: (doplní se)
- Ikony: (doplní se)

## Ověřené právní body
| Bod | Výsledek | Zdroj | Datum |
|---|---|---|---|
| Zakázané výrazy (EU 528/2012, čl. 72) | **Ověřeno jen ze sekundárních zdrojů.** Čl. 72 odst. 3: reklama na biocidní přípravek nesmí obsahovat „biocidní přípravek s nízkým rizikem“, „netoxický“, „neškodný“, „přírodní“, „šetrný k životnímu prostředí“, „šetrný ke zvířatům“ ani podobné údaje (SDEU C-296/23 z 20. 6. 2024 vykládá „podobné údaje“ široce). Čl. 72 odst. 1 ukládá do **reklamy na biocidní přípravek** povinnou větu „Používejte biocidní přípravky bezpečně. Před použitím si vždy přečtěte označení a informace o přípravku.“ (anglicky „Use biocides safely. Always read the label and product information before use.“; slovo „biocidní přípravky“ lze nahradit typem přípravku). Zda se článek vztahuje i na web firmy, která přípravky neprodává, ale poskytuje službu, **není jednoznačné** → opatrnější varianta: zakázané výrazy nepoužíváme nikde, konkrétní přípravky nejmenujeme, a proto povinnou větu web neobsahuje. Kdyby web někdy jmenoval nebo nabízel konkrétní přípravky, povinnou větu doplnit. | legislation.gov.uk (text nařízení 528/2012, čl. 72, původní znění EU) – https://www.legislation.gov.uk/eur/2012/528/article/72/adopted/data.html ; WebSearch, shrnutí rozsudku SDEU C-296/23. Primární zdroj eur-lex.europa.eu byl v sezení nedostupný (síťové omezení prostředí). | 2026-11-05 |
| Povinné údaje na webu (OZ § 435) | **Ověřeno jen ze sekundárních zdrojů.** § 435 odst. 1 zákona č. 89/2012 Sb.: každý podnikatel musí na obchodních listinách a v informacích zpřístupňovaných veřejnosti dálkovým přístupem (web) uvádět své **jméno a sídlo**; podnikatel zapsaný ve veřejném rejstříku i **údaj o zápisu** včetně oddílu a vložky; podnikatel zapsaný v jiné evidenci údaj o zápisu do této evidence; a **identifikační číslo (IČO)**, bylo-li přiděleno. Patička proto obsahuje `[DOPLNIT]` pro jméno/firmu, sídlo, IČO a údaj o zápisu. | podnikatel.cz / mesec.cz (znění OZ, Díl 5 – Podnikatel), přednáška SLU Opava „Základní pojmy obchodního práva“. Primární zdroj e-sbirka.gov.cz byl v sezení nedostupný. | 2026-11-05 |
| Název oprávnění k DDD (zák. 258/2000 Sb.) | **Ověřeno jen ze sekundárních zdrojů.** Odborná způsobilost: „odborná způsobilost k výkonu speciální ochranné dezinfekce, dezinsekce a deratizace“ podle **§ 58 zákona č. 258/2000 Sb.** (kurz a zkouška podle vyhlášky č. 490/2000 Sb.; pro práci s vysoce toxickými přípravky zvláštní způsobilost podle § 58 odst. 4). Živnost: vázaná živnost uváděná jako „**Speciální ochranná dezinfekce, dezinsekce a deratizace**“ (příloha č. 2 živnostenského zákona č. 455/1991 Sb.) – přesné znění se v zdrojích mírně liší (někde „Provádění speciální ochranné…“), proto je na webu jako `[DOPLNIT: přesný název vázané živnosti podle výpisu z živnostenského rejstříku]`. Sekce 6 se jmenuje „Bezpečnost a odborná způsobilost“. | mze.gov.cz (Otázky a odpovědi – vázaná živnost Speciální ochranná dezinfekce, dezinsekce a deratizace), khsstc.cz, businessinfo.cz, znění vyhlášky 490/2000 Sb. na epravo.cz. Primární zdroj e-sbirka.gov.cz byl nedostupný. | 2026-11-05 |

## Seznam [DOPLNIT]
Všechny se vyskytují v `obsah/texty.md` a ve všech 5 designech `navrhy/designy/design-N.html`.
- `[DOPLNIT: telefon]` – hlavička (tlačítko), úvod (tlačítko Zavolat vede na #kontakt), kontakt
- `[DOPLNIT: e-mail]` – kontakt
- `[DOPLNIT: jméno a příjmení]` – kontakt (kontaktní osoba)
- `[DOPLNIT: IČO]` – kontakt, patička
- `[DOPLNIT: oblast působnosti]` – kontakt
- `[DOPLNIT: kdy je možné volat]` – kontakt
- `[DOPLNIT: osvědčení o odborné způsobilosti – vydal, číslo, datum]` – sekce oprávnění
- `[DOPLNIT: přesný název vázané živnosti podle výpisu z živnostenského rejstříku]` – sekce oprávnění
- `[DOPLNIT: pojištění odpovědnosti – ano/ne, případně smazat]` – sekce oprávnění
- `[DOPLNIT: jméno a příjmení podnikatele nebo obchodní firma]` – patička
- `[DOPLNIT: adresa sídla nebo místa podnikání]` – patička
- `[DOPLNIT: údaj o zápisu …]` – patička

## Předpoklady
- Skill `frontend-design` v tomto sezení není k dispozici, návrhy vznikly bez něj.

## Otevřené problémy / co neproběhlo
- (zatím nic)

## Další krok
David vybere logo a design v galerii a spustí prompt 02.
