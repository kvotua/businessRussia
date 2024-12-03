document.addEventListener('DOMContentLoaded', function() {
    // Путь к файлу CSV
    const csvFile = 'cities.csv';

    // Получаем элемент <select> по его id
    const select = document.getElementById('cities');

    // Функция для чтения CSV файла
    function readCSV(filePath) {
        fetch(filePath)
            .then(response => response.text())
            .then(data => {
                // Разделяем строки по переносу строки
                const rows = data.split('\n');

                // Создаем элементы <option> для каждого города
                rows.forEach(row => {
                    const option = document.createElement('option');
                    option.value = row.split(';')[0];
                    option.text = row.split(';')[0];
                    select.appendChild(option);
                });
            })
            .catch(error => console.error('Ошибка чтения CSV файла:', error));
    }

    // Вызываем функцию чтения CSV файла
    readCSV(csvFile);
});