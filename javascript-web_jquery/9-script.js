// Ensure the script runs as soon as it's loaded in the <head> tag
$(document).ready(function() {
  // URL of the API endpoint for fetching the greeting message in French
  var apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

  // Make AJAX GET request to fetch the greeting message
  $.ajax({
    url: apiUrl,
    method: 'GET',
    success: function(data) {
      // Update the content of #hello div with the translated greeting message
      $('#hello').text(data.hello);
    },
    error: function(error) {
      console.log('Error fetching greeting:', error);
      $('#hello').text('Error fetching greeting. Please try again later.');
    }
  });
});
