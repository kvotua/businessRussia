document.addEventListener('DOMContentLoaded', function() {
    const csvFile = '/frontend/bd/cities.csv';

    const dropdown = document.querySelector('.custom-dropdown');
    const arrow = dropdown.querySelector('.arrow');
    const selectedOption = dropdown.querySelector('.selected-option');
    const optionsList = dropdown.querySelector('.options-list');
    let cities = [];

    function readCSV(filePath) {
        fetch(filePath)
            .then(response => response.text())
            .then(data => {
                const rows = data.split('\n');
                cities = rows.map(row => row.split(';')[0]);
                renderOptions(cities);
            })
            .catch(error => console.error('Ошибка чтения CSV файла:', error));
    }

    function renderOptions(filteredCities) {
        optionsList.innerHTML = '';
        filteredCities.forEach(city => {
            const li = document.createElement('li');
            li.innerHTML = `<img src="/frontend/images/location_mark.png" alt="" class="location-icon">${city}`;
            li.addEventListener('click', function() {
                selectedOption.value = city;
                optionsList.style.display = 'none';
            });
            optionsList.appendChild(li);
        });
    }

    readCSV(csvFile);

    selectedOption.addEventListener('focus', function() {
        optionsList.style.display = 'block';
    });

    selectedOption.addEventListener('input', function() {
        const filter = selectedOption.value.toLowerCase();
        const filteredCities = cities.filter(city => city.toLowerCase().startsWith(filter));
        if (filteredCities.length > 0) {            
            renderOptions(filteredCities);
            optionsList.style.display = 'block';
        } else {
            optionsList.style.display = 'none';
        }
    });

    document.addEventListener('click', function(event) {
        if (!dropdown.contains(event.target)) {
            optionsList.style.display = 'none';
        }       
    });


    const buttons = document.querySelectorAll('.type-button');
    let selectedCount = 0;
    const selectedTypes = [];

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            if (button.classList.contains('button-selected')) {
                button.classList.remove('button-selected');
                selectedCount--;
                selectedTypes.splice(selectedTypes.indexOf(button.textContent), 1); 
            } else {
                if (selectedCount < 3) {
                    button.classList.add('button-selected');
                    selectedCount++;
                    selectedTypes.push(button.textContent); 
                }
            }
            document.getElementById('selected-types').value = selectedTypes.join(',');             
        });
    });
});