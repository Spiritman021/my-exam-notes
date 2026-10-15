/* Makes a notes page work inside the hub (../index.html).
   Include in <head> of every notes page:
   <script src="../assets/embed.js"></script>
   Does nothing when the page is opened on its own. */
(function(){
  if (window.self === window.top) return;
  var root = document.documentElement;
  root.classList.add('embedded');

  // Hub already has prev/next + theme controls: hide the page's duplicates.
  var css = document.createElement('style');
  css.textContent =
    'html.embedded button.themer{display:none!important}' +
    'html.embedded nav.topnav.hub-dup{display:none!important}';
  document.head.appendChild(css);

  // Hide only the top chapter nav; keep the bottom one for "next chapter" at the end.
  document.addEventListener('DOMContentLoaded', function(){
    var navs = document.querySelectorAll('nav.topnav');
    if (navs.length > 1) navs[0].classList.add('hub-dup');
  });

  function send(msg){ try{ window.parent.postMessage(msg, '*'); }catch(e){} }

  // Route links to other notes pages through the hub so its URL + sidebar stay in sync.
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.target || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var url = a.href.split('#')[0];
    if (!/\.html$/.test(url) || url === location.href.split('#')[0]) return;
    e.preventDefault();
    send({ notesHub: 'nav', href: a.href });
  });

  window.addEventListener('message', function(e){
    var d = e.data || {};
    if (d.notesHub === 'theme' && d.theme) root.setAttribute('data-theme', d.theme);
  });

  send({ notesHub: 'loaded', href: location.href });
})();
