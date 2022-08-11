function setPretext(allText) {
  document.getElementById("Response").innerHTML = allText;
  allText.replace(/\n|\r|\s*/g, "");
  console.log(allText);
}
