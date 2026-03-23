document.querySelector('#add_item').addEventListener('click', function () {
  var newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
