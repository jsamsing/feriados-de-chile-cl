(function(){
var F=__FERIADOS__, GA='__GA4__';
// fecha de hoy en Chile (YYYY-MM-DD) sin depender de la zona del visitante
function hoyCL(add){var d=new Date(Date.now()+(add||0)*864e5);return new Intl.DateTimeFormat('en-CA',{timeZone:'America/Santiago'}).format(d)}
function txt(iso){var d=new Date(iso+'T12:00:00Z');return new Intl.DateTimeFormat('es-CL',{timeZone:'UTC',weekday:'long',day:'numeric',month:'long',year:'numeric'}).format(d)}
function busca(iso){for(var i=0;i<F.length;i++)if(F[i][0]===iso)return F[i];return null}
function tick(){
var h=hoyCL(0),m=hoyCL(1),fh=busca(h),fm=busca(m);
var r=document.querySelector('[data-hoy-r]');
if(r){document.querySelector('[data-hoy-t]').textContent='¿Hoy '+txt(h)+' es feriado?';
r.textContent=fh?'Sí: '+fh[1]+(fh[3]?' (irrenunciable)':'')+'.':'No, hoy no es feriado en Chile.';
document.querySelector('[data-hoy]').classList.toggle('si',!!fh);
document.querySelector('[data-man]').textContent='Mañana: '+(fm?'sí es feriado ('+fm[1]+').':'no es feriado.');}
var p=F.filter(function(x){return x[0]>h})[0],s=document.querySelector('[data-prox]');
if(s&&p){s.querySelector('[data-pf-n]').textContent=p[1];s.querySelector('[data-pf-f]').textContent=txt(p[0]);
var t=Math.max(0,Math.floor((Date.parse(p[0]+(+p[0].slice(5,7)>=5&&+p[0].slice(5,7)<=8?'T04:00:00Z':'T03:00:00Z'))-Date.now())/1000)),dd=Math.floor(t/86400),hh=Math.floor(t%86400/3600),mm=Math.floor(t%3600/60),ss=t%60;
s.querySelector('[data-cd]').textContent=dd+' días, '+hh+' h '+mm+' min '+ss+' s';}
}
tick();setInterval(tick,1000);
window.ckShow=function(){document.getElementById('ck').hidden=false};
window.ckSet=function(v){try{localStorage.setItem('fc_ck',v?'g':'d')}catch(e){}document.getElementById('ck').hidden=true;if(v)ga()};
function ga(){if(!GA||location.hostname!=='feriados-de-chile.cl'||window.gtag)return;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA)}
var k=null;try{k=localStorage.getItem('fc_ck')}catch(e){}
if(k==='g')ga();else if(!k&&GA)setTimeout(ckShow,1500);
document.addEventListener('click',function(e){var a=e.target.closest('[data-ev]');if(a&&window.gtag)gtag('event',a.dataset.ev,{cta_label:a.dataset.label})});
})();
