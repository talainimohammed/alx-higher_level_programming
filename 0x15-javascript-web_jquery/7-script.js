const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (body) {
  let name = body['name'];
  $('#character').html(name);
});
