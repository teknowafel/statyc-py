
(function () {
  $(".article .copyButton").on("click", function () {
    let ID = $(this).attr("id");
    let SELECTED = document.createElement('textarea');
    SELECTED.value = 'https://teknowafel.github.io/statyc-py/index.html#' + ID.replace("btn", "");
    document.body.appendChild(SELECTED);
    SELECTED.select();
    document.execCommand('copy');
    document.body.removeChild(SELECTED);
    window.getSelection().removeAllRanges();
    $("#" + ID).html('Copied!');
    setTimeout(function () { $("#" + ID).html('Share'); }, 1000);
  });
  $(".article .readMoreButton").on("click", function () {
    let ARTICLE = $(this).attr("id").replace("btnMore", "");
    let STATUSES = { true: false, false: true };
    let STATUS = STATUSES[$("#" + ARTICLE + "-content").attr("data-open")];
    $("#" + ARTICLE + "-content").attr("data-open", STATUS);
    $('html, body').animate({scrollTop: ($("#" + ARTICLE).offset().top)}, 700);});
})();