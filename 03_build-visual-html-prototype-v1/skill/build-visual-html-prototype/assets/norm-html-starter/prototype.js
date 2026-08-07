document.querySelectorAll('.chip').forEach((chip) => chip.addEventListener('click', () => {
  document.querySelectorAll('.chip').forEach((item) => item.classList.remove('active'));
  chip.classList.add('active');
}));
