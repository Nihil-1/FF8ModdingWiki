console.log('Turlututu2');


  const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

  // Toggle the theme on button click
  jtd.addEvent(toggleDarkMode, 'click', function () {
    const currentTheme = jtd.getTheme();
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
  });

