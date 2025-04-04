fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Insère le nom du personnage dans le <div id="character">
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Erreur lors du fetch:', error);
  });
