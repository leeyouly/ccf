(function(){var h={},mt={},c={id:"69684b1f0a44d5d36f504b59a0385dd9",dm:["ccf.com.cn"],js:"tongji.baidu.com/hm-web/js/",etrk:[],icon:'/hmt/icon/21|gif|20|20',ctrk:false,align:-1,nv:-1,vdur:1800000,age:31536000000,rec:0,rp:[],trust:0,vcard:0,qiao:0,lxb:0,conv:0,med:0,cvcc:'',cvcf:[],apps:''};var q=void 0,r=!0,s=null,w=!1;mt.j={};mt.j.T=/msie (\d+\.\d+)/i.test(navigator.userAgent);mt.j.Aa=/msie (\d+\.\d+)/i.test(navigator.userAgent)?document.documentMode||+RegExp.$1:q;mt.j.cookieEnabled=navigator.cookieEnabled;mt.j.javaEnabled=navigator.javaEnabled();mt.j.language=navigator.language||navigator.browserLanguage||navigator.systemLanguage||navigator.userLanguage||"";mt.j.Fa=(window.screen.width||0)+"x"+(window.screen.height||0);mt.j.colorDepth=window.screen.colorDepth||0;mt.cookie={};
mt.cookie.set=function(a,d,e){var b;e.I&&(b=new Date,b.setTime(b.getTime()+e.I));document.cookie=a+"="+d+(e.domain?"; domain="+e.domain:"")+(e.path?"; path="+e.path:"")+(b?"; expires="+b.toGMTString():"")+(e.Za?"; secure":"")};mt.cookie.get=function(a){return(a=RegExp("(^| )"+a+"=([^;]*)(;|$)").exec(document.cookie))?a[2]:s};mt.s={};mt.s.la=function(a){return document.getElementById(a)};mt.s.Ta=function(a,d){for(d=d.toUpperCase();(a=a.parentNode)&&1==a.nodeType;)if(a.tagName==d)return a;return s};
(mt.s.Y=function(){function a(){if(!a.C){a.C=r;for(var d=0,f=b.length;d<f;d++)b[d]()}}function d(){try{document.documentElement.doScroll("left")}catch(b){setTimeout(d,1);return}a()}var e=w,b=[],f;document.addEventListener?f=function(){document.removeEventListener("DOMContentLoaded",f,w);a()}:document.attachEvent&&(f=function(){"complete"===document.readyState&&(document.detachEvent("onreadystatechange",f),a())});(function(){if(!e)if(e=r,"complete"===document.readyState)a.C=r;else if(document.addEventListener)document.addEventListener("DOMContentLoaded",
f,w),window.addEventListener("load",a,w);else if(document.attachEvent){document.attachEvent("onreadystatechange",f);window.attachEvent("onload",a);var b=w;try{b=window.frameElement==s}catch(n){}document.documentElement.doScroll&&b&&d()}})();return function(d){a.C?d():b.push(d)}}()).C=w;mt.event={};mt.event.c=function(a,d,e){a.attachEvent?a.attachEvent("on"+d,function(b){e.call(a,b)}):a.addEventListener&&a.addEventListener(d,e,w)};
mt.event.preventDefault=function(a){a.preventDefault?a.preventDefault():a.returnValue=w};mt.l={};mt.l.parse=function(){return(new Function('return (" + source + ")'))()};
mt.l.stringify=function(){function a(a){/["\\\x00-\x1f]/.test(a)&&(a=a.replace(/["\\\x00-\x1f]/g,function(a){var b=e[a];if(b)return b;b=a.charCodeAt();return"\\u00"+Math.floor(b/16).toString(16)+(b%16).toString(16)}));return'"'+a+'"'}function d(a){return 10>a?"0"+a:a}var e={"\b":"\\b","\t":"\\t","\n":"\\n","\f":"\\f","\r":"\\r",'"':'\\"',"\\":"\\\\"};return function(b){switch(typeof b){case "undefined":return"undefined";case "number":return isFinite(b)?String(b):"null";case "string":return a(b);case "boolean":return String(b);
default:if(b===s)return"null";if(b instanceof Array){var f=["["],e=b.length,n,g,m;for(g=0;g<e;g++)switch(m=b[g],typeof m){case "undefined":case "function":case "unknown":break;default:n&&f.push(","),f.push(mt.l.stringify(m)),n=1}f.push("]");return f.join("")}if(b instanceof Date)return'"'+b.getFullYear()+"-"+d(b.getMonth()+1)+"-"+d(b.getDate())+"T"+d(b.getHours())+":"+d(b.getMinutes())+":"+d(b.getSeconds())+'"';n=["{"];g=mt.l.stringify;for(e in b)if(Object.prototype.hasOwnProperty.call(b,e))switch(m=
b[e],typeof m){case "undefined":case "unknown":case "function":break;default:f&&n.push(","),f=1,n.push(g(e)+":"+g(m))}n.push("}");return n.join("")}}}();mt.lang={};mt.lang.d=function(a,d){return"[object "+d+"]"==={}.toString.call(a)};mt.lang.Wa=function(a){return mt.lang.d(a,"Number")&&isFinite(a)};mt.lang.Ya=function(a){return mt.lang.d(a,"String")};mt.localStorage={};
mt.localStorage.G=function(){if(!mt.localStorage.g)try{mt.localStorage.g=document.createElement("input"),mt.localStorage.g.type="hidden",mt.localStorage.g.style.display="none",mt.localStorage.g.addBehavior("#default#userData"),document.getElementsByTagName("head")[0].appendChild(mt.localStorage.g)}catch(a){return w}return r};
mt.localStorage.set=function(a,d,e){var b=new Date;b.setTime(b.getTime()+e||31536E6);try{window.localStorage?(d=b.getTime()+"|"+d,window.localStorage.setItem(a,d)):mt.localStorage.G()&&(mt.localStorage.g.expires=b.toUTCString(),mt.localStorage.g.load(document.location.hostname),mt.localStorage.g.setAttribute(a,d),mt.localStorage.g.save(document.location.hostname))}catch(f){}};
mt.localStorage.get=function(a){if(window.localStorage){if(a=window.localStorage.getItem(a)){var d=a.indexOf("|"),e=a.substring(0,d)-0;if(e&&e>(new Date).getTime())return a.substring(d+1)}}else if(mt.localStorage.G())try{return mt.localStorage.g.load(document.location.hostname),mt.localStorage.g.getAttribute(a)}catch(b){}return s};
mt.localStorage.remove=function(a){if(window.localStorage)window.localStorage.removeItem(a);else if(mt.localStorage.G())try{mt.localStorage.g.load(document.location.hostname),mt.localStorage.g.removeAttribute(a),mt.localStorage.g.save(document.location.hostname)}catch(d){}};mt.sessionStorage={};mt.sessionStorage.set=function(a,d){if(window.sessionStorage)try{window.sessionStorage.setItem(a,d)}catch(e){}};
mt.sessionStorage.get=function(a){return window.sessionStorage?window.sessionStorage.getItem(a):s};mt.sessionStorage.remove=function(a){window.sessionStorage&&window.sessionStorage.removeItem(a)};mt.P={};mt.P.log=function(a,d){var e=new Image,b="mini_tangram_log_"+Math.floor(2147483648*Math.random()).toString(36);window[b]=e;e.onload=e.onerror=e.onabort=function(){e.onload=e.onerror=e.onabort=s;e=window[b]=s;d&&d(a)};e.src=a};mt.F={};
mt.F.sa=function(){var a="";if(navigator.plugins&&navigator.mimeTypes.length){var d=navigator.plugins["Shockwave Flash"];d&&d.description&&(a=d.description.replace(/^.*\s+(\S+)\s+\S+$/,"$1"))}else if(window.ActiveXObject)try{if(d=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"))(a=d.GetVariable("$version"))&&(a=a.replace(/^.*\s+(\d+),(\d+).*$/,"$1.$2"))}catch(e){}return a};
mt.F.ea=function(a,d,e,b,f){return'<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" id="'+a+'" width="'+e+'" height="'+b+'"><param name="movie" value="'+d+'" /><param name="flashvars" value="'+(f||"")+'" /><param name="allowscriptaccess" value="always" /><embed type="application/x-shockwave-flash" name="'+a+'" width="'+e+'" height="'+b+'" src="'+d+'" flashvars="'+(f||"")+'" allowscriptaccess="always" /></object>'};mt.url={};
mt.url.k=function(a,d){var e=a.match(RegExp("(^|&|\\?|#)("+d+")=([^&#]*)(&|$|#)",""));return e?e[3]:s};mt.url.Va=function(a){return(a=a.match(/^(https?:)\/\//))?a[1]:s};mt.url.oa=function(a){return(a=a.match(/^(https?:\/\/)?([^\/\?#]*)/))?a[2].replace(/.*@/,""):s};mt.url.R=function(a){return(a=mt.url.oa(a))?a.replace(/:\d+$/,""):a};mt.url.Ua=function(a){return(a=a.match(/^(https?:\/\/)?[^\/]*(.*)/))?a[2].replace(/[\?#].*/,"").replace(/^$/,"/"):s};
h.r={za:"http://tongji.baidu.com/hm-web/welcome/ico",X:"hm.baidu.com/hm.gif",ba:"baidu.com",wa:"hmmd",xa:"hmpl",va:"hmkw",ta:"hmci",ya:"hmsr",ua:"hmcu",p:0,m:Math.round(+new Date/1E3),protocol:"https:"===document.location.protocol?"https:":"http:",Xa:0,Pa:6E5,Qa:10,Ra:1024,Oa:1,M:2147483647,Z:"cc cf ci ck cl cm cp cu cw ds ep et fl ja ln lo lt nv rnd si st su v cv lv api u tt".split(" ")};
(function(){var a={o:{},c:function(a,e){this.o[a]=this.o[a]||[];this.o[a].push(e)},z:function(a,e){this.o[a]=this.o[a]||[];for(var b=this.o[a].length,f=0;f<b;f++)this.o[a][f](e)}};return h.A=a})();
(function(){function a(a,b){var f=document.createElement("script");f.charset="utf-8";d.d(b,"Function")&&(f.readyState?f.onreadystatechange=function(){if("loaded"===f.readyState||"complete"===f.readyState)f.onreadystatechange=s,b()}:f.onload=function(){b()});f.src=a;var l=document.getElementsByTagName("script")[0];l.parentNode.insertBefore(f,l)}var d=mt.lang;return h.load=a})();
(function(){var a=h.r,d=mt.F,e={init:function(){if(""!==c.icon){var b;b=c.icon.split("|");var f=a.za+"?s="+c.id,e=("http:"==a.protocol?"http://eiv":"https://bs")+".baidu.com"+b[0]+"."+b[1];switch(b[1]){case "swf":b=d.ea("HolmesIcon"+a.m,e,b[2],b[3],"s="+f);break;case "gif":b='<a href="'+f+'" target="_blank"><img border="0" src="'+e+'" width="'+b[2]+'" height="'+b[3]+'"></a>';break;default:b='<a href="'+f+'" target="_blank">'+b[0]+"</a>"}document.write(b)}}};h.A.c("pv-b",e.init);return e})();
(function(){function a(){return function(){h.b.a.nv=0;h.b.a.st=4;h.b.a.et=3;h.b.a.ep=h.H.qa()+","+h.H.na();h.b.i()}}function d(){clearTimeout(y);var a;x&&(a="visible"==document[x]);z&&(a=!document[z]);g="undefined"==typeof a?r:a;if((!n||!m)&&g&&k)u=r,p=+new Date;else if(n&&m&&(!g||!k))u=w,t+=+new Date-p;n=g;m=k;y=setTimeout(d,100)}function e(a){var p=document,m="";if(a in p)m=a;else for(var b=["webkit","ms","moz","o"],d=0;d<b.length;d++){var f=b[d]+a.charAt(0).toUpperCase()+a.slice(1);if(f in p){m=
f;break}}return m}function b(a){if(!("focus"==a.type||"blur"==a.type)||!(a.target&&a.target!=window))k="focus"==a.type||"focusin"==a.type?r:w,d()}var f=mt.event,l=h.A,n=r,g=r,m=r,k=r,v=+new Date,p=v,t=0,u=r,x=e("visibilityState"),z=e("hidden"),y;d();(function(){var a=x.replace(/[vV]isibilityState/,"visibilitychange");f.c(document,a,d);f.c(window,"pageshow",d);f.c(window,"pagehide",d);"object"==typeof document.onfocusin?(f.c(document,"focusin",b),f.c(document,"focusout",b)):(f.c(window,"focus",b),
f.c(window,"blur",b))})();h.H={qa:function(){return+new Date-v},na:function(){return u?+new Date-p+t:t}};l.c("pv-b",function(){f.c(window,"unload",a())});return h.H})();
(function(){var a=mt.lang,d=h.r,e=h.load,b={Ba:function(b){if((window._dxt===q||a.d(window._dxt,"Array"))&&"undefined"!==typeof h.b){var l=h.b.J();e([d.protocol,"//datax.baidu.com/x.js?si=",c.id,"&dm=",encodeURIComponent(l)].join(""),b)}},Ma:function(b){if(a.d(b,"String")||a.d(b,"Number"))window._dxt=window._dxt||[],window._dxt.push(["_setUserId",b])}};return h.fa=b})();
(function(){function a(m){for(var b in m)if({}.hasOwnProperty.call(m,b)){var d=m[b];e.d(d,"Object")||e.d(d,"Array")?a(d):m[b]=String(d)}}function d(a){return a.replace?a.replace(/'/g,"'0").replace(/\*/g,"'1").replace(/!/g,"'2"):a}var e=mt.lang,b=mt.l,f=h.r,l=h.A,n=h.fa,g={w:[],D:0,V:w,init:function(){g.e=0;l.c("pv-b",function(){g.ga();g.ia()});l.c("pv-d",g.ka);l.c("stag-b",function(){h.b.a.api=g.e||g.D?g.e+"_"+g.D:""});l.c("stag-d",function(){h.b.a.api=0;g.e=0;g.D=0})},ga:function(){var a=window._hmt||
[];if(!a||e.d(a,"Array"))window._hmt={id:c.id,cmd:{},push:function(){for(var a=window._hmt,b=0;b<arguments.length;b++){var p=arguments[b];e.d(p,"Array")&&(a.cmd[a.id].push(p),"_setAccount"===p[0]&&(1<p.length&&/^[0-9a-f]{32}$/.test(p[1]))&&(p=p[1],a.id=p,a.cmd[p]=a.cmd[p]||[]))}}},window._hmt.cmd[c.id]=[],window._hmt.push.apply(window._hmt,a)},ia:function(){var a=window._hmt;if(a&&a.cmd&&a.cmd[c.id])for(var b=a.cmd[c.id],d=/^_track(Event|MobConv|Order|RTEvent)$/,p=0,f=b.length;p<f;p++){var e=b[p];
d.test(e[0])?g.w.push(e):g.N(e)}a.cmd[c.id]={push:g.N}},ka:function(){if(0<g.w.length)for(var a=0,b=g.w.length;a<b;a++)g.N(g.w[a]);g.w=s},N:function(a){var b=a[0];if(g.hasOwnProperty(b)&&e.d(g[b],"Function"))g[b](a)},_setAccount:function(a){1<a.length&&/^[0-9a-f]{32}$/.test(a[1])&&(g.e|=1)},_setAutoPageview:function(a){if(1<a.length&&(a=a[1],w===a||r===a))g.e|=2,h.b.S=a},_trackPageview:function(a){if(1<a.length&&a[1].charAt&&"/"===a[1].charAt(0)){g.e|=4;h.b.a.et=0;h.b.a.ep="";h.b.K?(h.b.a.nv=0,h.b.a.st=
4):h.b.K=r;var b=h.b.a.u,d=h.b.a.su;h.b.a.u=f.protocol+"//"+document.location.host+a[1];g.V||(h.b.a.su=document.location.href);h.b.i();h.b.a.u=b;h.b.a.su=d}},_trackEvent:function(a){2<a.length&&(g.e|=8,h.b.a.nv=0,h.b.a.st=4,h.b.a.et=4,h.b.a.ep=d(a[1])+"*"+d(a[2])+(a[3]?"*"+d(a[3]):"")+(a[4]?"*"+d(a[4]):""),h.b.i())},_setCustomVar:function(a){if(!(4>a.length)){var b=a[1],f=a[4]||3;if(0<b&&6>b&&0<f&&4>f){g.D++;for(var p=(h.b.a.cv||"*").split("!"),e=p.length;e<b-1;e++)p.push("*");p[b-1]=f+"*"+d(a[2])+
"*"+d(a[3]);h.b.a.cv=p.join("!");a=h.b.a.cv.replace(/[^1](\*[^!]*){2}/g,"*").replace(/((^|!)\*)+$/g,"");""!==a?h.b.setData("Hm_cv_"+c.id,encodeURIComponent(a),c.age):h.b.Ea("Hm_cv_"+c.id)}}},_setReferrerOverride:function(a){1<a.length&&(h.b.a.su=a[1].charAt&&"/"===a[1].charAt(0)?f.protocol+"//"+window.location.host+a[1]:a[1],g.V=r)},_trackOrder:function(d){d=d[1];e.d(d,"Object")&&(a(d),g.e|=16,h.b.a.nv=0,h.b.a.st=4,h.b.a.et=94,h.b.a.ep=b.stringify(d),h.b.i())},_trackMobConv:function(a){if(a={webim:1,
tel:2,map:3,sms:4,callback:5,share:6}[a[1]])g.e|=32,h.b.a.et=93,h.b.a.ep=a,h.b.i()},_trackRTPageview:function(d){d=d[1];e.d(d,"Object")&&(a(d),d=b.stringify(d),512>=encodeURIComponent(d).length&&(g.e|=64,h.b.a.rt=d))},_trackRTEvent:function(d){d=d[1];if(e.d(d,"Object")){a(d);d=encodeURIComponent(b.stringify(d));var k=function(a){var b=h.b.a.rt;g.e|=128;h.b.a.et=90;h.b.a.rt=a;h.b.i();h.b.a.rt=b},l=d.length;if(900>=l)k.call(this,d);else for(var l=Math.ceil(l/900),p="block|"+Math.round(Math.random()*
f.M).toString(16)+"|"+l+"|",t=[],u=0;u<l;u++)t.push(u),t.push(d.substring(900*u,900*u+900)),k.call(this,p+t.join("|")),t=[]}},_setUserId:function(a){a=a[1];n.Ba();n.Ma(a)}};g.init();h.ca=g;return h.ca})();
(function(){function a(){"undefined"===typeof window["_bdhm_loaded_"+c.id]&&(window["_bdhm_loaded_"+c.id]=r,this.a={},this.S=r,this.K=w,this.init())}var d=mt.url,e=mt.P,b=mt.F,f=mt.lang,l=mt.cookie,n=mt.j,g=mt.localStorage,m=mt.sessionStorage,k=h.r,v=h.A;a.prototype={L:function(a,b){a="."+a.replace(/:\d+/,"");b="."+b.replace(/:\d+/,"");var d=a.indexOf(b);return-1<d&&d+b.length===a.length},W:function(a,b){a=a.replace(/^https?:\/\//,"");return 0===a.indexOf(b)},B:function(a){for(var b=0;b<c.dm.length;b++)if(-1<
c.dm[b].indexOf("/")){if(this.W(a,c.dm[b]))return r}else{var f=d.R(a);if(f&&this.L(f,c.dm[b]))return r}return w},J:function(){for(var a=document.location.hostname,b=0,d=c.dm.length;b<d;b++)if(this.L(a,c.dm[b]))return c.dm[b].replace(/(:\d+)?[\/\?#].*/,"");return a},Q:function(){for(var a=0,b=c.dm.length;a<b;a++){var d=c.dm[a];if(-1<d.indexOf("/")&&this.W(document.location.href,d))return d.replace(/^[^\/]+(\/.*)/,"$1")+"/"}return"/"},ra:function(){if(!document.referrer)return k.m-k.p>c.vdur?1:4;var a=
w;this.B(document.referrer)&&this.B(document.location.href)?a=r:(a=d.R(document.referrer),a=this.L(a||"",document.location.hostname));return a?k.m-k.p>c.vdur?1:4:3},getData:function(a){try{return l.get(a)||m.get(a)||g.get(a)}catch(b){}},setData:function(a,b,d){try{l.set(a,b,{domain:this.J(),path:this.Q(),I:d}),d?g.set(a,b,d):m.set(a,b)}catch(f){}},Ea:function(a){try{l.set(a,"",{domain:this.J(),path:this.Q(),I:-1}),m.remove(a),g.remove(a)}catch(b){}},Ka:function(){var a,b,d,f,e;k.p=this.getData("Hm_lpvt_"+
c.id)||0;13===k.p.length&&(k.p=Math.round(k.p/1E3));b=this.ra();a=4!==b?1:0;if(d=this.getData("Hm_lvt_"+c.id)){f=d.split(",");for(e=f.length-1;0<=e;e--)13===f[e].length&&(f[e]=""+Math.round(f[e]/1E3));for(;2592E3<k.m-f[0];)f.shift();e=4>f.length?2:3;for(1===a&&f.push(k.m);4<f.length;)f.shift();d=f.join(",");f=f[f.length-1]}else d=k.m,f="",e=1;this.setData("Hm_lvt_"+c.id,d,c.age);this.setData("Hm_lpvt_"+c.id,k.m);d=k.m===this.getData("Hm_lpvt_"+c.id)?"1":"0";if(0===c.nv&&this.B(document.location.href)&&
(""===document.referrer||this.B(document.referrer)))a=0,b=4;this.a.nv=a;this.a.st=b;this.a.cc=d;this.a.lt=f;this.a.lv=e},Ia:function(){for(var a=[],b=this.a.et,d=0,f=k.Z.length;d<f;d++){var e=k.Z[d],g=this.a[e];"undefined"!==typeof g&&""!==g&&("tt"!==e||"tt"===e&&0===b)&&a.push(e+"="+encodeURIComponent(g))}this.a.rt&&(0===b?a.push("rt="+encodeURIComponent(this.a.rt)):90===b&&a.push("rt="+this.a.rt));return a.join("&")},La:function(){this.Ka();this.a.si=c.id;this.a.su=document.referrer;this.a.ds=n.Fa;
this.a.cl=n.colorDepth+"-bit";this.a.ln=n.language;this.a.ja=n.javaEnabled?1:0;this.a.ck=n.cookieEnabled?1:0;this.a.lo="number"===typeof _bdhm_top?1:0;this.a.fl=b.sa();this.a.v="1.1.26";this.a.cv=decodeURIComponent(this.getData("Hm_cv_"+c.id)||"");this.a.tt=document.title||"";var a=document.location.href;this.a.cm=d.k(a,k.wa)||"";this.a.cp=d.k(a,k.xa)||"";this.a.cw=d.k(a,k.va)||"";this.a.ci=d.k(a,k.ta)||"";this.a.cf=d.k(a,k.ya)||"";this.a.cu=d.k(a,k.ua)||""},init:function(){try{this.La(),0===this.a.nv?
this.Ha():this.O(".*"),h.b=this,this.da(),v.z("pv-b"),this.Ga()}catch(a){var b=[];b.push("si="+c.id);b.push("n="+encodeURIComponent(a.name));b.push("m="+encodeURIComponent(a.message));b.push("r="+encodeURIComponent(document.referrer));e.log(k.protocol+"//"+k.X+"?"+b.join("&"))}},Ga:function(){function a(){v.z("pv-d")}this.S?(this.K=r,this.a.et=0,this.a.ep="",this.i(a)):a()},i:function(a){var b=this;b.a.rnd=Math.round(Math.random()*k.M);v.z("stag-b");var d=k.protocol+"//"+k.X+"?"+b.Ia();v.z("stag-d");
b.aa(d);e.log(d,function(d){b.O(d);f.d(a,"Function")&&a.call(b)})},da:function(){var a=document.location.hash.substring(1),b=RegExp(c.id),f=-1<document.referrer.indexOf(k.ba),e=d.k(a,"jn"),g=/^heatlink$|^select$/.test(e);a&&(b.test(a)&&f&&g)&&(this.a.rnd=Math.round(Math.random()*k.M),a=document.createElement("script"),a.setAttribute("type","text/javascript"),a.setAttribute("charset","utf-8"),a.setAttribute("src",k.protocol+"//"+c.js+e+".js?"+this.a.rnd),e=document.getElementsByTagName("script")[0],
e.parentNode.insertBefore(a,e))},aa:function(a){var b=m.get("Hm_unsent_"+c.id)||"",d=this.a.u?"":"&u="+encodeURIComponent(document.location.href),b=encodeURIComponent(a.replace(/^https?:\/\//,"")+d)+(b?","+b:"");m.set("Hm_unsent_"+c.id,b)},O:function(a){var b=m.get("Hm_unsent_"+c.id)||"";b&&(a=encodeURIComponent(a.replace(/^https?:\/\//,"")),a=RegExp(a.replace(/([\*\(\)])/g,"\\$1")+"(%26u%3D[^,]*)?,?","g"),(b=b.replace(a,"").replace(/,$/,""))?m.set("Hm_unsent_"+c.id,b):m.remove("Hm_unsent_"+c.id))},
Ha:function(){var a=this,b=m.get("Hm_unsent_"+c.id);if(b)for(var b=b.split(","),d=function(b){e.log(k.protocol+"//"+decodeURIComponent(b),function(b){a.O(b)})},f=0,g=b.length;f<g;f++)d(b[f])}};return new a})();
(function(){var a=mt.s,d=mt.event,e=mt.url,b=mt.l;try{if(window.performance&&performance.timing&&"undefined"!==typeof h.b){var f=+new Date,l=function(a){var b=performance.timing,d=b[a+"Start"]?b[a+"Start"]:0;a=b[a+"End"]?b[a+"End"]:0;return{start:d,end:a,value:0<a-d?a-d:0}},n=s;a.Y(function(){n=+new Date});var g=function(){var a,d,g;g=l("navigation");d=l("request");g={netAll:d.start-g.start,netDns:l("domainLookup").value,netTcp:l("connect").value,srv:l("response").start-d.start,dom:performance.timing.domInteractive-
performance.timing.fetchStart,loadEvent:l("loadEvent").end-g.start};a=document.referrer;var m=a.match(/^(http[s]?:\/\/)?([^\/]+)(.*)/)||[],u=s;d=s;if("www.baidu.com"===m[2]||"m.baidu.com"===m[2])u=e.k(a,"qid"),d=e.k(a,"click_t");a=u;g.qid=a!=s?a:"";d!=s?(g.bdDom=n?n-d:0,g.bdRun=f-d,g.bdDef=l("navigation").start-d):(g.bdDom=0,g.bdRun=0,g.bdDef=0);h.b.a.et=87;h.b.a.ep=b.stringify(g);h.b.i()};d.c(window,"load",function(){setTimeout(g,500)})}}catch(m){}})();
(function(){var a=h.r,d={init:function(){try{if("http:"===a.protocol){var b=document.createElement("IFRAME");b.setAttribute("src","http://boscdn.bpc.baidu.com/v1/holmes-moplus/mp-cdn.html");b.style.display="none";b.style.width="1";b.style.height="1";b.Sa="0";document.body.appendChild(b)}}catch(d){}}},e=navigator.userAgent.toLowerCase();-1<e.indexOf("android")&&-1===e.indexOf("micromessenger")&&d.init()})();
(function(){var a=mt.j,d=mt.lang,e=mt.event,b=mt.l;if("undefined"!==typeof h.b&&(c.med||(!a.T||7<a.Aa)&&c.cvcc)){var f,l,n,g,m=function(a){if(a.item){for(var b=a.length,d=Array(b);b--;)d[b]=a[b];return d}return[].slice.call(a)},k=function(a,b){for(var d in a)if(a.hasOwnProperty(d)&&b.call(a,d,a[d])===w)return w},v=function(a,e){var g={};g.n=f;g.t="clk";g.v=a;if(e){var l=e.getAttribute("href"),k=e.getAttribute("onclick")?""+e.getAttribute("onclick"):s,m=e.getAttribute("id")||"";n.test(l)?(g.sn="mediate",
g.snv=l):d.d(k,"String")&&n.test(k)&&(g.sn="wrap",g.snv=k);g.id=m}h.b.a.et=86;h.b.a.ep=b.stringify(g);h.b.i();for(g=+new Date;400>=+new Date-g;);};if(c.med)l="/zoosnet",f="swt",n=/swt|zixun|call|chat|zoos|business|talk|kefu|openkf|online|\/LR\/Chatpre\.aspx/i,g={click:function(){for(var a=[],b=m(document.getElementsByTagName("a")),b=[].concat.apply(b,m(document.getElementsByTagName("area"))),b=[].concat.apply(b,m(document.getElementsByTagName("img"))),d,f,e=0,g=b.length;e<g;e++)d=b[e],f=d.getAttribute("onclick"),
d=d.getAttribute("href"),(n.test(f)||n.test(d))&&a.push(b[e]);return a}};else if(c.cvcc){l="/other-comm";f="other";n=c.cvcc.q||q;var p=c.cvcc.id||q;g={click:function(){for(var a=[],b=m(document.getElementsByTagName("a")),b=[].concat.apply(b,m(document.getElementsByTagName("area"))),b=[].concat.apply(b,m(document.getElementsByTagName("img"))),d,f,e,g=0,l=b.length;g<l;g++)d=b[g],n!==q?(f=d.getAttribute("onclick"),e=d.getAttribute("href"),p?(d=d.getAttribute("id"),(n.test(f)||n.test(e)||p.test(d))&&
a.push(b[g])):(n.test(f)||n.test(e))&&a.push(b[g])):p!==q&&(d=d.getAttribute("id"),p.test(d)&&a.push(b[g]));return a}}}if("undefined"!==typeof g&&"undefined"!==typeof n){var t;l+=/\/$/.test(l)?"":"/";var u=function(a,b){if(t===b)return v(l+a,b),w;if(d.d(b,"Array")||d.d(b,"NodeList"))for(var f=0,e=b.length;f<e;f++)if(t===b[f])return v(l+a+"/"+(f+1),b[f]),w};e.c(document,"mousedown",function(a){a=a||window.event;t=a.target||a.srcElement;var b={};for(k(g,function(a,f){b[a]=d.d(f,"Function")?f():document.getElementById(f)});t&&
t!==document&&k(b,u)!==w;)t=t.parentNode})}}})();(function(){var a=mt.s,d=mt.lang,e=mt.event,b=mt.l;if("undefined"!==typeof h.b&&d.d(c.cvcf,"Array")&&0<c.cvcf.length){var f={$:function(){for(var b=c.cvcf.length,d,g=0;g<b;g++)(d=a.la(decodeURIComponent(c.cvcf[g])))&&e.c(d,"click",f.ha())},ha:function(){return function(){h.b.a.et=86;var a={n:"form",t:"clk"};a.id=this.id;h.b.a.ep=b.stringify(a);h.b.i()}}};a.Y(function(){f.$()})}})();
(function(){var a=mt.event,d=mt.l;if(c.med&&"undefined"!==typeof h.b){var e=+new Date,b={n:"anti",sb:0,kb:0,clk:0},f=function(){h.b.a.et=86;h.b.a.ep=d.stringify(b);h.b.i()};a.c(document,"click",function(){b.clk++});a.c(document,"keyup",function(){b.kb=1});a.c(window,"scroll",function(){b.sb++});a.c(window,"unload",function(){b.t=+new Date-e;f()});a.c(window,"load",function(){setTimeout(f,5E3)})}})();
(function(){function a(){this.f=s}var d=mt.P,e=mt.j;a.prototype={Ca:function(a){if(this.f)this.h(a,0);else if(this.isSupported()){try{this.f=new ActiveXObject("BDEXIE.BDExExtension.1"),this.U=r}catch(b){this.U=w}this.U?this.h(a,0):this.h(a,-1)}else this.h(a,-1)},Na:function(){this.f&&delete this.f;this.f=s},Ja:function(a,b,d){if(this.f&&"SetLocalCache"in this.f)try{this.f.SetLocalCache(a,b)===q&&this.h(d,0)}catch(e){this.h(d,-1)}else this.h(d,-1)},pa:function(a,b){if(this.f&&"GetLocalCache"in this.f)try{this.h(b,
this.f.GetLocalCache(a))}catch(d){this.h(b,"")}else this.h(b,"")},ma:function(a){if(this.f&&"GetCryptStr"in this.f)try{this.h(a,this.f.GetCryptStr("strEncryptID1"))}catch(b){this.h(a,"")}else this.h(a,"")},h:function(a,b){"function"===typeof a&&a(b,this)},isSupported:function(){if(window.ActiveXObject||"ActiveXObject"in window)try{return!!new ActiveXObject("BDEXIE.BDExExtension.1")}catch(a){}return w},Da:function(){var a=this;this.ma(function(b){b!==q&&""!==b&&(d.log("//datax.baidu.com/x.gif?dm="+
encodeURIComponent("datax.baidu.com/webadapter/guid")+"&ac="+encodeURIComponent(b)+"&v=hm-webadapter-0.0.1&rnd="+Math.round(2147483647*Math.random())),a.Ja("hmKey",+new Date,function(){a.Na()}))})}};if(e.T&&/^http(s)?:$/.test(document.location.protocol)){var b=new a;b.Ca(function(a){0===a&&b.pa("hmKey",function(a){a=+a;(isNaN(a)||6048E5<+new Date-a)&&b.Da()})})}})();})();
