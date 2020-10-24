function openNav() {
  document.getElementById("mySidepanel").style.width = "280px";
  document.getElementById("overlay").style.display = "block";
  window.addEventListener('scroll', noScroll)
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
  document.getElementById("overlay").style.display = "none";
  window.removeEventListener('scroll', noScroll)
}
function noScroll() {
  window.scrollTo(0, 0)
}