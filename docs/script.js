const copyToClipboard = str => {
  const el = document.createElement('textarea');
  el.value = str;
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);
  const selected =
    document.getSelection().rangeCount > 0 ? document.getSelection().getRangeAt(0) : false;
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  if (selected) {
    document.getSelection().removeAllRanges();
    document.getSelection().addRange(selected);
  }

};

function copiedAlert(id) {
  document.getElementById(id).textContent = 'Copied!';
  setTimeout(function (){
    document.getElementById(id).textContent = 'Share';
  }, 1000);
}

function readMore(name, articleName, button) {
  var elmnt = document.getElementById(articleName);
  var h = document.getElementById(name).scrollHeight;
  document.getElementById(name).style.maxHeight = h + 'pt';
  document.getElementById(button).textContent = 'Read Less';
  
  setTimeout(function (){
    elmnt.scrollIntoView({ behavior: 'smooth' });
  }, 700);
}

function readLess(name, articleName, button) {
  document.getElementById(name).style.maxHeight = '60pt';
  var elmnt = document.getElementById(articleName);
  document.getElementById(button).textContent = 'Read More';

  setTimeout(function (){
    elmnt.scrollIntoView({ behavior: 'smooth' });
  }, 700);
}

function readButton(name, articleName, button) {
  var article = document.getElementById(name);
  var articleOpen = article.getAttribute('data-open');

  if (articleOpen == "false"){
    readMore(name, articleName, button)
    article.setAttribute("data-open", 'true')
  } else {
    readLess(name, articleName, button)
    article.setAttribute("data-open", 'false')
  }
}
