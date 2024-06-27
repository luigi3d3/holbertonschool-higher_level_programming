$(document).ready(function() {
  // URL of the API endpoint
  var apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

  // Make AJAX GET request to fetch character data
  $.ajax({
    url: apiUrl,
    method: 'GET',
    success: function(data) {
      // Update the content of #character div with character name
      $('#character').text(data.name);
    },
    error: function(error) {
      console.log('Error fetching character:', error);
      $('#character').text('Error fetching character. Please try again later.');
    }
  });
});
