//GETS BASE URL OF SITE
const baseURL = window.location.origin+window.location.pathname;

(function () {

//ON CLICK ON SCOLLER
  $(".scroller button").on("click", function () {
    $("html, body").animate({scrollTop : 0},500);
  });

//ON CLICK ON "SHARE"

  $(".article .copyButton").on("click", function () {

    //DEFINE TEMPORARY VARIABLES
    let ID = $(this).attr("id");
    let SELECTED = document.createElement('textarea');

    //SET THE TEXT GENERATED
    SELECTED.value = baseURL + '#' + ID.replace("btn", "");

    //COPY THE TEXT
    document.body.appendChild(SELECTED);
    SELECTED.select();
    document.execCommand('copy');
    document.body.removeChild(SELECTED);
    window.getSelection().removeAllRanges();

    //TELL THE USER THAT THE TEXT IS COPIED & THEN RESET THE TEXT AFTER 1000ms
    $("#" + ID).html('Copied!');
    setTimeout(function () { $("#" + ID).html('Share'); }, 1000);
  });

//ON CLICK ON "READ MORE"

  $(".article .readMoreButton").on("click", function () {

    //DEFINE TEMPORARY VARIABLES
    let ARTICLE = $(this).attr("id").replace("btnMore", "");
    let STATUSES = { true: [false, "Read Less"], false: [true, "Read More"] };

    //SCROLL TO TOP
    $('html, body').animate({ scrollTop: ($("#" + ARTICLE).offset().top) }, 700);

    //DEFINE DATA-OPEN OF CURRENT ID
    $("#" + ARTICLE + "-content").attr("data-open", STATUSES[$("#" + ARTICLE + "-content").attr("data-open")][0]);

    //DEFINE THE MAX HEIGHT OF THE CURRENT ID (DISABLED BY CSS IF FALSE)
    $("#" + ARTICLE + "-content").attr("style", "max-height:" + $("#" + ARTICLE + "-content").prop('scrollHeight') + "pt");

    //UPDATE THE TEXT OF THE BUTTON
    $("#" + $(this).attr("id")).html( STATUSES[$("#" + ARTICLE + "-content").attr("data-open")][1]);
  });
})();