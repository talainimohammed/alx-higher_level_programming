$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(body) {
  let hello = body["hello"];
  $("#hello").html(hello);
});
