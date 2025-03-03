console.log('Turlututu');

    // Function to get the saved theme from localStorage
    function getSavedTheme() {
      return localStorage.getItem('theme');
    }

    // Function to apply the theme
    function applyTheme(theme) {
      if (theme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
      } else {
        document.documentElement.removeAttribute('data-theme');
      }
    }

    // Initialize the theme before the page renders
    (function () {
      const savedTheme = getSavedTheme();
      if (savedTheme) {
        applyTheme(savedTheme);
      } else {
        // Default to system preference
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        applyTheme(prefersDark ? 'dark' : 'light');
      }
    })();
  const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

  // Function to set the theme and save it to localStorage
  function setTheme(theme) {
    try {
      applyTheme(theme); // Apply the theme
      localStorage.setItem('theme', theme); // Save the theme preference
      toggleDarkMode.textContent = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
      console.log(`Theme set to: ${theme}`); // Debugging: Log the theme
    } catch (error) {
      console.error('Error setting theme:', error); // Debugging: Log errors
    }
  }

  // Toggle the theme on button click
  if (toggleDarkMode) {
    toggleDarkMode.addEventListener('click', function () {
      const currentTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
    });
  }
