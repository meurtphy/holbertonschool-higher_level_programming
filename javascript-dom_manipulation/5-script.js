// Sélectionner l'élément cliquable
const updateHeader = document.querySelector('#update_header');

// Écouter le clic
updateHeader.addEventListener('click', () => {
  // Sélectionner le <header> et changer son contenu texte
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
