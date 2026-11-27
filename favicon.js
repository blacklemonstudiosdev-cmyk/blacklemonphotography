/* BlackLemon Photography favicons. Add <script src="favicon.js"></script> to index.html (keep favicon.svg, favicon.png and apple-touch-icon.png in the same folder). */
(function(){
  var s=document.currentScript,base=s&&s.src?s.src.replace(/[^\/]*$/,''):'';
  [['icon','image/svg+xml',null,'favicon.svg'],['icon','image/png','32x32','favicon.png'],['apple-touch-icon',null,'180x180','apple-touch-icon.png']].forEach(function(d){
    var l=document.createElement('link');l.rel=d[0];if(d[1])l.type=d[1];if(d[2])l.sizes=d[2];l.href=base+d[3];document.head.appendChild(l);
  });
})();
