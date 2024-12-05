document.addEventListener('DOMContentLoaded', function() {
    const csvFile = './bd/cities.csv';

    const dropdown = document.querySelector('.custom-dropdown');
    const arrow = dropdown.querySelector('.arrow');
    const selectedOption = dropdown.querySelector('.selected-option');
    const optionsList = dropdown.querySelector('.options-list');

    function readCSV(filePath) {
        fetch(filePath)
            .then(response => response.text())
            .then(data => {
                const rows = data.split('\n');

                rows.forEach(row => {
                    const city = row.split(';')[0];
                    const li = document.createElement('li');
                    li.innerHTML = `<img src="./images/location_mark.png" alt="Location Icon" class="location-icon">${city}`;
                    li.addEventListener('click', function() {
                        selectedOption.querySelector('.selected-text').textContent = city;
                        dropdown.classList.remove('open');
                        arrow.src = "./images/arrow_down.png";
                        selectedOption.style.color = 'rgba(46, 2, 73, 0.3)';
                        dropdown.style.borderColor = 'rgba(46, 2, 73, 0.3)';
                    });
                    optionsList.appendChild(li);
                });
            })
            .catch(error => console.error('Ошибка чтения CSV файла:', error));
    }

    readCSV(csvFile);

    selectedOption.addEventListener('click', function() {
        dropdown.classList.toggle('open');
        selectedOption.style.color = 'rgba(0, 71, 133, 1)';
        dropdown.style.borderColor = 'rgba(0, 71, 133, 1)';

        if (!dropdown.classList.contains('open')) {
            arrow.src = "./images/arrow_down.png";
            selectedOption.style.color = 'rgba(46, 2, 73, 0.3)';
            dropdown.style.borderColor = 'rgba(46, 2, 73, 0.3)';
        }
        else arrow.src = "./images/arrow_up.png";
        
    });

    document.addEventListener('click', function(event) {
        if (!dropdown.contains(event.target)) {
            dropdown.classList.remove('open');
            selectedOption.style.color = 'rgba(46, 2, 73, 0.3)';
            dropdown.style.borderColor = 'rgba(46, 2, 73, 0.3)';
            arrow.src = "./images/arrow_down.png";          
        }
    });
});