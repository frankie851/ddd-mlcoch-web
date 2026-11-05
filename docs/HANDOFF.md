# HANDOFF – DDD Mlčoch web
datum: 2026-11-05 · předává: krok 01 (návrhy) · přebírá: krok 02 (stavba webu)

## Stav jednou větou
Hotovo: 10 log, 5 návrhů hlavní stránky s přepínačem log, společné texty a galerie `navrhy/index.html`; čeká se na Davidův výběr loga a designu.

## Průběh (odškrtávej po každém kroku, pak commit + push)
- ☑ Krok 0 – základ repozitáře
- ☑ Krok 1 – 10 log
- ☑ Krok 2 – texty + ověření právních bodů
- ☑ Krok 3 – 5 designů
- ☑ Krok 4 – galerie
- ☑ Krok 5 – kontrola v prohlížeči
- ☑ Krok 6 – dokončení předávky
Rozpracováno: nic. Další krok je Davidův výběr a prompt 02.

## Hotovo
### Loga (`navrhy/loga/`)
Každé logo má soubor `logo-NN.svg` (celé logo) a `logo-NN-znacka.svg` (samotná značka, čtverec 100 × 100 – podklad pro favicon).

| č. | název nápadu | v čem je vtip | soubor |
|---|---|---|---|
| 1 | Prst na ústech | Mlčoch = mlčet; prst na ústech, slogan „Po nás je ticho.“ | `logo-01.svg` |
| 2 | Zmlklá vlna | zvuková vlna se uklidní do rovné čáry, „Škůdci zmlknou.“ | `logo-02.svg` |
| 3 | Myš s cedulkou PSST | myš sama drží cedulku „PSST“, „Psst… už jsou pryč.“ (maskot) | `logo-03.svg` |
| 4 | Ztichlý cvrček | cvrček usnul (zZ), „I cvrček ztichl.“ | `logo-04.svg` |
| 5 | Stěhování škůdců | myš s kufříkem odchází, „Škůdci se stěhují.“ (maskot) | `logo-05.svg` |
| 6 | Odznak s hubitelem | retro odznak, pan hubitel s knírem a čepicí mrká (maskot) | `logo-06.svg` |
| 7 | Brouk s bílou vlajkou | brouk mává bílou vlajkou, „Škůdci kapitulují.“ + výstražná páska (maskot) | `logo-07.svg` |
| 8 | DDD jako tři stopy | tři stopy ve tvaru D odcházejí z kruhu, „Stopy vedou pryč.“ (typografické) | `logo-08.svg` |
| 9 | Tři kapky | tři kapky = tři D, prostřední s odškrtnutím, „Čisto. Ticho. Hotovo.“ (typografické) | `logo-09.svg` |
| 10 | Písmeno D jako myš | písmeno D s uchem, očkem, vousky a ocáskem, „Myš? Jen v logu.“ (typografické) | `logo-10.svg` |

Technika log (důležité pro krok 2):
- Text log je zatím **živý text** (`<text>`) s písmem z `navrhy/pisma/`. Samostatný soubor SVG si písma načte přes `<?xml-stylesheet href="../spolecne/pisma.css"?>`; v HTML se logo vkládá inline. **V kroku 2 převést text vybraného loga na křivky** (opentype.js umí číst WOFF z `navrhy/pisma/*.woff`; WOFF2 nečte). Písma jsou podmnožina latin + latin-ext v jednom souboru, takže stačí jeden soubor na řez.
- Barva textu jde přes CSS proměnné `--logo-ink` (název) a `--logo-ink2` (slogan); výchozí jsou tmavé. Na tmavém pozadí stačí nastavit světlé hodnoty (viz `.tmave` v `navrhy/spolecne/galerie.css`). Po převodu na křivky je vhodné připravit dvě varianty souboru (světlé/tmavé pozadí).
- Všechna `id` v logu mají předponu `l01-` … `l10-` (gradient/vzor/clipPath jen u log 1 a 7). Při vkládání více kopií na jednu stránku přidává generátor/přepínač příponu.
- Loga generuje skript `navrhy/nastroje/loga.py` (potřebuje `pip install fonttools`) – měří šířku textu podle písem, aby `viewBox` přesně seděl.

### Designy (`navrhy/designy/`)
| č. | směr | použité logo | barvy | písma | soubor |
|---|---|---|---|---|---|
| 1 | Čistý hygienický | 9 – Tři kapky | bílá, tyrkysová #0f766e, zelená #0b7a43, mátová #eef7f4, tmavě zelený text #10302b | Manrope | `design-1.html` + `design-1.css` |
| 2 | Zemitý venkovský | 5 – Stěhování škůdců | papír #f4ecda se zrnem, olivová #3e4d1d/#55682a, okr #c98b2b, rez #9c4a2f | Fraunces (nadpisy), Source Sans 3 (text) | `design-2.html` + `design-2.css` |
| 3 | Výstražný | 7 – Brouk s bílou vlajkou | žlutá #ffcc00, černá #121212, výstražné pásky | Barlow Condensed (nadpisy), Barlow (text) | `design-3.html` + `design-3.css` |
| 4 | Tmavý technický | 2 – Zmlklá vlna | antracit #0f1419, panely #161d24, limetková #b6f23c, mřížka | Space Grotesk, IBM Plex Sans, IBM Plex Mono | `design-4.html` + `design-4.css` |
| 5 | Retro řemeslný | 6 – Odznak s hubitelem | krémová #f6ead2, červená #c8322b, tmavá #2b2622, modrá #2f5d73 | Alfa Slab One, Pacifico, Bitter | `design-5.html` + `design-5.css` |

Všechny designy mají stejnou HTML strukturu a všech 8 sekcí (hlavička, `#uvod`, `#sluzby`, `#pro-koho`, `#postup`, `#opravneni`, `#kontakt`, patička). Logo je v hlavičce ve slotu `.logo-slot` (pevná výška 56 px, na mobilu 42 px, do 400 px 36 px; šířka automatická). Přepínač loga (`?logo=N` v adrese nebo panel vlevo dole) je jen v návrzích.

### Struktura složky `navrhy/`
- `index.html` – galerie pro Davida
- `loga/` – 10 log + 10 samostatných značek (SVG)
- `designy/` – `design-1..5.html` + vlastní `design-1..5.css`
- `nahledy/` – snímky celé stránky: `design-N-pocitac.jpg` (1440 px zmenšeno na 720 px), `design-N-mobil.jpg` (390 px), `galerie-pocitac.jpg`, `galerie-mobil.jpg`; všechny pod 400 KB
- `spolecne/` – `pisma.css` (@font-face), `zaklad.css` (společný základ designů), `prepinac.js` (přepínač log), `loga.js` (loga jako text pro přepínač – generované), `galerie.css`
- `pisma/` – WOFF2 (web) + WOFF (pro převod na křivky), `pisma/licence/` – licence OFL
- `ikony/` – použité ikony Tabler (SVG) + `LICENSE-tabler.txt`; `mys.svg` je vlastní kresba
- `nastroje/` – `loga.py` (generátor log), `designy.py` (sestaví designy, `loga.js` a galerii z textů; jen standardní knihovna Pythonu). Krok 2 je nepotřebuje – finální web se píše ručně.

## Licence
- Písma (všechna SIL Open Font License 1.1, staženo přes npm balíčky `@expo-google-fonts/*`, zmenšeno na latin + latin-ext nástrojem fonttools):
  Manrope, Fraunces, Source Sans 3, Barlow, Barlow Condensed, Space Grotesk, IBM Plex Sans, IBM Plex Mono, Alfa Slab One, Pacifico, Bitter, Baloo 2 – texty licencí v `navrhy/pisma/licence/`.
- Ikony: Tabler Icons 3.50.0 – MIT (`navrhy/ikony/LICENSE-tabler.txt`, npm `@tabler/icons`). Ikona myši (`mys.svg`), všechna loga a ilustrace v úvodech designů jsou vlastní kresba.
- Žádné fotky ani obrázky odjinud.

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
- Skill `frontend-design` v tomto sezení nebyl k dispozici, návrhy vznikly bez něj.
- Hlavní slogan „Po nás je ticho.“ a humorný nadpis „Tři D, jeden cíl: klid“ (sekce Služby) jsou jediná vtipná místa mimo logo (pravidlo max. 2 nadpisy dodrženo).
- Výčet škůdců a postupů v sekci Služby je obecný popis oboru, ne tvrzení o konkrétní firmě. Pokud firma některou službu nedělá (např. vosy, štěnice, zamlžování), v kroku 2 smazat.
- Věta o „uzamykatelných staničkách“ a „přípravcích povolených pro profesionální použití“ popisuje běžnou správnou praxi; David ať potvrdí, že odpovídá skutečnosti.
- Povinná věta z čl. 72 odst. 1 („Používejte biocidní přípravky bezpečně…“) na webu není, protože web nejmenuje ani nenabízí žádný konkrétní přípravek (opatrnější varianta – viz tabulka výše).
- Sekce 6 se jmenuje „Bezpečnost a odborná způsobilost“; v menu je zkráceně „Oprávnění“ (kotva `#opravneni`).
- Rok v patičce: 2026.
- Kontakt obsahuje i řádky „Kontaktní osoba“ a „Kdy volat“ – nepovinné, lze smazat.
- Na mobilu (pod 960 px) hlavička nezůstává přilepená nahoře, protože menu má dva řádky; na počítači je u designů 1, 3, 4 přilepená.
- Menu na mobilu je zalomené do řádků (bez „hamburgeru“), aby nebyl potřeba JavaScript.

## Otevřené problémy / co neproběhlo
- **Právní body ověřeny jen ze sekundárních zdrojů**: síťové nastavení tohoto cloudového prostředí neumožnilo otevřít eur-lex.europa.eu ani e-sbirka.gov.cz (DNS blokováno). Doporučení: v kroku 2 nebo 3 ověřit znění čl. 72 nařízení 528/2012, § 435 OZ a přesný název vázané živnosti na primárních zdrojích (případně povolit tyto domény v nastavení prostředí).
- Vizuální kontrola **proběhla** (Playwright/Chromium, server v podsložce `/ddd-mlcoch-web/`): snímky 1440 a 390 px prohlédnuty, všech 10 log přepnuto v hlavičce každého designu na 360, 390 a 1440 px, bez vodorovného posouvání (kontrolováno i 360 px), konzole bez chyb, žádné externí požadavky, všechny odkazy a kotvy fungují, žádné `tel:`/`mailto:` odkazy, `noindex` na všech stránkách.
- Loga 4 a 5 mají v tmavé variantě „DDD“ ve středně tmavé barvě (modrá/olivová) – čitelné, ale s menším kontrastem; u vybraného loga v kroku 2 případně zesvětlit pro tmavé pozadí.

## Další krok
David vybere logo a design v galerii a spustí prompt 02.
