/* Přepínač loga – JEN pro návrhy (v kroku 2 se nepoužije).
   Vymění obsah všech prvků s atributem data-logo-slot za vybrané logo z window.DDD_LOGA.
   Logo jde zvolit i adresou: design-1.html?logo=4 */
(function () {
  var loga = window.DDD_LOGA || {};
  var pocitadlo = 0;
  function vloz(n) {
    var svg = loga[n];
    if (!svg) return;
    document.querySelectorAll('[data-logo-slot]').forEach(function (slot) {
      pocitadlo++;
      // každé vložení dostane vlastní příponu id, aby se gradienty a vzory nepletly
      slot.innerHTML = svg.replace(/(l\d\d-[\w-]+)/g, '$1-p' + pocitadlo);
    });
    document.querySelectorAll('.prepinac-loga button[data-n]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-n') === String(n)));
    });
  }
  var css = '.prepinac-loga{position:fixed;left:8px;bottom:8px;z-index:9999;max-width:calc(100vw - 16px);box-sizing:border-box;'
    + 'background:#fff;color:#111;border:2px solid #111;border-radius:10px;padding:6px 8px;box-shadow:0 4px 16px rgba(0,0,0,.25);'
    + 'font:600 13px/1.2 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;display:flex;flex-wrap:wrap;align-items:center;gap:4px}'
    + '.prepinac-loga span{margin-right:4px}'
    + '.prepinac-loga button{font:inherit;min-width:30px;height:30px;border:1px solid #888;border-radius:6px;background:#f3f3f3;color:#111;cursor:pointer;padding:0 4px}'
    + '.prepinac-loga button[aria-pressed=true]{background:#111;color:#fff;border-color:#111}'
    + '.prepinac-loga .zavrit{background:transparent;border:0;margin-left:2px}'
    + '.prepinac-loga.sbaleno>*:not(.otevrit){display:none}.prepinac-loga .otevrit{display:none}.prepinac-loga.sbaleno .otevrit{display:inline-block}'
    + '@media print{.prepinac-loga{display:none}}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  var p = document.createElement('div');
  p.className = 'prepinac-loga'; p.setAttribute('role', 'group'); p.setAttribute('aria-label', 'Vyzkoušet logo');
  var h = '<span>Vyzkoušet logo:</span>';
  for (var i = 1; i <= 10; i++) h += '<button type="button" data-n="' + i + '" aria-pressed="false">' + i + '</button>';
  h += '<button type="button" class="zavrit" title="Skrýt panel" aria-label="Skrýt panel">✕</button>';
  h += '<button type="button" class="otevrit" title="Zobrazit přepínač loga">Logo</button>';
  p.innerHTML = h;
  p.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.classList.contains('zavrit')) { p.classList.add('sbaleno'); return; }
    if (b.classList.contains('otevrit')) { p.classList.remove('sbaleno'); return; }
    vloz(b.getAttribute('data-n'));
  });
  document.body.appendChild(p);
  var vychozi = document.body.getAttribute('data-vychozi-logo');
  var m = /[?&]logo=(\d+)/.exec(location.search);
  if (m && loga[+m[1]]) vloz(+m[1]);
  else if (vychozi) {
    document.querySelectorAll('.prepinac-loga button[data-n="' + (+vychozi) + '"]').forEach(function (b) { b.setAttribute('aria-pressed', 'true'); });
  }
})();
