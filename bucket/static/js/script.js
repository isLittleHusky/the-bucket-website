function hamburgerClick() {
	const menuButton = document.querySelector('.menu-button');
	const menu = document.querySelector('.menu');
	menuButton.classList.toggle('change');
	menu.classList.toggle('change');
}