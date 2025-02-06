const fs = require('fs');
const csv = require('csv-parser');
const axios = require('axios');
const cheerio = require('cheerio');

const games = [];

fs.createReadStream('games.csv')
  .pipe(csv())
  .on('data', (row) => {
    if (row['Nom']) {  
      games.push(row); 
    }
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
    scrapeGameRatings();
  });

async function scrapeGameRatings() {
  const header = 'Nom,Résumé,Date de sortie,Genres,Plateformes,Note\n';
  fs.writeFileSync('game_ratings_with_notes.csv', header, 'utf-8');
  console.log('Fichier CSV créé avec l\'en-tête.');

  for (const game of games) {
    const gameNameFormatted = game['Nom'].toLowerCase().replace(/\s+/g, '-');
    const url = `https://www.ign.com/games/${gameNameFormatted}`;
    
    console.log(`Vérification de l'URL: ${url}`);

    try {
      const response = await axios.get(url);
      
      if (response.status === 404) {
        console.log(`Erreur 404 pour le jeu: ${game['Nom']}. Sa n'extste pas.`);
        saveToCSV(game, 'Page non trouvée');
        continue; 
      }

      const $ = cheerio.load(response.data);

      await new Promise(resolve => setTimeout(resolve, 2000));
      
      const rating = $('.stack.jsx-2509706801 .title5.jsx-62124236').text().trim();
      if (!rating) {
        console.log('Note introuvable avec ce sélecteur principal. Tentons un autre sélecteur...');
        
        const ratingFallback = $('span[data-testid="score"]').text().trim();
        if (!ratingFallback) {
          console.log(`Aucune note trouvée pour le jeu: ${game['Nom']}`);
          saveToCSV(game, 'Note non trouvée');
          continue;
        } else {
          console.log(`Note trouvée avec le fallback: ${ratingFallback}`);
        }
      }

      console.log(`Nom du jeu: ${game['Nom']}`);
      console.log(`URL: ${url}`);
      console.log(`Note: ${rating || ratingFallback}`);

      saveToCSV(game, rating || ratingFallback);

    } catch (error) {
      console.error(`Erreur pour le jeu: ${game['Nom']} - ${error.message}`);
      saveToCSV(game, 'Erreur de scraping');
    }
  }
}

function saveToCSV(game, rating) {
  const data = `${game['Nom']},${game['Résumé']},${game['Date de sortie']},${game['Genres']},${game['Plateformes']},${rating}\n`;

  fs.appendFileSync('game_ratings_with_notes.csv', data, 'utf-8');
  console.log(`Saved pour ${game['Nom']}`);
}
