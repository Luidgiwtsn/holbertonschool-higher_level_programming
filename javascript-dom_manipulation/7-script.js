fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    var list = document.querySelector('#list_movies');

    data.results.forEach(function (movie) {
      var newItem = document.createElement('li');
      newItem.textContent = movie.title;
      list.appendChild(newItem);
    });
  });
