$.ajaxSetup({beforeSend:function(e,t){if(!function(e){return/^(GET|HEAD|OPTIONS|TRACE)$/.test(e)}(t.type)&&!this.crossDomain){var n=function(e){var t=null;if(document.cookie&&""!=document.cookie)for(var n=document.cookie.split(";"),o=0;o<n.length;o++){var r=jQuery.trim(n[o]);if(r.substring(0,e.length+1)==e+"="){t=decodeURIComponent(r.substring(e.length+1));break}}return t}("csrftoken");e.setRequestHeader("X-CSRFToken",n)}}});