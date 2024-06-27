$(document).ready(function() {
  // URL of the API endpoint for Star Wars movies
  var apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

  // Make AJAX GET request to fetch movies data
  $.ajax({
    url: apiUrl,
    method: 'GET',
    success: function(data) {
      // Iterate over each movie in the results
      data.results.forEach(function(movie) {
        // Append each movie title to the #list_movies ul
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function(error) {
      console.log('Error fetching movies:', error);
      $('#list_movies').append('<li>Error fetching movies. Please try again later.</li>');
    }
  });
});
