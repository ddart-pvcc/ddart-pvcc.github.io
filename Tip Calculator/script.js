function createInputs() {
  const bartenders = parseInt(document.getElementById('bartenders').value);

  if (bartenders > 0) {
    document.getElementById('managerForm').classList.add('hidden');
    document.getElementById('hoursForm').classList.remove('hidden');

    const inputsContainer = document.getElementById('inputsContainer');
    inputsContainer.innerHTML = '';

    for (let i = 0; i < bartenders; i++) {
      const input = document.createElement('input');
      input.type = 'number';
      input.min = '0';
      input.placeholder = `Bartender ${i + 1} hours`;
      inputsContainer.appendChild(input);
    }
  }
}

function calculateTips() {
  const hoursInputs = document.querySelectorAll('#inputsContainer input');
  const totalTips = parseFloat(document.getElementById('totalTips').value);
  let totalHours = 0;

  hoursInputs.forEach(input => {
    const hours = parseFloat(input.value);
    totalHours += hours;
  });

  const tipPercentage = (totalHours > 0) ? totalTips / totalHours : 0;
  const tips = [];

  hoursInputs.forEach(input => {
    const hours = parseFloat(input.value);
    const tipAmount = (tipPercentage * hours).toFixed(2);
    tips.push(tipAmount);
  });

  document.getElementById('hoursForm').classList.add('hidden');
  document.getElementById('result').classList.remove('hidden');
  document.getElementById('tipAmount').textContent = `Tips to be paid: ${tips.join(', ')}`;
}