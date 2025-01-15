// Toggle the collapsible left menu on click
const menuButton = document.getElementById('menu-btn');
const leftMenu = document.getElementById('left-menu');

if (menuButton && leftMenu) {
    menuButton.addEventListener('click', () => {
        if (leftMenu.style.display === 'block') {
            leftMenu.style.display = 'none';
        } else {
            leftMenu.style.display = 'block';
        }
    });
}
