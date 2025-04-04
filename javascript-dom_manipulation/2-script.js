// Sélectionne l'élément à cliquer
const redHeader = document.querySelector('#red_header');

// Quand on clique sur #red_header
redHeader.addEventListener('click', () => {
  // Sélectionne la balise <header>
  const header = document.querySelector('header');
  // Ajoute la classe "red"
  header.classList.add('red');
});
