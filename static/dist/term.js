function openTerminal(t){var s=new WSSHClient,e=new Terminal(80,24,function(t){s.send(t)});e.open(),$(".terminal").detach().appendTo("#term"),e.resize(80,24),e.write("Connecting..."),s.connect($.extend(t,{onError:function(t){e.write("Error: "+t+"\r\n")},onConnect:function(){e.write("\r")},onClose:function(){e.write("Connection Reset By Peer")},onData:function(t){e.write(t)}}))}(function(){"use strict";function t(){this._events={}}function s(e,i,r){t.call(this);var o;"object"==typeof e&&(e=(o=e).cols,i=o.rows,r=o.handler),this._options=o||{},this.cols=e||s.geometry[0],this.rows=i||s.geometry[1],r&&this.on("data",r),this.ybase=0,this.ydisp=0,this.x=0,this.y=0,this.cursorState=0,this.cursorHidden=!1,this.convertEol=!1,this.state=0,this.queue="",this.scrollTop=0,this.scrollBottom=this.rows-1,this.applicationKeypad=!1,this.originMode=!1,this.insertMode=!1,this.wraparoundMode=!1,this.normal=null,this.charset=null,this.gcharset=null,this.glevel=0,this.charsets=[null],this.decLocator,this.x10Mouse,this.vt200Mouse,this.vt300Mouse,this.normalMouse,this.mouseEvents,this.sendFocus,this.utfMouse,this.sgrMouse,this.urxvtMouse,this.element,this.children,this.refreshStart,this.refreshEnd,this.savedX,this.savedY,this.savedCols,this.readable=!0,this.writable=!0,this.defAttr=131840,this.curAttr=this.defAttr,this.params=[],this.currentParam=0,this.prefix="",this.postfix="",this.lines=[];for(var a=this.rows;a--;)this.lines.push(this.blankLine());this.tabs,this.setupStops()}function e(t,s,e,i){t.addEventListener(s,e,i||!1)}function i(t,s,e,i){t.removeEventListener(s,e,i||!1)}function r(t){return t.preventDefault&&t.preventDefault(),t.returnValue=!1,t.stopPropagation&&t.stopPropagation(),t.cancelBubble=!0,!1}function o(t,s){function e(){this.constructor=t}e.prototype=s.prototype,t.prototype=new e}function a(){var t=n.createElement("span");t.innerHTML="hello world",n.body.appendChild(t);var s=t.scrollWidth;t.style.fontWeight="bold";var e=t.scrollWidth;return n.body.removeChild(t),s!==e}var h=this,n=this.document;t.prototype.addListener=function(t,s){this._events[t]=this._events[t]||[],this._events[t].push(s)},t.prototype.on=t.prototype.addListener,t.prototype.removeListener=function(t,s){if(this._events[t])for(var e=this._events[t],i=e.length;i--;)if(e[i]===s||e[i].listener===s)return void e.splice(i,1)},t.prototype.off=t.prototype.removeListener,t.prototype.removeAllListeners=function(t){this._events[t]&&delete this._events[t]},t.prototype.once=function(t,s){function e(){var i=Array.prototype.slice.call(arguments);return this.removeListener(t,e),s.apply(this,i)}return e.listener=s,this.on(t,e)},t.prototype.emit=function(t){if(this._events[t])for(var s=Array.prototype.slice.call(arguments,1),e=this._events[t],i=e.length,r=0;r<i;r++)e[r].apply(this,s)},t.prototype.listeners=function(t){return this._events[t]=this._events[t]||[]};o(s,t),s.colors=["#2e3436","#cc0000","#4e9a06","#c4a000","#3465a4","#75507b","#06989a","#d3d7cf","#555753","#ef2929","#8ae234","#fce94f","#729fcf","#ad7fa8","#34e2e2","#eeeeec"],s.colors=function(){function t(t,s,i){r.push("#"+e(t)+e(s)+e(i))}function e(t){return(t=t.toString(16)).length<2?"0"+t:t}var i,r=s.colors,o=[0,95,135,175,215,255];for(i=0;i<216;i++)t(o[i/36%6|0],o[i/6%6|0],o[i%6]);for(i=0;i<24;i++)t(o=8+10*i,o,o);return r}(),s.defaultColors={bg:"#000000",fg:"#f0f0f0"},s.colors[256]=s.defaultColors.bg,s.colors[257]=s.defaultColors.fg,s.termName="xterm",s.geometry=[80,30],s.cursorBlink=!0,s.visualBell=!1,s.popOnBell=!1,s.scrollback=1e3,s.screenKeys=!1,s.programFeatures=!1,s.debug=!1,s.focus=null,s.prototype.focus=function(){s.focus!==this&&(s.focus&&(s.focus.cursorState=0,s.focus.refresh(s.focus.y,s.focus.y),s.focus.sendFocus&&s.focus.send("[O")),s.focus=this,this.sendFocus&&this.send("[I"),this.showCursor())},s.bindKeys=function(){s.focus||(e(n,"keydown",function(t){return s.focus.keyDown(t)},!0),e(n,"keypress",function(t){return s.focus.keyPress(t)},!0))},s.prototype.open=function(){var t,i=this,o=0;for(this.element=n.createElement("div"),this.element.className="terminal",this.children=[];o<this.rows;o++)t=n.createElement("div"),this.element.appendChild(t),this.children.push(t);n.body.appendChild(this.element),this.refresh(0,this.rows-1),s.bindKeys(),this.focus(),this.startBlink(),e(this.element,"mousedown",function(){i.focus()}),e(this.element,"mousedown",function(t){var s=null!=t.button?+t.button:null!=t.which?t.which-1:null;~navigator.userAgent.indexOf("MSIE")&&(s=1===s?0:4===s?1:s),2===s&&(i.element.contentEditable="true",p(function(){i.element.contentEditable="inherit"},1))},!0),e(this.element,"paste",function(t){return t.clipboardData?i.send(t.clipboardData.getData("text/plain")):h.clipboardData&&i.send(h.clipboardData.getData("Text")),i.element.contentEditable="inherit",r(t)}),this.bindMouse(),null==s.brokenBold&&(s.brokenBold=a()),this.element.style.backgroundColor=s.defaultColors.bg,this.element.style.color=s.defaultColors.fg},s.prototype.bindMouse=function(){function t(t){var s,e;if(s=c(t),e=p(t))switch(a(s,e),t.type){case"mousedown":d=s;break;case"mouseup":d=32}}function s(t){var s,e=d;(s=p(t))&&a(e+=32,s)}function o(t,s){if(f.utfMouse){if(2047===s)return t.push(0);s<127?t.push(s):(s>2047&&(s=2047),t.push(192|s>>6),t.push(128|63&s))}else{if(255===s)return t.push(0);s>127&&(s=127),t.push(s)}}function a(t,s){if(f.vt300Mouse){t&=3,s.x-=32,s.y-=32;var e="[24";if(0===t)e+="1";else if(1===t)e+="3";else if(2===t)e+="5";else{if(3===t)return;e+="0"}return e+="~["+s.x+","+s.y+"]\r",void f.send(e)}return f.decLocator?(t&=3,s.x-=32,s.y-=32,0===t?t=2:1===t?t=4:2===t?t=6:3===t&&(t=3),void f.send("["+t+";"+(3===t?4:0)+";"+s.y+";"+s.x+";"+(s.page||0)+"&w")):f.urxvtMouse?(s.x-=32,s.y-=32,s.x++,s.y++,void f.send("["+t+";"+s.x+";"+s.y+"M")):f.sgrMouse?(s.x-=32,s.y-=32,void f.send("[<"+(3==(3&t)?-4&t:t)+";"+s.x+";"+s.y+(3==(3&t)?"m":"M"))):(o(e=[],t),o(e,s.x),o(e,s.y),void f.send("[M"+l.fromCharCode.apply(l,e)))}function c(t){var s,e,i,r,o;switch(t.type){case"mousedown":s=null!=t.button?+t.button:null!=t.which?t.which-1:null,~navigator.userAgent.indexOf("MSIE")&&(s=1===s?0:4===s?1:s);break;case"mouseup":s=3;break;case"DOMMouseScroll":s=t.detail<0?64:65;break;case"mousewheel":s=t.wheelDeltaY>0?64:65}return e=t.shiftKey?4:0,i=t.metaKey?8:0,r=t.ctrlKey?16:0,o=e|i|r,f.vt200Mouse?o&=r:f.normalMouse||(o=0),s=32+(o<<2)+s}function p(t){var s,e,i,r,o;if(null!=t.pageX){for(s=t.pageX,e=t.pageY,o=f.element;o!==n.documentElement;)s-=o.offsetLeft,e-=o.offsetTop,o=o.parentNode;return i=f.element.clientWidth,r=f.element.clientHeight,s=s/i*f.cols|0,e=e/r*f.rows|0,s<0&&(s=0),s>f.cols&&(s=f.cols),e<0&&(e=0),e>f.rows&&(e=f.rows),s+=32,e+=32,{x:s,y:e,down:"mousedown"===t.type,up:"mouseup"===t.type,wheel:t.type===y,move:"mousemove"===t.type}}}var u=this.element,f=this,d=32,y="onmousewheel"in h?"mousewheel":"DOMMouseScroll";e(u,"mousedown",function(o){if(f.mouseEvents)return t(o),f.focus(),f.vt200Mouse?(t({__proto__:o,type:"mouseup"}),r(o)):(f.normalMouse&&e(n,"mousemove",s),f.x10Mouse||e(n,"mouseup",function e(o){return t(o),f.normalMouse&&i(n,"mousemove",s),i(n,"mouseup",e),r(o)}),r(o))}),e(u,y,function(s){if(f.mouseEvents&&!(f.x10Mouse||f.vt300Mouse||f.decLocator))return t(s),r(s)}),e(u,y,function(t){if(!f.mouseEvents&&!f.applicationKeypad)return"DOMMouseScroll"===t.type?f.scrollDisp(t.detail<0?-5:5):f.scrollDisp(t.wheelDeltaY>0?-5:5),r(t)})},s.prototype.destroy=function(){this.readable=!1,this.writable=!1,this._events={},this.handler=function(){},this.write=function(){}},s.prototype.refresh=function(t,e){var i,r,o,a,h,n,c,l,p,u,f,d,y,b;for(e-t>=this.rows/2&&(b=this.element.parentNode)&&b.removeChild(this.element),c=this.cols,r=t;r<=e;r++){for(y=r+this.ydisp,a=this.lines[y],h="",i=r===this.y&&this.cursorState&&this.ydisp===this.ybase&&!this.cursorHidden?this.x:-1,p=this.defAttr,o=0;o<c;o++){switch(l=a[o][0],n=a[o][1],o===i&&(l=-1),l!==p&&(p!==this.defAttr&&(h+="</span>"),l!==this.defAttr&&(-1===l?h+='<span class="reverse-video">':(h+='<span style="',f=511&l,u=l>>9&511,1&(d=l>>18)&&(s.brokenBold||(h+="font-weight:bold;"),u<8&&(u+=8)),2&d&&(h+="text-decoration:underline;"),256!==f&&(h+="background-color:"+s.colors[f]+";"),257!==u&&(h+="color:"+s.colors[u]+";"),h+='">'))),n){case"&":h+="&amp;";break;case"<":h+="&lt;";break;case">":h+="&gt;";break;default:h+=n<=" "?"&nbsp;":n}p=l}p!==this.defAttr&&(h+="</span>"),this.children[r].innerHTML=h}b&&b.appendChild(this.element)},s.prototype.cursorBlink=function(){s.focus===this&&(this.cursorState^=1,this.refresh(this.y,this.y))},s.prototype.showCursor=function(){this.cursorState||(this.cursorState=1,this.refresh(this.y,this.y))},s.prototype.startBlink=function(){if(s.cursorBlink){var t=this;this._blinker=function(){t.cursorBlink()},this._blink=u(this._blinker,500)}},s.prototype.refreshBlink=function(){s.cursorBlink&&(clearInterval(this._blink),this._blink=u(this._blinker,500))},s.prototype.scroll=function(){var t;++this.ybase===s.scrollback&&(this.ybase=this.ybase/2|0,this.lines=this.lines.slice(1-(this.ybase+this.rows))),this.ydisp=this.ybase,t=this.ybase+this.rows-1,(t-=this.rows-1-this.scrollBottom)===this.lines.length?this.lines.push(this.blankLine()):this.lines.splice(t,0,this.blankLine()),0!==this.scrollTop&&(0!==this.ybase&&(this.ybase--,this.ydisp=this.ybase),this.lines.splice(this.ybase+this.scrollTop,1)),this.updateRange(this.scrollTop),this.updateRange(this.scrollBottom)},s.prototype.scrollDisp=function(t){this.ydisp+=t,this.ydisp>this.ybase?this.ydisp=this.ybase:this.ydisp<0&&(this.ydisp=0),this.refresh(0,this.rows-1)},s.prototype.write=function(t){var e,i,r=t.length,o=0;for(this.refreshStart=this.y,this.refreshEnd=this.y,this.ybase!==this.ydisp&&(this.ydisp=this.ybase,this.maxRange());o<r;o++)switch(i=t[o],this.state){case 0:switch(i){case"":this.bell();break;case"\n":case"\v":case"\f":this.convertEol&&(this.x=0),++this.y>this.scrollBottom&&(this.y--,this.scroll());break;case"\r":this.x=0;break;case"\b":this.x>0&&this.x--;break;case"\t":this.x=this.nextStop();break;case"":this.setgLevel(1);break;case"":this.setgLevel(0);break;case"":this.state=1;break;default:i>=" "&&(this.charset&&this.charset[i]&&(i=this.charset[i]),this.x>=this.cols&&(this.x=0,++this.y>this.scrollBottom&&(this.y--,this.scroll())),this.lines[this.y+this.ybase][this.x]=[this.curAttr,i],this.x++,this.updateRange(this.y))}break;case 1:switch(i){case"[":this.params=[],this.currentParam=0,this.state=2;break;case"]":this.params=[],this.currentParam=0,this.state=3;break;case"P":this.params=[],this.currentParam=0,this.state=5;break;case"_":case"^":this.state=6;break;case"c":this.reset();break;case"E":this.x=0;case"D":this.index();break;case"M":this.reverseIndex();break;case"%":this.setgLevel(0),this.setgCharset(0,s.charsets.US),this.state=0,o++;break;case"(":case")":case"*":case"+":case"-":case".":switch(i){case"(":this.gcharset=0;break;case")":this.gcharset=1;break;case"*":this.gcharset=2;break;case"+":this.gcharset=3;break;case"-":this.gcharset=1;break;case".":this.gcharset=2}this.state=4;break;case"/":this.gcharset=3,this.state=4,o--;break;case"N":case"O":break;case"n":this.setgLevel(2);break;case"o":case"|":this.setgLevel(3);break;case"}":this.setgLevel(2);break;case"~":this.setgLevel(1);break;case"7":this.saveCursor(),this.state=0;break;case"8":this.restoreCursor(),this.state=0;break;case"#":this.state=0,o++;break;case"H":this.tabSet();break;case"=":this.log("Serial port requested application keypad."),this.applicationKeypad=!0,this.state=0;break;case">":this.log("Switching back to normal keypad."),this.applicationKeypad=!1,this.state=0;break;default:this.state=0,this.error("Unknown ESC control: %s.",i)}break;case 4:switch(i){case"0":e=s.charsets.SCLD;break;case"A":e=s.charsets.UK;break;case"B":e=s.charsets.US;break;case"4":e=s.charsets.Dutch;break;case"C":case"5":e=s.charsets.Finnish;break;case"R":e=s.charsets.French;break;case"Q":e=s.charsets.FrenchCanadian;break;case"K":e=s.charsets.German;break;case"Y":e=s.charsets.Italian;break;case"E":case"6":e=s.charsets.NorwegianDanish;break;case"Z":e=s.charsets.Spanish;break;case"H":case"7":e=s.charsets.Swedish;break;case"=":e=s.charsets.Swiss;break;case"/":e=s.charsets.ISOLatin,o++;break;default:e=s.charsets.US}this.setgCharset(this.gcharset,e),this.gcharset=null,this.state=0;break;case 3:if(""===i||""===i){switch(""===i&&o++,this.params.push(this.currentParam),this.params[0]){case 0:case 1:case 2:this.params[1]&&(this.title=this.params[1],this.handleTitle(this.title))}this.params=[],this.currentParam=0,this.state=0}else this.params.length?this.currentParam+=i:i>="0"&&i<="9"?this.currentParam=10*this.currentParam+i.charCodeAt(0)-48:";"===i&&(this.params.push(this.currentParam),this.currentParam="");break;case 2:if("?"===i||">"===i||"!"===i){this.prefix=i;break}if(i>="0"&&i<="9"){this.currentParam=10*this.currentParam+i.charCodeAt(0)-48;break}if("$"===i||'"'===i||" "===i||"'"===i){this.postfix=i;break}if(this.params.push(this.currentParam),this.currentParam=0,";"===i)break;switch(this.state=0,i){case"A":this.cursorUp(this.params);break;case"B":this.cursorDown(this.params);break;case"C":this.cursorForward(this.params);break;case"D":this.cursorBackward(this.params);break;case"H":this.cursorPos(this.params);break;case"J":this.eraseInDisplay(this.params);break;case"K":this.eraseInLine(this.params);break;case"m":this.charAttributes(this.params);break;case"n":this.deviceStatus(this.params);break;case"@":this.insertChars(this.params);break;case"E":this.cursorNextLine(this.params);break;case"F":this.cursorPrecedingLine(this.params);break;case"G":this.cursorCharAbsolute(this.params);break;case"L":this.insertLines(this.params);break;case"M":this.deleteLines(this.params);break;case"P":this.deleteChars(this.params);break;case"X":this.eraseChars(this.params);break;case"`":this.charPosAbsolute(this.params);break;case"a":this.HPositionRelative(this.params);break;case"c":this.sendDeviceAttributes(this.params);break;case"d":this.linePosAbsolute(this.params);break;case"e":this.VPositionRelative(this.params);break;case"f":this.HVPosition(this.params);break;case"h":this.setMode(this.params);break;case"l":this.resetMode(this.params);break;case"r":this.setScrollRegion(this.params);break;case"s":this.saveCursor(this.params);break;case"u":this.restoreCursor(this.params);break;case"I":this.cursorForwardTab(this.params);break;case"S":this.scrollUp(this.params);break;case"T":this.params.length<2&&!this.prefix&&this.scrollDown(this.params);break;case"Z":this.cursorBackwardTab(this.params);break;case"b":this.repeatPrecedingCharacter(this.params);break;case"g":this.tabClear(this.params);break;case"p":switch(this.prefix){case"!":this.softReset(this.params)}break;default:this.error("Unknown CSI code: %s.",i)}this.prefix="",this.postfix="";break;case 5:if(""===i||""===i){switch(""===i&&o++,this.prefix){case"":break;case"$q":h=!1;switch(a=this.currentParam){case'"q':a='0"q';break;case'"p':a='61"p';break;case"r":a=this.scrollTop+1+";"+(this.scrollBottom+1)+"r";break;case"m":a="0m";break;default:this.error("Unknown DCS Pt: %s.",a),a=""}this.send("P"+ +h+"$r"+a+"\\");break;case"+p":break;case"+q":var a=this.currentParam,h=!1;this.send("P"+ +h+"+r"+a+"\\");break;default:this.error("Unknown DCS prefix: %s.",this.prefix)}this.currentParam=0,this.prefix="",this.state=0}else this.currentParam?this.currentParam+=i:this.prefix||"$"===i||"+"===i?2===this.prefix.length?this.currentParam=i:this.prefix+=i:this.currentParam=i;break;case 6:""!==i&&""!==i||(""===i&&o++,this.state=0)}this.updateRange(this.y),this.refresh(this.refreshStart,this.refreshEnd)},s.prototype.writeln=function(t){this.write(t+"\r\n")},s.prototype.keyDown=function(t){var s;switch(t.keyCode){case 8:if(t.shiftKey){s="\b";break}s="";break;case 9:if(t.shiftKey){s="[Z";break}s="\t";break;case 13:s="\r";break;case 27:s="";break;case 37:if(this.applicationKeypad){s="OD";break}s="[D";break;case 39:if(this.applicationKeypad){s="OC";break}s="[C";break;case 38:if(this.applicationKeypad){s="OA";break}if(t.ctrlKey)return this.scrollDisp(-1),r(t);s="[A";break;case 40:if(this.applicationKeypad){s="OB";break}if(t.ctrlKey)return this.scrollDisp(1),r(t);s="[B";break;case 46:s="[3~";break;case 45:s="[2~";break;case 36:if(this.applicationKeypad){s="OH";break}s="OH";break;case 35:if(this.applicationKeypad){s="OF";break}s="OF";break;case 33:if(t.shiftKey)return this.scrollDisp(-(this.rows-1)),r(t);s="[5~";break;case 34:if(t.shiftKey)return this.scrollDisp(this.rows-1),r(t);s="[6~";break;case 112:s="OP";break;case 113:s="OQ";break;case 114:s="OR";break;case 115:s="OS";break;case 116:s="[15~";break;case 117:s="[17~";break;case 118:s="[18~";break;case 119:s="[19~";break;case 120:s="[20~";break;case 121:s="[21~";break;case 122:s="[23~";break;case 123:s="[24~";break;default:t.ctrlKey?t.keyCode>=65&&t.keyCode<=90?s=l.fromCharCode(t.keyCode-64):32===t.keyCode?s=l.fromCharCode(0):t.keyCode>=51&&t.keyCode<=55?s=l.fromCharCode(t.keyCode-51+27):56===t.keyCode?s=l.fromCharCode(127):219===t.keyCode?s=l.fromCharCode(27):221===t.keyCode&&(s=l.fromCharCode(29)):(!c&&t.altKey||c&&t.metaKey)&&(t.keyCode>=65&&t.keyCode<=90?s=""+l.fromCharCode(t.keyCode+32):192===t.keyCode?s="`":t.keyCode>=48&&t.keyCode<=57&&(s=""+(t.keyCode-48)))}return this.emit("keydown",t),!s||(this.emit("key",s,t),this.showCursor(),this.handler(s),r(t))},s.prototype.setgLevel=function(t){this.glevel=t,this.charset=this.charsets[t]},s.prototype.setgCharset=function(t,s){this.charsets[t]=s,this.glevel===t&&(this.charset=s)},s.prototype.keyPress=function(t){var s;if(r(t),t.charCode)s=t.charCode;else if(null==t.which)s=t.keyCode;else{if(0===t.which||0===t.charCode)return!1;s=t.which}return!(!s||t.ctrlKey||t.altKey||t.metaKey)&&(s=l.fromCharCode(s),this.emit("keypress",s,t),this.emit("key",s,t),this.showCursor(),this.handler(s),!1)},s.prototype.send=function(t){var s=this;this.queue||p(function(){s.handler(s.queue),s.queue=""},1),this.queue+=t},s.prototype.bell=function(){if(s.visualBell){var t=this;this.element.style.borderColor="white",p(function(){t.element.style.borderColor=""},10),s.popOnBell&&this.focus()}},s.prototype.log=function(){if(s.debug&&h.console&&h.console.log){var t=Array.prototype.slice.call(arguments);h.console.log.apply(h.console,t)}},s.prototype.error=function(){if(s.debug&&h.console&&h.console.error){var t=Array.prototype.slice.call(arguments);h.console.error.apply(h.console,t)}},s.prototype.resize=function(t,s){var e,i,r,o,a;if(t<1&&(t=1),s<1&&(s=1),(o=this.cols)<t)for(a=[this.defAttr," "],r=this.lines.length;r--;)for(;this.lines[r].length<t;)this.lines[r].push(a);else if(o>t)for(r=this.lines.length;r--;)for(;this.lines[r].length>t;)this.lines[r].pop();if(this.setupStops(o),this.cols=t,(o=this.rows)<s)for(i=this.element;o++<s;)this.lines.length<s+this.ybase&&this.lines.push(this.blankLine()),this.children.length<s&&(e=n.createElement("div"),i.appendChild(e),this.children.push(e));else if(o>s)for(;o-- >s;)if(this.lines.length>s+this.ybase&&this.lines.pop(),this.children.length>s){if(!(i=this.children.pop()))continue;i.parentNode.removeChild(i)}this.rows=s,this.y>=s&&(this.y=s-1),this.x>=t&&(this.x=t-1),this.scrollTop=0,this.scrollBottom=s-1,this.refresh(0,this.rows-1),this.normal=null},s.prototype.updateRange=function(t){t<this.refreshStart&&(this.refreshStart=t),t>this.refreshEnd&&(this.refreshEnd=t)},s.prototype.maxRange=function(){this.refreshStart=0,this.refreshEnd=this.rows-1},s.prototype.setupStops=function(t){for(null!=t?this.tabs[t]||(t=this.prevStop(t)):(this.tabs={},t=0);t<this.cols;t+=8)this.tabs[t]=!0},s.prototype.prevStop=function(t){for(null==t&&(t=this.x);!this.tabs[--t]&&t>0;);return t>=this.cols?this.cols-1:t<0?0:t},s.prototype.nextStop=function(t){for(null==t&&(t=this.x);!this.tabs[++t]&&t<this.cols;);return t>=this.cols?this.cols-1:t<0?0:t},s.prototype.eraseRight=function(t,s){for(var e=this.lines[this.ybase+s],i=[this.curAttr," "];t<this.cols;t++)e[t]=i;this.updateRange(s)},s.prototype.eraseLeft=function(t,s){var e=this.lines[this.ybase+s],i=[this.curAttr," "];for(t++;t--;)e[t]=i;this.updateRange(s)},s.prototype.eraseLine=function(t){this.eraseRight(0,t)},s.prototype.blankLine=function(t){for(var s=[t?this.curAttr:this.defAttr," "],e=[],i=0;i<this.cols;i++)e[i]=s;return e},s.prototype.ch=function(t){return t?[this.curAttr," "]:[this.defAttr," "]},s.prototype.is=function(t){return 0===((this.termName||s.termName)+"").indexOf(t)},s.prototype.handler=function(t){this.emit("data",t)},s.prototype.handleTitle=function(t){this.emit("title",t)},s.prototype.index=function(){++this.y>this.scrollBottom&&(this.y--,this.scroll()),this.state=0},s.prototype.reverseIndex=function(){var t;--this.y<this.scrollTop&&(this.y++,this.lines.splice(this.y+this.ybase,0,this.blankLine(!0)),t=this.rows-1-this.scrollBottom,this.lines.splice(this.rows-1+this.ybase-t+1,1),this.updateRange(this.scrollTop),this.updateRange(this.scrollBottom)),this.state=0},s.prototype.reset=function(){s.call(this,this.cols,this.rows),this.refresh(0,this.rows-1)},s.prototype.tabSet=function(){this.tabs[this.x]=!0,this.state=0},s.prototype.cursorUp=function(t){var s=t[0];s<1&&(s=1),this.y-=s,this.y<0&&(this.y=0)},s.prototype.cursorDown=function(t){var s=t[0];s<1&&(s=1),this.y+=s,this.y>=this.rows&&(this.y=this.rows-1)},s.prototype.cursorForward=function(t){var s=t[0];s<1&&(s=1),this.x+=s,this.x>=this.cols&&(this.x=this.cols-1)},s.prototype.cursorBackward=function(t){var s=t[0];s<1&&(s=1),this.x-=s,this.x<0&&(this.x=0)},s.prototype.cursorPos=function(t){var s,e;s=t[0]-1,e=t.length>=2?t[1]-1:0,s<0?s=0:s>=this.rows&&(s=this.rows-1),e<0?e=0:e>=this.cols&&(e=this.cols-1),this.x=e,this.y=s},s.prototype.eraseInDisplay=function(t){var s;switch(t[0]){case 0:for(this.eraseRight(this.x,this.y),s=this.y+1;s<this.rows;s++)this.eraseLine(s);break;case 1:for(this.eraseLeft(this.x,this.y),s=this.y;s--;)this.eraseLine(s);break;case 2:for(s=this.rows;s--;)this.eraseLine(s)}},s.prototype.eraseInLine=function(t){switch(t[0]){case 0:this.eraseRight(this.x,this.y);break;case 1:this.eraseLeft(this.x,this.y);break;case 2:this.eraseLine(this.y)}},s.prototype.charAttributes=function(t){for(var s,e,i,r=t.length,o=0;o<r;o++)if((i=t[o])>=30&&i<=37)this.curAttr=-261633&this.curAttr|i-30<<9;else if(i>=40&&i<=47)this.curAttr=-512&this.curAttr|i-40;else if(i>=90&&i<=97)i+=8,this.curAttr=-261633&this.curAttr|i-90<<9;else if(i>=100&&i<=107)i+=8,this.curAttr=-512&this.curAttr|i-100;else if(0===i)this.curAttr=this.defAttr;else if(1===i)this.curAttr=this.curAttr|1<<18;else if(4===i)this.curAttr=this.curAttr|2<<18;else if(7===i||27===i){if(7===i){if(this.curAttr>>18&4)continue;this.curAttr=this.curAttr|4<<18}else if(27===i){if(4&~(this.curAttr>>18))continue;this.curAttr=-1048577&this.curAttr}s=511&this.curAttr,e=this.curAttr>>9&511,this.curAttr=-262144&this.curAttr|s<<9|e}else if(22===i)this.curAttr=-262145&this.curAttr;else if(24===i)this.curAttr=-524289&this.curAttr;else if(39===i)this.curAttr=-261633&this.curAttr,this.curAttr=this.curAttr|(this.defAttr>>9&511)<<9;else if(49===i)this.curAttr=-512&this.curAttr,this.curAttr=this.curAttr|511&this.defAttr;else if(38===i){if(5!==t[o+1])continue;i=255&t[o+=2],this.curAttr=-261633&this.curAttr|i<<9}else if(48===i){if(5!==t[o+1])continue;i=255&t[o+=2],this.curAttr=-512&this.curAttr|i}},s.prototype.deviceStatus=function(t){if(this.prefix){if("?"===this.prefix)switch(t[0]){case 6:this.send("[?"+(this.y+1)+";"+(this.x+1)+"R")}}else switch(t[0]){case 5:this.send("[0n");break;case 6:this.send("["+(this.y+1)+";"+(this.x+1)+"R")}},s.prototype.insertChars=function(t){var s,e,i,r;for((s=t[0])<1&&(s=1),e=this.y+this.ybase,i=this.x,r=[this.curAttr," "];s--&&i<this.cols;)this.lines[e].splice(i++,0,r),this.lines[e].pop()},s.prototype.cursorNextLine=function(t){var s=t[0];s<1&&(s=1),this.y+=s,this.y>=this.rows&&(this.y=this.rows-1),this.x=0},s.prototype.cursorPrecedingLine=function(t){var s=t[0];s<1&&(s=1),this.y-=s,this.y<0&&(this.y=0),this.x=0},s.prototype.cursorCharAbsolute=function(t){var s=t[0];s<1&&(s=1),this.x=s-1},s.prototype.insertLines=function(t){var s,e,i;for((s=t[0])<1&&(s=1),e=this.y+this.ybase,i=this.rows-1-this.scrollBottom,i=this.rows-1+this.ybase-i+1;s--;)this.lines.splice(e,0,this.blankLine(!0)),this.lines.splice(i,1);this.updateRange(this.y),this.updateRange(this.scrollBottom)},s.prototype.deleteLines=function(t){var s,e,i;for((s=t[0])<1&&(s=1),e=this.y+this.ybase,i=this.rows-1-this.scrollBottom,i=this.rows-1+this.ybase-i;s--;)this.lines.splice(i+1,0,this.blankLine(!0)),this.lines.splice(e,1);this.updateRange(this.y),this.updateRange(this.scrollBottom)},s.prototype.deleteChars=function(t){var s,e,i;for((s=t[0])<1&&(s=1),e=this.y+this.ybase,i=[this.curAttr," "];s--;)this.lines[e].splice(this.x,1),this.lines[e].push(i)},s.prototype.eraseChars=function(t){var s,e,i,r;for((s=t[0])<1&&(s=1),e=this.y+this.ybase,i=this.x,r=[this.curAttr," "];s--&&i<this.cols;)this.lines[e][i++]=r},s.prototype.charPosAbsolute=function(t){var s=t[0];s<1&&(s=1),this.x=s-1,this.x>=this.cols&&(this.x=this.cols-1)},s.prototype.HPositionRelative=function(t){var s=t[0];s<1&&(s=1),this.x+=s,this.x>=this.cols&&(this.x=this.cols-1)},s.prototype.sendDeviceAttributes=function(t){t[0]>0||(this.prefix?">"===this.prefix&&(this.is("xterm")?this.send("[>0;276;0c"):this.is("rxvt-unicode")?this.send("[>85;95;0c"):this.is("linux")?this.send(t[0]+"c"):this.is("screen")&&this.send("[>83;40003;0c")):this.is("xterm")||this.is("rxvt-unicode")||this.is("screen")?this.send("[?1;2c"):this.is("linux")&&this.send("[?6c"))},s.prototype.linePosAbsolute=function(t){var s=t[0];s<1&&(s=1),this.y=s-1,this.y>=this.rows&&(this.y=this.rows-1)},s.prototype.VPositionRelative=function(t){var s=t[0];s<1&&(s=1),this.y+=s,this.y>=this.rows&&(this.y=this.rows-1)},s.prototype.HVPosition=function(t){t[0]<1&&(t[0]=1),t[1]<1&&(t[1]=1),this.y=t[0]-1,this.y>=this.rows&&(this.y=this.rows-1),this.x=t[1]-1,this.x>=this.cols&&(this.x=this.cols-1)},s.prototype.setMode=function(t){if("object"!=typeof t)if(this.prefix){if("?"===this.prefix)switch(t){case 1:this.applicationKeypad=!0;break;case 2:this.setgCharset(0,s.charsets.US),this.setgCharset(1,s.charsets.US),this.setgCharset(2,s.charsets.US),this.setgCharset(3,s.charsets.US);break;case 3:this.savedCols=this.cols,this.resize(132,this.rows);break;case 6:this.originMode=!0;break;case 7:this.wraparoundMode=!0;break;case 12:break;case 9:case 1e3:case 1002:case 1003:this.x10Mouse=9===t,this.vt200Mouse=1e3===t,this.normalMouse=t>1e3,this.mouseEvents=!0,this.element.style.cursor="default",this.log("Binding to mouse events.");break;case 1004:this.sendFocus=!0;break;case 1005:this.utfMouse=!0;break;case 1006:this.sgrMouse=!0;break;case 1015:this.urxvtMouse=!0;break;case 25:this.cursorHidden=!1;break;case 1049:case 47:case 1047:if(!this.normal){var e={lines:this.lines,ybase:this.ybase,ydisp:this.ydisp,x:this.x,y:this.y,scrollTop:this.scrollTop,scrollBottom:this.scrollBottom,tabs:this.tabs};this.reset(),this.normal=e,this.showCursor()}}}else switch(t){case 4:this.insertMode=!0}else for(var i=t.length,r=0;r<i;r++)this.setMode(t[r])},s.prototype.resetMode=function(t){if("object"!=typeof t)if(this.prefix){if("?"===this.prefix)switch(t){case 1:this.applicationKeypad=!1;break;case 3:132===this.cols&&this.savedCols&&this.resize(this.savedCols,this.rows),delete this.savedCols;break;case 6:this.originMode=!1;break;case 7:this.wraparoundMode=!1;break;case 12:break;case 9:case 1e3:case 1002:case 1003:this.x10Mouse=!1,this.vt200Mouse=!1,this.normalMouse=!1,this.mouseEvents=!1,this.element.style.cursor="";break;case 1004:this.sendFocus=!1;break;case 1005:this.utfMouse=!1;break;case 1006:this.sgrMouse=!1;break;case 1015:this.urxvtMouse=!1;break;case 25:this.cursorHidden=!0;break;case 1049:case 47:case 1047:this.normal&&(this.lines=this.normal.lines,this.ybase=this.normal.ybase,this.ydisp=this.normal.ydisp,this.x=this.normal.x,this.y=this.normal.y,this.scrollTop=this.normal.scrollTop,this.scrollBottom=this.normal.scrollBottom,this.tabs=this.normal.tabs,this.normal=null,this.refresh(0,this.rows-1),this.showCursor())}}else switch(t){case 4:this.insertMode=!1}else for(var s=t.length,e=0;e<s;e++)this.resetMode(t[e])},s.prototype.setScrollRegion=function(t){this.prefix||(this.scrollTop=(t[0]||1)-1,this.scrollBottom=(t[1]||this.rows)-1,this.x=0,this.y=0)},s.prototype.saveCursor=function(t){this.savedX=this.x,this.savedY=this.y},s.prototype.restoreCursor=function(t){this.x=this.savedX||0,this.y=this.savedY||0},s.prototype.cursorForwardTab=function(t){for(var s=t[0]||1;s--;)this.x=this.nextStop()},s.prototype.scrollUp=function(t){for(var s=t[0]||1;s--;)this.lines.splice(this.ybase+this.scrollTop,1),this.lines.splice(this.ybase+this.scrollBottom,0,this.blankLine());this.updateRange(this.scrollTop),this.updateRange(this.scrollBottom)},s.prototype.scrollDown=function(t){for(var s=t[0]||1;s--;)this.lines.splice(this.ybase+this.scrollBottom,1),this.lines.splice(this.ybase+this.scrollTop,0,this.blankLine());this.updateRange(this.scrollTop),this.updateRange(this.scrollBottom)},s.prototype.initMouseTracking=function(t){},s.prototype.resetTitleModes=function(t){},s.prototype.cursorBackwardTab=function(t){for(var s=t[0]||1;s--;)this.x=this.prevStop()},s.prototype.repeatPrecedingCharacter=function(t){for(var s=t[0]||1,e=this.lines[this.ybase+this.y],i=e[this.x-1]||[this.defAttr," "];s--;)e[this.x++]=i},s.prototype.tabClear=function(t){var s=t[0];s<=0?delete this.tabs[this.x]:3===s&&(this.tabs={})},s.prototype.mediaCopy=function(t){},s.prototype.setResources=function(t){},s.prototype.disableModifiers=function(t){},s.prototype.setPointerMode=function(t){},s.prototype.softReset=function(t){this.cursorHidden=!1,this.insertMode=!1,this.originMode=!1,this.wraparoundMode=!1,this.applicationKeypad=!1,this.scrollTop=0,this.scrollBottom=this.rows-1,this.curAttr=this.defAttr,this.x=this.y=0,this.charset=null,this.glevel=0,this.charsets=[null]},s.prototype.requestAnsiMode=function(t){},s.prototype.requestPrivateMode=function(t){},s.prototype.setConformanceLevel=function(t){},s.prototype.loadLEDs=function(t){},s.prototype.setCursorStyle=function(t){},s.prototype.setCharProtectionAttr=function(t){},s.prototype.restorePrivateValues=function(t){},s.prototype.setAttrInRectangle=function(t){for(var s,e,i=t[0],r=t[1],o=t[2],a=t[3],h=t[4];i<o+1;i++)for(s=this.lines[this.ybase+i],e=r;e<a;e++)s[e]=[h,s[e][1]];this.updateRange(t[0]),this.updateRange(t[2])},s.prototype.savePrivateValues=function(t){},s.prototype.manipulateWindow=function(t){},s.prototype.reverseAttrInRectangle=function(t){},s.prototype.setTitleModeFeature=function(t){},s.prototype.setWarningBellVolume=function(t){},s.prototype.setMarginBellVolume=function(t){},s.prototype.copyRectangle=function(t){},s.prototype.enableFilterRectangle=function(t){},s.prototype.requestParameters=function(t){},s.prototype.selectChangeExtent=function(t){},s.prototype.fillRectangle=function(t){for(var s,e,i=t[0],r=t[1],o=t[2],a=t[3],h=t[4];r<a+1;r++)for(s=this.lines[this.ybase+r],e=o;e<h;e++)s[e]=[s[e][0],l.fromCharCode(i)];this.updateRange(t[1]),this.updateRange(t[3])},s.prototype.enableLocatorReporting=function(t){t[0]},s.prototype.eraseRectangle=function(t){var s,e,i,r=t[0],o=t[1],a=t[2],h=t[3];for(i=[this.curAttr," "];r<a+1;r++)for(s=this.lines[this.ybase+r],e=o;e<h;e++)s[e]=i;this.updateRange(t[0]),this.updateRange(t[2])},s.prototype.setLocatorEvents=function(t){},s.prototype.selectiveEraseRectangle=function(t){},s.prototype.requestLocatorPosition=function(t){},s.prototype.insertColumns=function(){for(var t,s=params[0],e=this.ybase+this.rows,i=[this.curAttr," "];s--;)for(t=this.ybase;t<e;t++)this.lines[t].splice(this.x+1,0,i),this.lines[t].pop();this.maxRange()},s.prototype.deleteColumns=function(){for(var t,s=params[0],e=this.ybase+this.rows,i=[this.curAttr," "];s--;)for(t=this.ybase;t<e;t++)this.lines[t].splice(this.x,1),this.lines[t].push(i);this.maxRange()},s.charsets={},s.charsets.SCLD={"`":"◆",a:"▒",b:"\t",c:"\f",d:"\r",e:"\n",f:"°",g:"±",h:"␤",i:"\v",j:"┘",k:"┐",l:"┌",m:"└",n:"┼",o:"⎺",p:"⎻",q:"─",r:"⎼",s:"⎽",t:"├",u:"┤",v:"┴",w:"┬",x:"│",y:"≤",z:"≥","{":"π","|":"≠","}":"£","~":"·"},s.charsets.UK=null,s.charsets.US=null,s.charsets.Dutch=null,s.charsets.Finnish=null,s.charsets.French=null,s.charsets.FrenchCanadian=null,s.charsets.German=null,s.charsets.Italian=null,s.charsets.NorwegianDanish=null,s.charsets.Spanish=null,s.charsets.Swedish=null,s.charsets.Swiss=null,s.charsets.ISOLatin=null;var c=~navigator.userAgent.indexOf("Mac"),l=this.String,p=this.setTimeout,u=this.setInterval;s.EventEmitter=t,s.isMac=c,s.inherits=o,s.on=e,s.off=i,s.cancel=r,"undefined"!=typeof module?module.exports=s:this.Terminal=s}).call(function(){return this||("undefined"!=typeof window?window:global)}()),$(document).ready(function(){$("#ssh").hide(),$("#private_key_authentication","#connect").hide(),$("input:radio[value=private_key]","#connect").click(function(){$("#password_authentication").hide(),$("#private_key_authentication").show()}),$("input:radio[value=password]","#connect").click(function(){$("#password_authentication").show(),$("#private_key_authentication").hide()}),$("#connect").submit(function(t){function s(t){var s=!0;return t.forEach(function(t){t.val()||(s=!1)}),s}t.preventDefault(),console.log("login on ..."),$(".error").removeClass("error");var e=$("input:text#username"),i=$("input:text#hostname"),r=$("input:text#portnumber"),o=$("input[name=authentication_method]:checked","#connect").val(),a={username:e.val(),hostname:i.val(),command:"",authentication_method:o};console.log(a);var h=parseInt(r.val());if(h>0&&h<65535?$.extend(a,{port:h}):$.extend(a,{port:22}),"password"==o){var n=$("input:password#password");if(!s([e,i,n]))return toastr.warning("请填SSH写登录信息"),!1;$.extend(a,{password:n.val()})}else if("private_key"==o){var c=$("textarea#private_key");if(!s([e,i,c]))return toastr.warning("请填写密钥信息"),!1;$.extend(a,{private_key:c.val()});var l=$("input:password#key_passphrase");l.val()&&$.extend(a,{key_passphrase:l.val()})}console.log("ssh login ...."),$("#connect").hide(),$("#ssh").show(),openTerminal(a)})});