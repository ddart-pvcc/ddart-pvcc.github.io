function createInputs() {
  const bartenders = parseInt(document.getElementById('bartenders').value);

  if (bartenders > 0) {
    document.getElementById('managerForm').classList.add('hidden');
    document.getElementById('hoursForm').classList.remove('hidden');

    const inputsContainer = document.getElementById('inputsContainer');
    inputsContainer.innerHTML = '';

    for (let i = 0; i < bartenders; i++) {
      const inputContainer = document.createElement('div');

      const nameLabel = document.createElement('label');
      nameLabel.textContent = `Bartender ${i + 1} name:`;
      inputContainer.appendChild(nameLabel);

      const nameInput = document.createElement('input');
      nameInput.type = 'text';
      nameInput.id = `bartender${i + 1}Name`;
      inputContainer.appendChild(nameInput);

      const hoursLabel = document.createElement('label');
      hoursLabel.textContent = `Bartender ${i + 1} hours:`;
      inputContainer.appendChild(hoursLabel);

      const hoursInput = document.createElement('input');
      hoursInput.type = 'number';
      hoursInput.min = '0';
      hoursInput.placeholder = `Bartender ${i + 1} hours`;
      inputContainer.appendChild(hoursInput);

      inputsContainer.appendChild(inputContainer);

      
    }
  }
}

function calculateTips() {
  const inputsContainer = document.getElementById('inputsContainer');
  const nameInputs = inputsContainer.querySelectorAll('input[type="text"]');
  const hoursInputs = inputsContainer.querySelectorAll('input[type="number"]');
  const totalTips = parseFloat(document.getElementById('totalTips').value);
  let totalHours = 0;

  const tableBody = document.getElementById('tableBody');
  tableBody.innerHTML = ''; // Clear previous table data

  nameInputs.forEach((input, index) => {
    const name = input.value;
    const hours = parseFloat(hoursInputs[index].value);
    totalHours += hours;

    const row = document.createElement('tr');

    const bartenderCell = document.createElement('td');
    bartenderCell.textContent = name;
    row.appendChild(bartenderCell);

    const hoursCell = document.createElement('td');
    hoursCell.textContent = hours;
    row.appendChild(hoursCell);

    tableBody.appendChild(row);

    
  });

  const tipPercentage = (totalHours > 0) ? totalTips / totalHours : 0;
  const tips = [];

  nameInputs.forEach((input, index) => {
    const hours = parseFloat(hoursInputs[index].value);
    const tipAmount = (tipPercentage * hours).toFixed(2);
    tips.push(tipAmount);

    const row = tableBody.childNodes[index];
    const tipCell = document.createElement('td');
    tipCell.textContent = tipAmount;
    row.appendChild(tipCell);
  });

  document.getElementById('hoursForm').classList.add('hidden');
  document.getElementById('result').classList.remove('hidden');
  document.getElementById('tipTable').classList.remove('hidden');
}