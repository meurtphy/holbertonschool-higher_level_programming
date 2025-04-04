// Sélectionner le bouton "Add item"
const addItem = document.querySelector('#add_item');

// Ajouter un écouteur sur le clic
addItem.addEventListener('click', () => {
  // Créer un nouvel élément <li>
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Ajouter ce nouvel élément dans <ul class="my_list">
  const list = document.querySelector('.my_list');
  list.appendChild(newItem);
});
