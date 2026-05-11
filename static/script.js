const button = document.querySelector('button');
const quoteText = document.querySelector('p');

button.addEventListener('click', function() {
  fetch('/quotes/random')
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      quoteText.textContent = '"' + data.quote + '" - ' + data.author;
    });
});