const axios = require('axios');      
const cheerio = require('cheerio');   
const fs = require('fs');            


const url = 'https://www.ign.com/games/undertale-yellow';


async function getGameRating() {
  try {
    
    const { data } = await axios.get(url);

    
    const $ = cheerio.load(data);


    const rating = $('.stack.jsx-2509706801 .title5.jsx-62124236').text().trim();

    if (rating) {
      console.log('Note:', rating);

    
      const csvData = `"Note"\n"${rating}"\n`;


      fs.writeFileSync('testRating.csv', csvData, 'utf-8');
      console.log('Fichier CSV créé avec succès');
    } else {
      console.log('Impossible la note.');
    }

  } catch (error) {
    console.error('Erreur lors du scraping:', error);
  }
}


getGameRating();
