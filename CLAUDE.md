# DDD Mlčoch – web firmy (pravidla pro Claude Code)

Jednostránkový web-vizitka firmy DDD Mlčoch (deratizace, dezinsekce, dezinfekce) pro firmy a potravinářské provozy, obce, SVJ a správce domů a zemědělce. Jen česky. Zveřejňuje se přes GitHub Pages z větve `main` na https://frankie851.github.io/ddd-mlcoch-web/.

## Uživatel
David – zadavatel, není programátor. Komunikuj česky a bez žargonu, výsledky popisuj tak, aby jim rozuměl laik.

## Struktura
- `index.html` – web (do výběru designu jen rozcestník na návrhy)
- `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` – ikonky v kořeni (od kroku 2)
- `assets/` – CSS, písma, logo, og-image, obrázky (od kroku 2)
- `obsah/texty.md` – jediný zdroj textů webu; při změně textu uprav i tento soubor
- `navrhy/` – pracovní návrhy log a designů (v kroku 2 se smažou, zůstanou v historii gitu)
- `docs/HANDOFF.md` – stav práce a předávka mezi sezeními (aktualizuj po každém dokončeném kroku)
- `docs/KONTROLA.md` – zpráva z nezávislé kontroly
- `README.md` – návod pro Davida a seznam všech `[DOPLNIT]` (v kroku 2 se přepíše výchozí README z GitHubu)

Když změníš strukturu projektu, uprav i tuto sekci, aby odpovídala skutečnosti.

## Technická pravidla
- Čisté HTML a CSS, JavaScript jen tam, kde bez něj něco nejde. Žádný framework ani build krok – David musí umět upravit text přímo v HTML.
- Všechny cesty relativní (web běží v podsložce `/ddd-mlcoch-web/`, cesta začínající `/` by vedla mimo web). Jediná výjimka: `og:image` v hlavičce musí být absolutní adresa, jinak ho sociální sítě nenačtou.
- Nic externího: písma, skripty, ikony a obrázky jsou v repozitáři. Bez Google Fonts, CDN, analytiky a cookies – kvůli GDPR a rychlosti, díky tomu web nepotřebuje cookie lištu.
- Písma musí obsahovat české znaky (sada latin-ext); kontroluj ř, ů, č, ž.
- Responzivní od 360 px šířky bez vodorovného posouvání; kontrast běžného textu aspoň 4,5 : 1.
- `node_modules/` a dočasné soubory nástrojů do gitu nepatří.

## Obsahová pravidla
- Tón seriózní a věcný. Humor jen v logu (maskotovi), hlavním sloganu a nejvýš ve 2 nadpisech; laskavý, bez krve, mrtvých zvířat a nechutností.
- Nevymýšlej fakta o firmě (roky praxe, certifikáty a jejich čísla, reference, ceny, počty zákazníků, oblast působnosti, dojezdové časy). Neznámý údaj piš jako `[DOPLNIT: co přesně]` a přidej ho do seznamu `[DOPLNIT]` (v kroku 01 v `docs/HANDOFF.md`, od kroku 2 v `README.md`).
- Dokud chybí skutečné telefonní číslo, tlačítko „Zavolat“ vede na sekci kontakt (`#kontakt`), ne na falešné `tel:` číslo.
- Dokud web obsahuje `[DOPLNIT]`, má v hlavičce `<meta name="robots" content="noindex">`. Odstraní se, až budou doplněné všechny údaje a kontrola projde – tím se web „spustí“ pro vyhledávače.
- Nepoužívej výrazy jako „netoxický“, „neškodný“, „100% bezpečný“, „přírodní“, „ekologický / šetrný k životnímu prostředí“ – reklamu na biocidní přípravky je omezuje nařízení EU 528/2012 (čl. 72).
- Nenapodobuj známá loga, postavy ani loga jiných DDD firem.

## Git
- Pracuj ve své pracovní větvi, průběžně commituj a pushuj. Nikdy nepushuj do `main`, nedělej force-push ani nepřepisuj historii – do `main` se změny dostanou až Davidovým „Merge“.

## Při kontrole (nezávislý kontrolor)
Tato pravidla jsou měřítkem kontroly. Kontrolor opravuje jen jednoznačné drobnosti (překlep, nefunkční odkaz, chybějící alternativní text obrázku, chybějící položka v seznamu `[DOPLNIT]`). Všechno ostatní jen zapíše do `docs/KONTROLA.md` a nemění.
