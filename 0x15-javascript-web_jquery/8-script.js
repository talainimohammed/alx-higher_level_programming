$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(body) {
  let film = body["results"];
  let l = $("#list_movies");
  film.forEach(element => {
    l.append("<li>" + element["title"] + "</li>\n");
  });
});
