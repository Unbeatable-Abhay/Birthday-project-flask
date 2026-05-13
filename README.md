# 🎂 Birthday Project Flask

A beautiful, interactive Flask-based birthday greeting website with glassmorphism design and personalized birthday messages.

**Live Demo:** [Birthday Project on Render](https://birthday-project-flask.onrender.com)

---

## ✨ Features

- 🎨 **Modern Glassmorphism Design** – Frosted glass effects with smooth animations
- 🎉 **Personalized Birthday Messages** – Dynamic content based on user input
- 📱 **Responsive Layout** – Works seamlessly on desktop, tablet, and mobile
- 🌈 **Beautiful Gradient Backgrounds** – Custom background images with CSS styling
- ⚡ **Fast & Lightweight** – Minimal dependencies, optimized performance
- 🚀 **Production Ready** – Deployed on Render with proper configuration

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Backend logic |
| **Flask** | Web framework |
| **HTML5** | Structure |
| **CSS3** | Styling & animations (glassmorphism) |
| **JavaScript** | Interactivity |
| **Jinja2** | Template rendering |

---

## 📋 Project Structure

```
Birthday-project-flask/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Glassmorphism design & animations
│   ├── js/
│   │   └── script.js      # Frontend interactivity
│   └── images/
│       └── background.*   # Custom background images
├── templates/
│   ├── base.html          # Base template
│   └── birthday.html      # Birthday greeting template
└── README.md              # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Unbeatable-Abhay/Birthday-project-flask.git
   cd Birthday-project-flask
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   - **Windows (CMD):**
     ```bash
     venv\Scripts\activate
     ```
   - **Windows (PowerShell):**
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running Locally

### Start the Flask server:

```bash
python app.py
```

The application will be available at: **`http://localhost:5000`**

### Debug Mode (Development):

```bash
flask run --debug
```

### Local Network Access:

To preview on other devices on your network:

```bash
flask run --host=0.0.0.0 --port=5000
```

Then access via your machine's IPv4 address:
```
http://<your-ipv4-address>:5000
```

---

## 🌐 Deployment (Render)

This project is deployed on **Render.com**. Here's how it was set up:

### Render Configuration:

1. **Create Procfile** (already included):
   ```
   web: gunicorn app:app
   ```

2. **Update requirements.txt:**
   ```bash
   pip freeze > requirements.txt
   ```

3. **Connect GitHub repository** to Render
4. **Set environment variables** if needed
5. **Deploy** – Render auto-deploys on push

### Accessing the live site:
Visit: [https://birthday-project-flask.onrender.com](https://birthday-project-flask.onrender.com)

---

## 🎨 Design Highlights

### Glassmorphism Effect:
- Semi-transparent backgrounds with backdrop blur
- Elegant gradient overlays
- Smooth shadow effects
- Modern, clean aesthetic

### CSS Features Used:
```css
backdrop-filter: blur(10px);
background: rgba(255, 255, 255, 0.1);
border-radius: 15px;
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
```

---

## 📚 Learning Journey

This project was a hands-on exploration of:

✅ Flask web framework fundamentals  
✅ HTML/CSS/JavaScript integration  
✅ Git & GitHub workflows (PyCharm on Windows)  
✅ Branch management (handling master vs main naming)  
✅ Local network debugging & IPv4 access  
✅ CSS3 animations & modern design patterns  
✅ Background image pathing in Flask  
✅ Production deployment on Render  

---

## 🔧 Usage

1. **Enter a name** in the input field
2. **Click "Celebrate"** or press Enter
3. **Enjoy** a personalized birthday message with animations
4. **Share** the link with friends!

---

## 🐛 Troubleshooting

### Issue: Background images not loading
**Solution:** Check the image path in `static/images/` and update the CSS accordingly.

### Issue: Port 5000 already in use
**Solution:** Use a different port:
```bash
flask run --port=5001
```

### Issue: Git branch conflicts (master vs main)
**Solution:** Rename your branch:
```bash
git branch -m master main
git push origin main
```

---

## 📈 Future Enhancements

- [ ] User account system with saved celebrations
- [ ] Birthday countdown timer
- [ ] Custom confetti animations
- [ ] Multiple language support
- [ ] Birthday cake animation
- [ ] Share to social media integration
- [ ] Dark mode toggle
- [ ] Email birthday reminders

---

## 📄 Requirements

```
Flask==2.3.0
gunicorn==20.1.0
Werkzeug==2.3.0
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open source and available under the **MIT License** - feel free to use it for personal or educational purposes.

---

## 👨‍💻 Author

**Abhay** | CSE-AI Student @ NIET  
GitHub: [@Unbeatable-Abhay](https://github.com/Unbeatable-Abhay)

---

## 🙏 Acknowledgments

- Flask community & documentation
- CSS Glassmorphism design inspiration
- Render.com for free hosting
- Git & GitHub for version control

---

## 📞 Support

If you have questions or run into issues:
- Open an [Issue](https://github.com/Unbeatable-Abhay/Birthday-project-flask/issues)
- Check existing documentation
- Review Flask docs: [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

**Made with ❤️ by Abhay**

⭐ If you found this helpful, consider starring the repo!
