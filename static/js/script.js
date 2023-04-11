const items = document.querySelectorAll('.item');

items.forEach(item => {
  item.addEventListener('mouseover', () => {
    const imageUrl = item.getAttribute('data-image');
    document.body.style.backgroundImage = `url(${imageUrl})`;
    document.body.classList.add('body-hovered');
  });
  
  item.addEventListener('mouseout', () => {
    document.body.classList.remove('body-hovered');
    document.body.style.backgroundImage = 'url(default-image.jpg)';
  });
});
