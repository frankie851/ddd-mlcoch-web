"""Generátor log DDD Mlčoch (jen pro fázi návrhů).

Spuštění (potřebuje balíček fonttools):  python3 navrhy/nastroje/loga.py
Vytvoří navrhy/loga/logo-NN.svg (celé logo) a logo-NN-znacka.svg (samotná značka).
Šířka textu se měří podle skutečných písem v navrhy/pisma/, aby viewBox seděl.
Barvy textu jdou přes CSS proměnné --logo-ink a --logo-ink2 (tmavé pozadí je přepíše na světlé).
"""
import os
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PISMA = os.path.join(ROOT, "pisma")
OUT = os.path.join(ROOT, "loga")
_cache = {}

def tw(font, size, text, spacing=0.0):
    """Šířka textu v jednotkách viewBoxu."""
    if font not in _cache:
        f = TTFont(os.path.join(PISMA, font + ".woff"))
        _cache[font] = (f.getBestCmap(), f["hmtx"].metrics, f["head"].unitsPerEm)
    cmap, hmtx, upm = _cache[font]
    w = sum(hmtx[cmap.get(ord(c), ".notdef")][0] for c in text)
    return w * size / upm + spacing * size * (len(text) - 1)

INK = "fill:var(--logo-ink,#1c2420)"
INK2 = "fill:var(--logo-ink2,#4b5651)"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")

def text(x, y, s, fam, weight, size, style=INK, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-weight="{weight}" '
            f'font-size="{size}" style="{style}"{extra}>{esc(s)}</text>')

F = {
 "src": ("'Source Sans 3','DejaVu Sans',sans-serif", "SourceSans3_700Bold"),
 "src6": ("'Source Sans 3','DejaVu Sans',sans-serif", "SourceSans3_600SemiBold"),
 "plex": ("'IBM Plex Sans','DejaVu Sans',sans-serif", "IBMPlexSans_600SemiBold"),
 "mono": ("'IBM Plex Mono','DejaVu Sans Mono',monospace", "IBMPlexMono_500Medium"),
 "baloo": ("'Baloo 2','DejaVu Sans',sans-serif", "Baloo2_800ExtraBold"),
 "baloo7": ("'Baloo 2','DejaVu Sans',sans-serif", "Baloo2_700Bold"),
 "frau": ("'Fraunces','DejaVu Serif',serif", "Fraunces_800ExtraBold"),
 "bitter": ("'Bitter','DejaVu Serif',serif", "Bitter_700Bold"),
 "barc": ("'Barlow Condensed','DejaVu Sans Condensed',sans-serif", "BarlowCondensed_800ExtraBold"),
 "barc7": ("'Barlow Condensed','DejaVu Sans Condensed',sans-serif", "BarlowCondensed_700Bold"),
 "alfa": ("'Alfa Slab One','DejaVu Serif',serif", "AlfaSlabOne_400Regular"),
 "paci": ("'Pacifico','DejaVu Serif',cursive", "Pacifico_400Regular"),
 "man": ("'Manrope','DejaVu Sans',sans-serif", "Manrope_800ExtraBold"),
 "man7": ("'Manrope','DejaVu Sans',sans-serif", "Manrope_700Bold"),
 "space": ("'Space Grotesk','DejaVu Sans',sans-serif", "SpaceGrotesk_700Bold"),
}
W = {"SourceSans3_700Bold":700,"SourceSans3_600SemiBold":600,"IBMPlexSans_600SemiBold":600,"IBMPlexMono_500Medium":500,
     "Baloo2_800ExtraBold":800,"Baloo2_700Bold":700,"Fraunces_800ExtraBold":800,"Bitter_700Bold":700,
     "BarlowCondensed_800ExtraBold":800,"BarlowCondensed_700Bold":700,"AlfaSlabOne_400Regular":400,
     "Pacifico_400Regular":400,"Manrope_800ExtraBold":800,"Manrope_700Bold":700,"SpaceGrotesk_700Bold":700}

def t(key, x, y, s, size, style=INK, extra=""):
    fam, file = F[key]
    return text(x, y, s, fam, W[file], size, style, extra), tw(file, size, s)

def standard_word(n, name_key, slogan_key, slogan, acc, name_size=40, slogan_size=15, x0=116,
                  ddd_key=None, rest_key=None):
    """Klasické rozložení: DDD (akcent) + Mlčoch, pod tím slogan."""
    ddd_key = ddd_key or name_key
    rest_key = rest_key or name_key
    a, wa = t(ddd_key, x0, 58, "DDD", name_size, f"fill:{acc}")
    gap = name_size * 0.24
    b, wb = t(rest_key, x0 + wa + gap, 58, "Mlčoch", name_size)
    parts = [a, b]
    width = wa + gap + wb
    if slogan:
        c, wc = t(slogan_key, x0 + 1, 84, slogan, slogan_size, INK2)
        parts.append(c)
        width = max(width, wc)
    return "\n  ".join(parts), x0 + width + 4

# ---------------------------------------------------------------- značky (0–100)
MARKS = {}

MARKS[1] = """<clipPath id="l01-kruh"><circle cx="50" cy="50" r="48"/></clipPath>
  <circle cx="50" cy="50" r="48" fill="#1f7a4d"/>
  <g clip-path="url(#l01-kruh)">
    <path d="M23 41q8 8 16 0M61 41q8 8 16 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="50" cy="67" rx="18" ry="7.5" fill="#f28b7f"/>
    <path d="M33 67h34" stroke="#b9473d" stroke-width="2.4" stroke-linecap="round"/>
    <ellipse cx="50" cy="104" rx="23" ry="16" fill="#ffd6ad" stroke="#d99a68" stroke-width="2"/>
    <rect x="42.5" y="45" width="15" height="50" rx="7.5" fill="#ffd6ad" stroke="#d99a68" stroke-width="2"/>
    <rect x="45.3" y="48" width="9.4" height="10" rx="4" fill="#fff1e0"/>
  </g>"""

MARKS[2] = """<rect x="2" y="2" width="96" height="96" rx="24" fill="#0f766e"/>
  <path d="M11 50 19 22 28 78 37 30 46 68 54 40 61 58 67 47 72 50H86" fill="none" stroke="#fff" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="87" cy="50" r="5.5" fill="#7ff0dd"/>"""

MARKS[3] = """<circle cx="50" cy="50" r="48" fill="#f2b705"/>
  <circle cx="29" cy="27" r="14" fill="#9aa1aa"/><circle cx="71" cy="27" r="14" fill="#9aa1aa"/>
  <circle cx="29" cy="27" r="8" fill="#f5a7b8"/><circle cx="71" cy="27" r="8" fill="#f5a7b8"/>
  <ellipse cx="50" cy="46" rx="25" ry="21" fill="#b3b9c1"/>
  <circle cx="41" cy="42" r="3.6" fill="#1e2328"/><circle cx="59" cy="42" r="3.6" fill="#1e2328"/>
  <circle cx="42.2" cy="40.8" r="1.2" fill="#fff"/><circle cx="60.2" cy="40.8" r="1.2" fill="#fff"/>
  <ellipse cx="50" cy="52" rx="4" ry="3" fill="#e9798f"/>
  <path d="M44 54 28 51M44 57 29 60M56 54 72 51M56 57 71 60" stroke="#5b6168" stroke-width="1.6" stroke-linecap="round"/>
  <rect x="21" y="60" width="58" height="28" rx="5" fill="#fff" stroke="#1e2328" stroke-width="3"/>
  <circle cx="25" cy="62" r="5.5" fill="#b3b9c1" stroke="#1e2328" stroke-width="1.5"/><circle cx="75" cy="62" r="5.5" fill="#b3b9c1" stroke="#1e2328" stroke-width="1.5"/>
  <text x="50" y="82" text-anchor="middle" font-family="'Baloo 2','DejaVu Sans',sans-serif" font-weight="800" font-size="19" fill="#1e2328">PSST</text>"""

MARKS[4] = """<circle cx="50" cy="50" r="47" fill="#2c3e8f" stroke="#f6c445" stroke-width="3"/>
  <circle cx="74" cy="22" r="2" fill="#f6c445"/><circle cx="86" cy="36" r="1.5" fill="#f6c445"/>
  <path d="M14 80q36-10 72 0" fill="none" stroke="#5aa845" stroke-width="4" stroke-linecap="round"/>
  <path d="M40 63 30 42 20 73" fill="none" stroke="#4f9a3a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
  <ellipse cx="45" cy="64" rx="22" ry="10.5" fill="#7cc35b" transform="rotate(-6 45 64)"/>
  <path d="M28 63q16-7 33-3" fill="none" stroke="#4f9a3a" stroke-width="2" stroke-linecap="round"/>
  <circle cx="66" cy="58" r="9" fill="#7cc35b"/><circle cx="75" cy="52" r="8.5" fill="#8fd16c"/>
  <path d="M74 52q3 3 6 0" fill="none" stroke="#1e2a4f" stroke-width="2" stroke-linecap="round"/>
  <path d="M79 45q14-14 0-27M76 44q4-17-10-25" fill="none" stroke="#8fd16c" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M52 72 50 78M62 66 64 77M70 64 75 74" stroke="#4f9a3a" stroke-width="3" stroke-linecap="round"/>
  <text x="20" y="40" font-family="'Fraunces','DejaVu Serif',serif" font-weight="800" font-size="14" fill="#f6c445">z</text>
  <text x="29" y="30" font-family="'Fraunces','DejaVu Serif',serif" font-weight="800" font-size="19" fill="#f6c445">z</text>"""

MARKS[5] = """<circle cx="50" cy="50" r="48" fill="#6b7a34"/>
  <path d="M10 80H90" stroke="#a9b56a" stroke-width="3" stroke-linecap="round"/>
  <path d="M30 68q-15 5-18-8q-2-9 6-11" fill="none" stroke="#d9c7ab" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M41 76v4M55 76v4" stroke="#d9c7ab" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="47" cy="65" rx="19" ry="13" fill="#d9c7ab"/>
  <path d="M59 47Q72 44 84 59Q73 66 58 64Z" fill="#d9c7ab"/>
  <circle cx="62" cy="46" r="8" fill="#d9c7ab"/><circle cx="62" cy="46" r="4.5" fill="#efa0a8"/>
  <circle cx="71" cy="54" r="2.3" fill="#2a2a20"/><circle cx="84" cy="59" r="2.6" fill="#d76a7c"/>
  <path d="M62 60v-5h12v5" fill="none" stroke="#5a3418" stroke-width="2.6" stroke-linejoin="round"/>
  <rect x="56" y="59" width="24" height="17" rx="3" fill="#a0582a" stroke="#5a3418" stroke-width="2"/>
  <path d="M56 66h24" stroke="#5a3418" stroke-width="1.6"/><rect x="65" y="64" width="6" height="4" rx="1" fill="#f2c14e"/>
  <circle cx="66" cy="57" r="3.5" fill="#cdb898"/>
  <path d="M8 58h7M5 66h8M9 74h6" stroke="#a9b56a" stroke-width="2.4" stroke-linecap="round"/>"""

MARKS[6] = """<circle cx="50" cy="50" r="47" fill="#f6ead2" stroke="#c8322b" stroke-width="6"/>
  <circle cx="50" cy="50" r="39" fill="none" stroke="#2b2622" stroke-width="1.5" stroke-dasharray="3 3"/>
  <circle cx="29" cy="59" r="4.5" fill="#f1bf92"/><circle cx="71" cy="59" r="4.5" fill="#f1bf92"/>
  <circle cx="50" cy="59" r="21" fill="#f5cba3"/>
  <path d="M27 53Q27 27 50 27Q73 27 73 53Z" fill="#c8322b"/>
  <path d="M27 53H86Q88 59 80 59H27Z" fill="#9e2420"/>
  <circle cx="50" cy="27" r="3" fill="#9e2420"/>
  <text x="50" y="47" text-anchor="middle" font-family="'Alfa Slab One','DejaVu Serif',serif" font-size="13" fill="#f6ead2">M</text>
  <circle cx="43" cy="62" r="2.6" fill="#2b2622"/>
  <path d="M54 62q3.5-3 7 0" fill="none" stroke="#2b2622" stroke-width="2.4" stroke-linecap="round"/>
  <path d="M37 71q6.5-6 13-2q6.5-4 13 2q-6.5 3.5-13 0q-6.5 3.5-13 0Z" fill="#5a3a26"/>
  <path d="M44 75q6 4 12 0" fill="none" stroke="#2b2622" stroke-width="2" stroke-linecap="round"/>"""

MARKS[7] = """<rect x="3" y="3" width="94" height="94" rx="14" fill="#ffcc00" stroke="#1a1a1a" stroke-width="5"/>
  <path d="M73 86 79 13" stroke="#1a1a1a" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M79 15q8-4 15 1v17q-7-5-16-1Z" fill="#fff" stroke="#1a1a1a" stroke-width="2.4" stroke-linejoin="round"/>
  <path d="M28 54 15 48M27 64 13 66M30 74 18 84M56 54 69 48M57 66 70 70M54 76 63 86" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/>
  <path d="M57 47 75 33" stroke="#1a1a1a" stroke-width="3.2" stroke-linecap="round"/>
  <ellipse cx="42" cy="65" rx="16" ry="20" fill="#8a5530" stroke="#1a1a1a" stroke-width="2.5"/>
  <path d="M42 47v37" stroke="#1a1a1a" stroke-width="2"/>
  <circle cx="42" cy="39" r="11" fill="#6b3f22" stroke="#1a1a1a" stroke-width="2.5"/>
  <path d="M37 30q-4-14-14-15M47 30q4-14 14-16" fill="none" stroke="#1a1a1a" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="38" cy="38" r="4" fill="#fff"/><circle cx="47" cy="38" r="4" fill="#fff"/>
  <circle cx="39" cy="37" r="2" fill="#1a1a1a"/><circle cx="48" cy="37" r="2" fill="#1a1a1a"/>
  <path d="M38 44q4 3 8 0" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>"""

def foot(x, y, rot, fill, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" fill="{fill}">'
            '<path d="M-9-9h6a9 9 0 0 1 0 18h-6z"/>'
            '<circle cx="11" cy="-10" r="3"/><circle cx="14.5" cy="-3.6" r="3"/>'
            '<circle cx="14.5" cy="3.6" r="3"/><circle cx="11" cy="10" r="3"/></g>')

MARKS[8] = ('<circle cx="50" cy="50" r="48" fill="#e2603f"/>\n  '
            + foot(25, 69, -45, "#fff", 0.82) + foot(51, 57, -45, "#fff", 0.82) + foot(57, 29, -45, "#fff", 0.82))

def drop(cx, cy, s, fill):
    return (f'<path transform="translate({cx} {cy}) scale({s})" fill="{fill}" '
            'd="M0-22C5-13 15-3 15 7A15 15 0 0 1-15 7C-15-3-5-13 0-22Z"/>')

MARKS[9] = (drop(19, 60, 0.95, "#0ea5e9") + "\n  " + drop(81, 60, 0.95, "#14b8a6") + "\n  "
            + drop(50, 50, 1.6, "#10a35a") + "\n  "
            + '<path d="M40 61l7 7 13-14" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>')

MARKS[10] = """<rect x="2" y="2" width="96" height="96" rx="22" fill="#ffe3cc"/>
  <path d="M27 76q-13 2-13 11q0 6 8 5" fill="none" stroke="#2d3150" stroke-width="3.6" stroke-linecap="round"/>
  <circle cx="51" cy="25" r="10" fill="#2d3150"/><circle cx="51" cy="25" r="5.5" fill="#f39aa8"/>
  <path fill="#2d3150" fill-rule="evenodd" d="M26 24h22a27 27 0 0 1 0 54H26ZM37 35v32h11a16 16 0 0 0 0-32Z"/>
  <circle cx="64" cy="38" r="3.2" fill="#fff"/>
  <circle cx="75.5" cy="51" r="4" fill="#f06b84"/>
  <path d="M76 55l13 3M76 58l12 7" stroke="#2d3150" stroke-width="1.6" stroke-linecap="round"/>"""

# ---------------------------------------------------------------- loga
IDEAS = {
 1: dict(name="Prst na ústech", slogan="Po nás je ticho.", key="src", skey="src6", acc="#23955c"),
 2: dict(name="Zmlklá vlna", slogan="Škůdci zmlknou.", key="plex", skey="mono", acc="#14b8a6"),
 3: dict(name="Myš s cedulkou PSST", slogan="Psst… už jsou pryč.", key="baloo", skey="baloo7", acc="#d99a00"),
 4: dict(name="Ztichlý cvrček", slogan="I cvrček ztichl.", key="frau", skey="src6", acc="#4565d6"),
 5: dict(name="Stěhování škůdců", slogan="ŠKŮDCI SE STĚHUJÍ.", key="bitter", skey="barc7", acc="#7d8f2e"),
 6: dict(name="Odznak s hubitelem", slogan="DERATIZACE · DEZINSEKCE · DEZINFEKCE", key="alfa", skey="barc7", acc="#c8322b"),
 7: dict(name="Brouk s bílou vlajkou", slogan="ŠKŮDCI KAPITULUJÍ.", key="barc", skey="barc7", acc="#e0a800"),
 8: dict(name="DDD jako tři stopy", slogan="Stopy vedou pryč.", key="bitter", skey="src6", acc="#e2603f"),
 9: dict(name="Tři kapky", slogan="Čisto. Ticho. Hotovo.", key="man", skey="man7", acc="#10a35a"),
 10: dict(name="Písmeno D jako myš", slogan="Myš? Jen v logu.", key="space", skey="space", acc="#5a62c9"),
}

def wordmark(n):
    i = IDEAS[n]
    if n == 6:
        a, wa = t("alfa", 116, 54, "DDD", 36, "fill:#c8322b")
        b, wb = t("paci", 116 + wa + 10, 58, "Mlčoch", 38)
        c, wc = t("barc7", 117, 86, i["slogan"], 13.5, INK2, ' letter-spacing="0.6"')
        return "\n  ".join([a, b, c]), 116 + max(wa + 10 + wb, wc + 0.6 * 30) + 4
    if n == 7:
        a, wa = t("barc", 116, 58, "DDD", 46, "fill:#e0a800")
        b, wb = t("barc", 116 + wa + 10, 58, "Mlčoch", 46)
        c, wc = t("barc7", 117, 86, i["slogan"], 16, INK2, ' letter-spacing="1.2"')
        width = max(wa + 10 + wb, wc + 1.2 * 18)
        stripes = (f'<rect x="116" y="66" width="{width:.1f}" height="6" fill="url(#l07-pruhy)"/>')
        return "\n  ".join([a, b, stripes, c]), 116 + width + 4
    size = 42 if n in (3,) else 40
    return standard_word(n, i["key"], i["skey"], i["slogan"], i["acc"], name_size=size)

def svg(n, viewbox, body, label):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<?xml-stylesheet type="text/css" href="../spolecne/pisma.css"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" aria-label="{label}">\n'
            f'  {body}\n</svg>\n')

def main():
    os.makedirs(OUT, exist_ok=True)
    for n in range(1, 11):
        mark = MARKS[n]
        defs = ""
        if n == 7:
            defs = ('<defs><pattern id="l07-pruhy" width="12" height="6" patternUnits="userSpaceOnUse" '
                    'patternTransform="skewX(-45)"><rect width="12" height="6" fill="#ffcc00"/>'
                    '<rect width="6" height="6" fill="#1a1a1a"/></pattern></defs>\n  ')
        words, width = wordmark(n)
        full = f'{defs}<g class="znacka">\n  {mark}\n  </g>\n  {words}'
        with open(os.path.join(OUT, f"logo-{n:02d}.svg"), "w", encoding="utf-8") as fh:
            fh.write(svg(n, f"0 0 {width:.0f} 100", full, "DDD Mlčoch – logo"))
        with open(os.path.join(OUT, f"logo-{n:02d}-znacka.svg"), "w", encoding="utf-8") as fh:
            fh.write(svg(n, "0 0 100 100", mark, "DDD Mlčoch – značka"))
        print(n, IDEAS[n]["name"], f"{width:.0f}x100")

if __name__ == "__main__":
    main()
