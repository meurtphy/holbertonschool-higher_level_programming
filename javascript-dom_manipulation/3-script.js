// Sélectionne le bouton de toggle
const toggleHeader = document.querySelector('#toggle_header');

// Écoute le clic
toggleHeader.addEventListener('click', () => {
  const header = document.querySelector('header');

  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
