document.addEventListener('DOMContentLoaded', function () {
    const listFilm = document.getElementById('list-film');

    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => response.json())
        .then(data => {
            data.result.forEach(film => {
                const listMovies = document.createElement('li');
                listMovies.textContent = film.title;
                listFilm.appendChild(listMovies);
            });
        })
        .catch(error => {
            console.log('Error fetching data:', error);
        });
})