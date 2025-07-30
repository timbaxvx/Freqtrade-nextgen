module.exports = {
  content: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'bg-dark': '#181A20',
        'neon-cyan': '#00FFF7',
        'neon-magenta': '#FF00EA',
        'neon-lime': '#B6FF00',
        'glass': 'rgba(24,26,32,0.7)',
      },
      boxShadow: {
        'neon-cyan': '0 0 8px #00FFF7, 0 0 16px #00FFF7',
        'neon-magenta': '0 0 8px #FF00EA, 0 0 16px #FF00EA',
        'neon-lime': '0 0 8px #B6FF00, 0 0 16px #B6FF00',
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
}