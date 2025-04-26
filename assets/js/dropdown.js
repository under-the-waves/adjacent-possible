document.addEventListener('DOMContentLoaded', function() {
  var dropdown = document.getElementById('lifeAreasDropdown');
  var dropbtn = document.getElementById('lifeAreasButton');
  
  // Toggle dropdown on button click
  dropbtn.addEventListener('click', function(event) {
    event.preventDefault();
    dropdown.classList.toggle('active');
  });
  
  // Close dropdown when clicking outside
  document.addEventListener('click', function(event) {
    if (!event.target.closest('#lifeAreasButton') && !event.target.closest('#lifeAreasDropdown')) {
      dropdown.classList.remove('active');
    }
  });
});
