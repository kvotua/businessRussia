document.addEventListener('DOMContentLoaded', function() {
    const csvFile = '/frontend/bd/cities.csv';

    const sendButton = document.querySelector('.send-button');

    const dropdown = document.querySelector('.custom-dropdown');
    const selectedOption = dropdown.querySelector('.selected-option');
    const optionsList = dropdown.querySelector('.options-list');
    let cities = [];
    let types_of_problem = [];

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

    document.querySelector('.form').addEventListener('submit', async (event) => {
        event.preventDefault(); 

        
        const name = document.querySelector('input[name="name"]').value;
        const phone = document.querySelector('input[name="phone"]').value;
        const city = document.querySelector('input[name="city"]').value;
        const activity = document.querySelector('input[name="activity"]').value;
        const organization_name = document.querySelector('input[name="organization"]').value;
        const problem_description = document.querySelector('input[name="problem-description"]').value;

        const request = {
            types_of_problem: types_of_problem,
            name: name,
            phone: phone,
            city: city,
            activity: activity,
            organization_name: organization_name,
            problem_description: problem_description
        };
      
        try {
          const response = await fetch("http://127.0.0.1:8000/api/send", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(request) 
          });

          document.querySelector(".main-content").style.display = "none";
          document.querySelector(".info-container.success-message").style.display = "flex";
      
          if (response.ok) {
            const result = await response.json();
            console.log('Успешно:', result);
          } else {
            console.error('Ошибка:', response.statusText);
          }
        } catch (error) {
          console.error('Ошибка сети:', error);
        }
      });   

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
    let selectedButtons = [];
    

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            if (button.classList.contains('button-selected')) {
                button.classList.remove('button-selected');
                selectedCount--;
                types_of_problem.splice(types_of_problem.indexOf(button.textContent), 1); 
                selectedButtons = selectedButtons.filter(btn => btn !== button);
            } else {
                button.classList.add('button-selected');
                selectedCount++;
                selectedButtons.push(button);
                types_of_problem.push(button.textContent); 

                if (selectedCount > 3) { 
                    selectedButtons[0].classList.remove('button-selected');
                    selectedButtons.shift();                
                    types_of_problem.shift();
                    selectedCount--;
                } 
            }
        });
    });

    Inputmask({
        mask: '+7 (999) 999-99-99', // Маска для номера
        showMaskOnHover: true
      }).mask(document.getElementById('phone'));
});