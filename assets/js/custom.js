console.log('Turlututu');


  // Function to set the theme and save it to localStorage
  function setTheme(theme) {
    jtd.setTheme(theme);
    localStorage.setItem('theme', theme); // Save the theme preference
    toggleDarkMode.textContent = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
  }

  // Function to initialize the theme based on localStorage
  function initializeTheme() {
    const savedTheme = localStorage.getItem('theme'); // Retrieve the saved theme
    if (savedTheme) {
      setTheme(savedTheme); // Apply the saved theme
    } else {
      // Default to system preference or light mode
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      setTheme(prefersDark ? 'dark' : 'light');
    }
  }

  // Initialize the theme when the page loads
  initializeTheme();


