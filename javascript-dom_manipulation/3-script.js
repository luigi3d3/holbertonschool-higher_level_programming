document.addEventListener('DOMContentLoaded', function () {
    const toggle_header = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    toggle_header.addEventListener('click', function () {
        header.classList.toggle_header('red');
        header.classList.toggle_header('green');
    });
});
