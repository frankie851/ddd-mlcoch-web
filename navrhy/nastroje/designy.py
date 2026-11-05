"""Sestaví návrhy hlavní stránky navrhy/designy/design-1..5.html a navrhy/spolecne/loga.js.

Spuštění:  python3 navrhy/nastroje/designy.py   (jen standardní knihovna Pythonu)
Texty odpovídají obsah/texty.md. Vzhled je v navrhy/designy/design-N.css.
Výsledné HTML je obyčejný statický soubor – generátor jen šetří ruční kopírování
stejných textů do pěti návrhů. V kroku 2 se finální web píše ručně, bez generátoru.
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def logo_svg(n, suffix):
    s = open(os.path.join(ROOT, "loga", f"logo-{n:02d}.svg"), encoding="utf-8").read()
    s = s[s.index("<svg"):].strip()
    return re.sub(r"(l\d\d-[\w-]+)", r"\1-" + suffix, s)

def ikona(name):
    s = open(os.path.join(ROOT, "ikony", name + ".svg"), encoding="utf-8").read()
    s = s[s.index("<svg"):]
    s = re.sub(r'\s(width|height|class)="[^"]*"', "", s)
    s = s.replace("<svg", '<svg class="ikona" aria-hidden="true" focusable="false"', 1)
    s = re.sub(r"\s*\n\s*", " ", s).replace('<path stroke="none" d="M0 0h24v24H0z" fill="none" /> ', "")
    return s.strip()

def D(t):
    """Zvýrazní [DOPLNIT: …]."""
    return re.sub(r"\[DOPLNIT: ([^\]]+)\]", r'<span class="doplnit">[DOPLNIT: \1]</span>', t)

# ------------------------------------------------------------------ texty (= obsah/texty.md)
MENU = [("sluzby", "Služby"), ("pro-koho", "Pro koho"), ("postup", "Postup"), ("opravneni", "Oprávnění"), ("kontakt", "Kontakt")]
SLUZBY = [
 ("mys", "Deratizace", "Hubení hlodavců – potkanů a myší.",
  "sklady, výrobny, kuchyně, sklepy, kanalizační přípojky, zemědělské objekty.",
  "najdeme místa výskytu a cesty, kudy hlodavci pronikají, rozmístíme zabezpečené nástražné staničky a doporučíme, jak vstupy uzavřít."),
 ("bug", "Dezinsekce", "Hubení a omezování hmyzu – švábů, rusů, mravenců, much, vos, štěnic, blech a skladištních škůdců.",
  "potravinářské a skladové provozy, bytové domy, ubytovací zařízení, stáje.",
  "druh hmyzu určíme, zvolíme vhodný postup (postřik, gel, monitorovací pasti) a výsledek ověříme kontrolou."),
 ("droplet", "Dezinfekce", "Ničení choroboplodných zárodků – bakterií, virů a plísní – na plochách a v prostorech.",
  "provozovny, společné prostory domů, stáje a místa po výskytu škůdců.",
  "podle účelu zvolíme způsob (postřik, zamlžování, otěr) a přípravky schválené pro dané použití."),
]
PROKOHO = [
 ("tools-kitchen-2", "Potravinářské provozy",
  "Restaurace, jídelny, výrobny, pekárny a sklady potravin. Zajistíme pravidelné kontroly jako součást systému HACCP, vedeme evidenci monitorovacích míst a ke každé návštěvě předáme protokol pro hygienickou kontrolu."),
 ("building-community", "Obce, SVJ a správci domů",
  "Bytové domy, školy, úřady, sklepy a kanalizace. Domluvíme termín s ohledem na obyvatele, společné prostory označíme a výsledek zásahu doložíme protokolem."),
 ("tractor", "Zemědělci a farmy",
  "Stáje, sýpky, seníky a sklady krmiv. Postup volíme s ohledem na hospodářská zvířata a uskladněné komodity, umíme i opakovaný zásah podle sezóny."),
]
POSTUP = [
 ("search", "Prohlídka", "Prohlédneme objekt, určíme škůdce, rozsah výskytu a příčiny."),
 ("clipboard-check", "Návrh zásahu", "Navrhneme postup, termín a opatření, která má provést zákazník."),
 ("spray", "Zásah", "Provedeme deratizaci, dezinsekci nebo dezinfekci a předáme pokyny pro pobyt v ošetřených prostorách."),
 ("file-certificate", "Kontrola a protokol", "Výsledek zkontrolujeme, předáme protokol o provedení a u smluvních zákazníků plánujeme další pravidelné kontroly."),
]
OPRAVNENI = [
 ("Osvědčení o odborné způsobilosti k výkonu speciální ochranné dezinfekce, dezinsekce a deratizace", "[DOPLNIT: osvědčení o odborné způsobilosti – vydal, číslo, datum]"),
 ("Živnostenské oprávnění", "[DOPLNIT: přesný název vázané živnosti podle výpisu z živnostenského rejstříku]"),
 ("Pojištění odpovědnosti", "[DOPLNIT: pojištění odpovědnosti – ano/ne, případně smazat]"),
]
KONTAKT = [
 ("user", "Kontaktní osoba", "[DOPLNIT: jméno a příjmení]"),
 ("phone", "Telefon", "[DOPLNIT: telefon]"),
 ("mail", "E-mail", "[DOPLNIT: e-mail]"),
 ("id", "IČO", "[DOPLNIT: IČO]"),
 ("map-pin", "Oblast působnosti", "[DOPLNIT: oblast působnosti]"),
 ("clock", "Kdy volat", "[DOPLNIT: kdy je možné volat]"),
]
PATICKA = [
 ("Podnikatel", "[DOPLNIT: jméno a příjmení podnikatele nebo obchodní firma]"),
 ("Sídlo", "[DOPLNIT: adresa sídla nebo místa podnikání]"),
 ("IČO", "[DOPLNIT: IČO]"),
 ("Zápis v rejstříku", "[DOPLNIT: údaj o zápisu – např. „zapsán v živnostenském rejstříku“, u obchodní společnosti soud, oddíl a vložka obchodního rejstříku]"),
]

# ------------------------------------------------------------------ dekorace jednotlivých návrhů
HERO = {}
HERO[1] = """<svg viewBox="0 0 420 380" class="uvod__kresba" aria-hidden="true" focusable="false">
  <rect x="40" y="30" width="300" height="320" rx="18" fill="#fff" stroke="#d5e3df" stroke-width="2"/>
  <rect x="150" y="16" width="80" height="30" rx="8" fill="#0f766e"/>
  <rect x="70" y="80" width="150" height="14" rx="7" fill="#0f3d38"/>
  <rect x="70" y="104" width="220" height="10" rx="5" fill="#cfe3de"/>
  <g font-family="Manrope, sans-serif" font-weight="700" font-size="17" fill="#0f3d38">
    <circle cx="86" cy="160" r="14" fill="#e3f4ef"/><path d="M79 160l5 5 10-10" fill="none" stroke="#10a35a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><text x="112" y="166">Prohlídka</text>
    <circle cx="86" cy="210" r="14" fill="#e3f4ef"/><path d="M79 210l5 5 10-10" fill="none" stroke="#10a35a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><text x="112" y="216">Zásah</text>
    <circle cx="86" cy="260" r="14" fill="#e3f4ef"/><path d="M79 260l5 5 10-10" fill="none" stroke="#10a35a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><text x="112" y="266">Kontrola</text>
    <circle cx="86" cy="310" r="14" fill="#e3f4ef"/><path d="M79 310l5 5 10-10" fill="none" stroke="#10a35a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><text x="112" y="316">Protokol</text>
  </g>
  <circle cx="330" cy="290" r="62" fill="#10a35a"/>
  <path d="M302 290l20 20 36-38" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="370" cy="70" r="10" fill="#7dd3c0"/><circle cx="395" cy="110" r="6" fill="#0ea5e9"/><circle cx="18" cy="250" r="8" fill="#7dd3c0"/>
</svg>"""
HERO[2] = """<svg viewBox="0 0 520 300" class="uvod__kresba" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMax slice">
  <circle cx="400" cy="80" r="44" fill="#e9b949"/>
  <path d="M0 200 Q130 140 260 180 T520 160 V300 H0Z" fill="#9aa65a"/>
  <path d="M0 240 Q160 190 300 230 T520 220 V300 H0Z" fill="#6f7d36"/>
  <g stroke="#56622a" stroke-width="3" stroke-linecap="round"><path d="M40 270l30-14M90 280l40-18M150 286l44-20M220 292l50-22M300 294l52-22M380 292l50-20M450 288l50-20"/></g>
  <g transform="translate(250 112)"><path d="M0 70V30L45 0l45 30v40Z" fill="#9c4a2f"/><path d="M-6 32 45-4l51 36" fill="none" stroke="#5e2c1b" stroke-width="7" stroke-linejoin="round"/><rect x="33" y="40" width="24" height="30" fill="#f3e6c8"/><path d="M33 40l24 30M57 40 33 70" stroke="#9c4a2f" stroke-width="3"/></g>
  <g transform="translate(110 148)"><rect x="0" y="0" width="16" height="50" fill="#f3e6c8"/><path d="M-4 2 8-12 20 2Z" fill="#9c4a2f"/></g>
  <g fill="#3d4520" opacity=".8"><g transform="translate(372 214) rotate(-12)"><ellipse rx="3" ry="2"/><circle cx="5" cy="-3" r="1.2"/><circle cx="6" cy="0" r="1.2"/><circle cx="5" cy="3" r="1.2"/></g>
  <g transform="translate(398 206) rotate(-12)"><ellipse rx="3" ry="2"/><circle cx="5" cy="-3" r="1.2"/><circle cx="6" cy="0" r="1.2"/><circle cx="5" cy="3" r="1.2"/></g>
  <g transform="translate(424 200) rotate(-12)"><ellipse rx="3" ry="2"/><circle cx="5" cy="-3" r="1.2"/><circle cx="6" cy="0" r="1.2"/><circle cx="5" cy="3" r="1.2"/></g>
  <g transform="translate(450 192) rotate(-12)"><ellipse rx="3" ry="2"/><circle cx="5" cy="-3" r="1.2"/><circle cx="6" cy="0" r="1.2"/><circle cx="5" cy="3" r="1.2"/></g></g>
</svg>"""
HERO[3] = """<div class="uvod__razitko" aria-hidden="true"><span>Zásahová</span><span>jednotka</span><span>DDD</span></div>"""
HERO[4] = """<svg viewBox="0 0 400 400" class="uvod__kresba" aria-hidden="true" focusable="false">
  <defs><radialGradient id="d4-zar" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#b6f23c" stop-opacity=".22"/><stop offset="1" stop-color="#b6f23c" stop-opacity="0"/></radialGradient></defs>
  <circle cx="200" cy="200" r="190" fill="url(#d4-zar)"/>
  <g fill="none" stroke="#3a4552" stroke-width="1.5"><circle cx="200" cy="200" r="60"/><circle cx="200" cy="200" r="120"/><circle cx="200" cy="200" r="180"/><path d="M20 200h360M200 20v360"/></g>
  <g class="radar"><path d="M200 200 L200 20 A180 180 0 0 1 327 73 Z" fill="#b6f23c" opacity=".16"/><path d="M200 200V20" stroke="#b6f23c" stroke-width="2"/></g>
  <g fill="#b6f23c"><circle cx="280" cy="120" r="5"/><circle cx="120" cy="270" r="5"/><circle cx="300" cy="300" r="5"/></g>
  <g fill="none" stroke="#b6f23c" stroke-width="1.5" opacity=".6"><circle cx="280" cy="120" r="12"/><circle cx="120" cy="270" r="12"/><circle cx="300" cy="300" r="12"/></g>
  <g font-family="'IBM Plex Mono', monospace" font-size="13" fill="#9fb0bf"><text x="294" y="112">A-03</text><text x="134" y="262">B-11</text><text x="314" y="292">C-07</text></g>
</svg>"""
HERO[5] = """<div class="uvod__odznak" aria-hidden="true">
  <svg viewBox="0 0 320 320" focusable="false">
    <g class="paprsky" fill="#e9c98f">""" + "".join(
        f'<path d="M160 160 L{160+156*__import__("math").cos(__import__("math").radians(a)):.1f} {160+156*__import__("math").sin(__import__("math").radians(a)):.1f} L{160+156*__import__("math").cos(__import__("math").radians(a+7.5)):.1f} {160+156*__import__("math").sin(__import__("math").radians(a+7.5)):.1f}Z"/>'
        for a in range(0, 360, 15)) + """</g>
    <circle cx="160" cy="160" r="112" fill="#c8322b"/>
    <circle cx="160" cy="160" r="102" fill="#f6ead2"/>
    <circle cx="160" cy="160" r="70" fill="none" stroke="#2b2622" stroke-width="2" stroke-dasharray="4 5"/>
    <defs><path id="d5-oblouk" d="M76 160a84 84 0 0 1 168 0"/><path id="d5-oblouk2" d="M66 160a94 94 0 0 0 188 0"/></defs>
    <text font-family="'Barlow Condensed', sans-serif" font-weight="700" font-size="15" letter-spacing="1.6" fill="#2b2622"><textPath href="#d5-oblouk" startOffset="50%" text-anchor="middle">DERATIZACE · DEZINSEKCE</textPath></text>
    <text font-family="'Barlow Condensed', sans-serif" font-weight="700" font-size="15" letter-spacing="2.4" fill="#2b2622"><textPath href="#d5-oblouk2" startOffset="50%" text-anchor="middle">DEZINFEKCE</textPath></text>
    <path d="M80 151l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1zM240 151l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z" fill="#c8322b"/>
    <text x="160" y="170" text-anchor="middle" font-family="'Alfa Slab One', serif" font-size="44" fill="#c8322b">DDD</text>
    <text x="160" y="200" text-anchor="middle" font-family="'Pacifico', cursive" font-size="20" fill="#2b2622">a je klid</text>
  </svg>
</div>"""

CONFIG = {
 1: dict(nazev="Čistý hygienický", logo=9, tmava_hlavicka=False, tmava_paticka=True),
 2: dict(nazev="Zemitý venkovský", logo=5, tmava_hlavicka=False, tmava_paticka=True),
 3: dict(nazev="Výstražný", logo=7, tmava_hlavicka=True, tmava_paticka=True),
 4: dict(nazev="Tmavý technický", logo=2, tmava_hlavicka=True, tmava_paticka=True),
 5: dict(nazev="Retro řemeslný", logo=6, tmava_hlavicka=False, tmava_paticka=True),
}

def page(n):
    c = CONFIG[n]
    I = ikona
    menu = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in MENU)
    sluzby = "".join(f"""
        <article class="sluzba">
          <div class="sluzba__ikona">{I(ic)}</div>
          <h3>{h}</h3>
          <p class="sluzba__co">{co}</p>
          <p><strong>Kde:</strong> {kde}</p>
          <p><strong>Jak:</strong> {jak}</p>
        </article>""" for ic, h, co, kde, jak in SLUZBY)
    prokoho = "".join(f"""
        <article class="skupina">
          <div class="skupina__ikona">{I(ic)}</div>
          <h3>{h}</h3>
          <p>{t}</p>
        </article>""" for ic, h, t in PROKOHO)
    postup = "".join(f"""
        <li class="krok">
          <span class="krok__cislo">{i}</span>
          <div class="krok__ikona">{I(ic)}</div>
          <h3>{h}</h3>
          <p>{t}</p>
        </li>""" for i, (ic, h, t) in enumerate(POSTUP, 1))
    opr = "".join(f"""
            <li>{I('certificate')}<div><strong>{h}</strong><br>{D(v)}</div></li>""" for h, v in OPRAVNENI)
    kontakt = "".join(f"""
          <div class="kontakt__polozka{' kontakt__polozka--tel' if ic == 'phone' else ''}">
            <dt>{I(ic)}{h}</dt>
            <dd>{D(v)}</dd>
          </div>""" for ic, h, v in KONTAKT)
    paticka = "".join(f"<li><span>{h}:</span> {D(v)}</li>" for h, v in PATICKA)
    return f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Návrh {n} – {c['nazev']} · DDD Mlčoch</title>
<meta name="description" content="DDD Mlčoch – deratizace, dezinsekce a dezinfekce pro firmy, potravinářské provozy, obce, SVJ a zemědělce.">
<link rel="stylesheet" href="../spolecne/pisma.css">
<link rel="stylesheet" href="../spolecne/zaklad.css">
<link rel="stylesheet" href="design-{n}.css">
</head>
<body class="d{n}" data-vychozi-logo="{c['logo']}">
<!-- NÁVRH {n}: {c['nazev']}. Texty odpovídají obsah/texty.md. Vygenerováno skriptem navrhy/nastroje/designy.py. -->
<a class="skip" href="#obsah">Přeskočit na obsah</a>

<header class="hlavicka{' tmave' if c['tmava_hlavicka'] else ''}">
  <div class="wrap hlavicka__in">
    <a class="logo-slot" href="#uvod" aria-label="DDD Mlčoch – na začátek stránky" data-logo-slot>{logo_svg(c['logo'], 'h')}</a>
    <nav class="menu" aria-label="Hlavní menu"><ul>{menu}</ul></nav>
    <!-- Až bude známé číslo: href="tel:+420XXXXXXXXX" a text čísla. Do té doby odkaz na #kontakt. -->
    <a class="btn btn--tel" href="#kontakt">{I('phone')}<span class="doplnit">[DOPLNIT: telefon]</span></a>
  </div>
</header>

<main id="obsah">
  <section id="uvod" class="uvod">
    <div class="wrap uvod__in">
      <div class="uvod__text">
        <p class="nadtitulek">Deratizace · Dezinsekce · Dezinfekce</p>
        <h1>Po nás je ticho.</h1>
        <p class="perex">Zbavíme provozovny, domy a hospodářství hlodavců, hmyzu i choroboplodných zárodků – a pomůžeme jim zůstat čisté i dál.</p>
        <div class="akce">
          <a class="btn btn--hlavni" href="#kontakt">{I('phone')}Zavolat</a>
          <a class="btn btn--vedlejsi" href="#sluzby">Co děláme {I('arrow-right')}</a>
        </div>
      </div>
      <div class="uvod__obr">{HERO[n]}</div>
    </div>
  </section>

  <section id="sluzby" class="sekce sluzby">
    <div class="wrap">
      <header class="sekce__hlava">
        <h2>Tři D, jeden cíl: klid</h2>
        <p>Zásah vždy přizpůsobíme provozu, druhu škůdce a požadavkům hygieny.</p>
      </header>
      <div class="sluzby__mrizka">{sluzby}
      </div>
    </div>
  </section>

  <section id="pro-koho" class="sekce prokoho">
    <div class="wrap">
      <header class="sekce__hlava"><h2>Pro koho pracujeme</h2></header>
      <div class="prokoho__mrizka">{prokoho}
      </div>
    </div>
  </section>

  <section id="postup" class="sekce postup">
    <div class="wrap">
      <header class="sekce__hlava"><h2>Jak postupujeme</h2></header>
      <ol class="postup__kroky">{postup}
      </ol>
    </div>
  </section>

  <section id="opravneni" class="sekce opravneni">
    <div class="wrap opravneni__in">
      <div class="opravneni__text">
        <h2>Bezpečnost a odborná způsobilost</h2>
        <p>Speciální ochrannou deratizaci, dezinsekci a dezinfekci smí profesionálně provádět jen osoba s odbornou způsobilostí podle § 58 zákona č. 258/2000 Sb., o ochraně veřejného zdraví, a s příslušným živnostenským oprávněním.</p>
        <p>Používáme přípravky povolené pro profesionální použití a pracujeme podle návodu k jejich použití. Ošetřené prostory označíme, nástrahy umisťujeme do uzamykatelných staniček a před zásahem i po něm předáme pokyny, jak se v prostorech chovat.</p>
      </div>
      <ul class="opravneni__seznam">{opr}
      </ul>
    </div>
  </section>

  <section id="kontakt" class="sekce kontakt">
    <div class="wrap kontakt__in">
      <div class="kontakt__uvod">
        <h2>Kontakt</h2>
        <p>Zavolejte nebo napište. Domluvíme prohlídku a navrhneme postup.</p>
        <!-- Až bude známé číslo, přidat tlačítko: <a class="btn btn--hlavni" href="tel:+420XXXXXXXXX">Zavolat</a> -->
      </div>
      <dl class="kontakt__udaje">{kontakt}
      </dl>
    </div>
  </section>
</main>

<footer class="paticka{' tmave' if c['tmava_paticka'] else ''}">
  <div class="wrap paticka__in">
    <div class="paticka__znacka">
      <span class="logo-slot logo-slot--paticka" data-logo-slot>{logo_svg(c['logo'], 'f')}</span>
      <p><strong>DDD Mlčoch</strong> – deratizace, dezinsekce, dezinfekce</p>
    </div>
    <ul class="paticka__udaje">{paticka}</ul>
    <p class="paticka__copy">© 2026 DDD Mlčoch</p>
  </div>
</footer>

<script src="../spolecne/loga.js"></script>
<script src="../spolecne/prepinac.js"></script>
</body>
</html>
"""

# ------------------------------------------------------------------ galerie navrhy/index.html
LOGA_INFO = {
 1: ("Prst na ústech", "Mlčoch jako „mlčet“: prst na ústech říká „pst“ a slogan „Po nás je ticho.“ slibuje, že škůdce už nikdo neuslyší."),
 2: ("Zmlklá vlna", "Zvuková vlna, která se uklidní do rovné čáry – škůdci zmlknou. Vtip je tichý a technický, hodí se k seriózní firmě."),
 3: ("Myš s cedulkou PSST", "Myš sama drží cedulku „PSST“ – i ona ví, že u Mlčocha se nedělá hluk. Slogan „Psst… už jsou pryč.“"),
 4: ("Ztichlý cvrček", "Cvrček, který jinak cvrká celou noc, sladce usnul (zZ). „I cvrček ztichl.“"),
 5: ("Stěhování škůdců", "Myš si sbalila kufřík a odchází za humna – škůdci se stěhují, nikomu se nic nestalo."),
 6: ("Odznak s hubitelem", "Sympatický pan hubitel s knírem a čepicí mrká z retro odznaku jako ze staré plechové cedule."),
 7: ("Brouk s bílou vlajkou", "Brouk mává bílou vlajkou – škůdci kapitulují. Pod názvem výstražná páska."),
 8: ("DDD jako tři stopy", "Tři stopy ve tvaru písmene D odcházejí z kruhu – v jedné značce je DDD i odchod škůdců."),
 9: ("Tři kapky", "Tři kapky jsou tři D, prostřední s odškrtnutím. Slogan „Čisto. Ticho. Hotovo.“ nenápadně hraje na jméno."),
 10: ("Písmeno D jako myš", "Písmeno D má ucho, očko, vousky a ocásek. Slogan „Myš? Jen v logu.“"),
}
DESIGNY_INFO = {
 1: ("Čistý hygienický", "Hodně bílé, tyrkysová a svěží zelená, úhledné karty jako v laboratoři. Působí jako spolehlivý partner pro potravinářské provozy a kontroly HACCP."),
 2: ("Zemitý venkovský", "Papírová textura, olivová a okrová, patkové písmo a kreslená krajina se statkem. Vlídný a usedlý – míří hlavně na farmy a obce."),
 3: ("Výstražný", "Žlutá a černá jako výstražná páska, velké úzké písmo a razítko „zásahová jednotka“. Rázný a nepřehlédnutelný."),
 4: ("Tmavý technický", "Antracitové pozadí s jemnou mřížkou, jedna limetková barva a „radar“ v úvodu. Precizní a moderní."),
 5: ("Retro řemeslný", "Krémová a červená, nálepky s tlustým obrysem a odznak s paprsky ve stylu 50. let. Poctivé řemeslo, snadno zapamatovatelné."),
}

def znacka_svg(n, suffix):
    s = open(os.path.join(ROOT, "loga", f"logo-{n:02d}-znacka.svg"), encoding="utf-8").read()
    s = s[s.index("<svg"):].strip()
    return re.sub(r"(l\d\d-[\w-]+)", r"\1-" + suffix, s)

def jpg_rozmer(nazev, vychozi):
    """Rozměr JPG snímku (šířka, výška) – jen standardní knihovna."""
    cesta = os.path.join(ROOT, "nahledy", nazev)
    try:
        with open(cesta, "rb") as f:
            d = f.read()
        i = 2
        while i < len(d):
            m, ln = d[i + 1], int.from_bytes(d[i + 2:i + 4], "big")
            if m in (0xC0, 0xC1, 0xC2):
                return int.from_bytes(d[i + 7:i + 9], "big"), int.from_bytes(d[i + 5:i + 7], "big")
            i += 2 + ln
    except OSError:
        pass
    return vychozi

def galerie():
    loga = ""
    for n in range(1, 11):
        nazev, vtip = LOGA_INFO[n]
        loga += f"""
      <article class="logo-karta" id="logo-{n}">
        <h3><span class="cislo">{n}</span> {nazev}</h3>
        <p>{vtip}</p>
        <div class="logo-nahled svetle" aria-label="Logo {n} na světlém pozadí">{logo_svg(n, 'gs')}</div>
        <div class="logo-nahled tmave" aria-label="Logo {n} na tmavém pozadí">{logo_svg(n, 'gt')}</div>
        <div class="znacky"><span>Samotná značka:</span><span class="z32" title="32 × 32 px">{znacka_svg(n, 'z32')}</span><span class="z64" title="64 × 64 px">{znacka_svg(n, 'z64')}</span><small>32 px a 64 px</small></div>
      </article>"""
    designy = ""
    for n, (nazev, nalada) in DESIGNY_INFO.items():
        designy += f"""
      <article class="design-karta" id="design-{n}">
        <div class="design-karta__text">
          <h3><span class="cislo">{n}</span> {nazev}</h3>
          <p>{nalada}</p>
          <p class="drobne">Výchozí logo: č. {CONFIG[n]['logo']} · v návrhu jde přepnout na kterékoli z 10 log.</p>
          <a class="otevrit" href="designy/design-{n}.html">Otevřít celý návrh (můžeš v něm přepínat loga)</a>
        </div>
        <div class="nahledy">
          <figure class="nahled nahled--pocitac"><figcaption>Počítač</figcaption>
            <div class="nahled__okno"><img src="nahledy/design-{n}-pocitac.jpg" alt="Náhled návrhu {n} na počítači (celá stránka)" loading="lazy" data-ramec="designy/design-{n}.html" width="{jpg_rozmer(f'design-{n}-pocitac.jpg', (720, 1800))[0]}" height="{jpg_rozmer(f'design-{n}-pocitac.jpg', (720, 1800))[1]}"></div></figure>
          <figure class="nahled nahled--mobil"><figcaption>Mobil</figcaption>
            <div class="nahled__okno"><img src="nahledy/design-{n}-mobil.jpg" alt="Náhled návrhu {n} na mobilu (celá stránka)" loading="lazy" data-ramec="designy/design-{n}.html" width="{jpg_rozmer(f'design-{n}-mobil.jpg', (390, 3000))[0]}" height="{jpg_rozmer(f'design-{n}-mobil.jpg', (390, 3000))[1]}"></div></figure>
        </div>
      </article>"""
    html = f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Návrhy loga a webu · DDD Mlčoch</title>
<link rel="stylesheet" href="spolecne/pisma.css">
<link rel="stylesheet" href="spolecne/galerie.css">
</head>
<body>
<!-- Vygenerováno skriptem navrhy/nastroje/designy.py -->
<header class="hlava">
  <div class="obal">
    <p class="nadtitulek">DDD Mlčoch · pracovní návrhy</p>
    <h1>Vyber logo a design webu</h1>
    <div class="navod">
      <p><strong>Vyber jedno logo (číslo) a jeden design (číslo).</strong> Můžeš je libovolně kombinovat a připsat přání, např. <em>„logo 4, design 2, ale barvy z designu 5“</em>. Volbu napiš do promptu 02.</p>
      <p>Texty jsou ve všech pěti designech stejné, porovnáváš jen vzhled. Žluté rámečky <span class="doplnit">[DOPLNIT: …]</span> označují údaje, které je potřeba doplnit (telefon, IČO, oprávnění…).</p>
    </div>
    <nav class="skoky" aria-label="Rychlé odkazy"><a href="#loga">10 log</a><a href="#designy">5 designů</a></nav>
  </div>
</header>
<main>
  <section id="loga" class="obal">
    <h2>Loga</h2>
    <p class="uvodni">Každé logo je ukázané na světlém i tmavém pozadí. Samotná značka (obrázek bez textu) je ve velikosti ikonky prohlížeče – 32 px a 64 px.</p>
    <div class="loga-mrizka">{loga}
    </div>
  </section>
  <section id="designy" class="obal">
    <h2>Designy hlavní stránky</h2>
    <p class="uvodni">Náhledy ukazují celou stránku – dají se posouvat. Po otevření návrhu najdeš vlevo dole panel „Vyzkoušet logo: 1–10“.</p>
    <div class="designy-seznam">{designy}
    </div>
  </section>
</main>
<footer class="obal paticka"><p>Pracovní návrhy – po výběru se složka <code>navrhy/</code> smaže (zůstane v historii). <a href="../">Zpět na rozcestník</a></p></footer>
<script>
/* Když chybí snímek náhledu, ukáže se místo něj zmenšený živý návrh. */
document.querySelectorAll('img[data-ramec]').forEach(function (img) {{
  img.addEventListener('error', function () {{
    var f = document.createElement('iframe');
    f.src = img.getAttribute('data-ramec'); f.title = img.alt; f.loading = 'lazy';
    f.className = img.closest('.nahled--mobil') ? 'ramec ramec--mobil' : 'ramec';
    img.replaceWith(f);
  }});
}});
</script>
</body>
</html>
"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("galerie")

def main():
    loga = {}
    for n in range(1, 11):
        s = open(os.path.join(ROOT, "loga", f"logo-{n:02d}.svg"), encoding="utf-8").read()
        loga[n] = s[s.index("<svg"):].strip()
    with open(os.path.join(ROOT, "spolecne", "loga.js"), "w", encoding="utf-8") as fh:
        fh.write("/* Vygenerováno skriptem navrhy/nastroje/designy.py z navrhy/loga/logo-NN.svg – needitovat ručně. */\n")
        fh.write("window.DDD_LOGA = " + json.dumps(loga, ensure_ascii=False, indent=0) + ";\n")
    for n in CONFIG:
        with open(os.path.join(ROOT, "designy", f"design-{n}.html"), "w", encoding="utf-8") as fh:
            fh.write(page(n))
        print("design", n)
    galerie()

if __name__ == "__main__":
    main()
