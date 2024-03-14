document.addEventListener('DOMContentLoaded', function () {
    const helloDiv = document.getElementById('hello');

    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            const translation = data.hello;
            helloDiv.textContent = translation;
        })
        .catch(error => {
            console.error('Error fetching translation:', error);
            helloDiv.textContent = 'Translation not available';
        });
});
