/*
legitRipple.js v1.0.0, Copyright by Matthias Vogt (ISC license)
ripple.min.js, compiled: 12/10/2015 @ 0:29:21
*/
!function(t){t.fn.ripple=function(n,e){var i,o,a,s,r,p,l,u=20,c="ontouchstart"in window||"onmsgesturechange"in window,d=function(t,n){return(c?"touch"+t:"mouse"+n)+".ripple"},f=function(t){return c?t.originalEvent.touches.length:0},m=function(t){return c&&(t=t.originalEvent.touches[0]),[t.pageX,t.pageY]};if(this.off(".ripple").data("unbound",!0),n&&n.unbind)return this;this.addClass("legitRipple").removeData("unbound").on(d("start","down"),function(n){f(n)<=1&&(o=t(this),g(m(n)))}).on("dragstart.ripple",function(t){i.allowDragging||t.preventDefault()}),t(document).on(d("move","move"),function(t){o&&!o.data("unbound")&&f(t)<=1&&h(m(t))}).on(d("end","up"),function(t){!o||o.data("unbound")||f(t)||v()}).on("contextmenu.ripple",function(n){"WebkitAppearance"in document.documentElement.style&&t(document).trigger("mouseup.ripple")}),t(window).on("scroll.ripple blur.ripple",function(){o&&!o.data("unbound")&&v()});var g=function(n){i={},l=0,a=[o.outerWidth(),o.outerHeight()],w(),p=n,r=t("<span/>"),i.hasCustomRipple&&o.clone().children(".legitRipple-custom").last().removeClass("legitRipple-custom").appendTo(r),r.addClass("legitRipple-ripple").appendTo(o),x(n,!1),s=r.css("transition");var e=r.css("transition-duration").split(",");r.css("transition-duration",[5.5*parseFloat(e)+"s"].concat(e.slice(1)).join(",")).css("width",i.maxDiameter)},h=function(t){var n;if(l++,"proportional"==i.scaleMode){var e=Math.pow(l,l/100*5);n=e>40?40:e}else if("fixed"==i.scaleMode&&Math.abs(t[1]-p[1])>6)return void v();x(t,n)},v=function(){r.css("transition","all 0s linear 0s").css("width",r.css("width")).css("transition",s),setTimeout(function(){r.css("width",i.maxDiameter).css("opacity","0")},u),r.on("transitionend webkitTransitionEnd oTransitionEnd",function(){t(this).data("firstTransitionEnded")?t(this).off().remove():t(this).data("firstTransitionEnded",!0)}),o=null},w=function(){var e={dragging:!0,adaptPos:function(){return i.dragging},maxDiameter:function(){return Math.sqrt(Math.pow(a[0],2)+Math.pow(a[1],2))/o.outerWidth()*(i.adaptPos?100:200)+1+"%"},scaleMode:"fixed",hasCustomRipple:!1,allowDragging:!1};n=n||{},t.each(e,function(t,e){i[t]=n.hasOwnProperty(t)?n[t]:"function"==typeof e?e():e})},x=function(n,s){var p=[],u=[(n[0]-o.offset().left)/a[0],(n[1]-o.offset().top)/a[1]],c=[.5-u[0],.5-u[1]],d=[100/parseFloat(i.maxDiameter),100/parseFloat(i.maxDiameter)*(a[1]/a[0])],f=[c[0]*d[0],c[1]*d[1]],m=i.dragging||0===l;if(m&&"inline"==o.css("display")){var g=t("<span/>").text("Hi!").css("font-size",0).prependTo(o),h=g.offset().left;g.remove(),p=[n[0]-h+"px",n[1]-o.offset().top+"px"]}m&&(p=[p[0]||100*u[0]+"%",p[1]||100*u[1]+"%"],r.css("left",p[0]).css("top",p[1])),r.css("transform","translate3d(-50%, -50%, 0)"+(i.adaptPos?"translate3d("+100*f[0]+"%, "+100*f[1]+"%, 0)":"")+(s?"scale("+s+")":"")),e&&e(o,r,u,parseFloat(i.maxDiameter)/100)};return this},t.ripple=function(n){t.each(n,function(n,e){t(n).ripple(e[0]||e,e[1])})},t.ripple.destroy=function(){t(".legitRipple").removeClass("legitRipple").add(window).add(document).off(".ripple"),t(".legitRipple-ripple").remove(),$active=null}}(jQuery);

$(".ripple").ripple();
















// Trigger action when the contexmenu is about to be shown

$('#rc-context-menu').addClass('hidden');

$(document).bind("contextmenu", function (event) {
    
    // Avoid the real one
    event.preventDefault();
    
    // Show contextmenu
    $("#rc-context-menu").finish().toggleClass('hidden').
    
    // In the right position (the mouse)
    css({
        top: event.pageY + "px",
        left: event.pageX + "px"
    });
});


// If the document is clicked somewhere
$(document).bind("mousedown", function (e) {
    
    // If the clicked element is not the menu
    if (!$(e.target).parents("#rc-context-menu").length > 0) {
        
        // Hide it
        $("#rc-context-menu").addClass('hidden');
    }
});


// If the menu element is clicked
$("#rc-context-menu div").click(function(){
    
    // This is the triggered action name
    switch($(this).attr("data-rc-launch")) {
        
        // A case for each action. Your actions here
        case "first": alert("first"); break;
        case "second": alert("second"); break;
        case "third": alert("third"); break;
    }
  
    // Hide it AFTER the action was triggered
    $("#rc-context-menu").addClass('hidden');
  });