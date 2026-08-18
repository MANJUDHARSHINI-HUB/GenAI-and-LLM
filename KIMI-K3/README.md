# Ryomen Sukuna — 3D Showcase

An interactive, animated 3D showcase page for Ryomen Sukuna ("King of Curses" from *Jujutsu Kaisen*), packaged as a Streamlit app so it can be run locally or deployed to Streamlit Community Cloud.

## Description

This project renders a fully custom HTML/CSS/JavaScript "character showcase" card inside a Streamlit app. The original front-end code is untouched in terms of design, layout, colors, fonts, and behavior — Streamlit is only used as a thin wrapper (via `streamlit.components.v1.html`) to host and serve it.

## Features

- 🔄 Auto-rotating 3D image carousel (pauses on hover)
- 🃏 3D flip card revealing Sukuna's Domain Expansion info
- 🎵 Procedural ambient background music toggle (Web Audio API, no audio files needed)
- 🟣 Floating glowing orbs that subtly follow the mouse
- 🧊 Decorative rotating 3D cube
- 💬 Auto-rotating character quotes
- ✨ Animated glowing title, cards, and domain bar
- 📱 Responsive layout with mobile-friendly CSS
- 🈴 Floating drifting curse-mark kanji characters

## Technologies Used

- **Streamlit** — app shell / hosting for local + cloud deployment
- **HTML5 / CSS3** — layout, 3D transforms, animations, responsive design
- **Vanilla JavaScript** — carousel control, flip card interaction, Web Audio API ambient music, dynamic quote rotation
- **Google Fonts** — Cinzel & Orbitron

## Project Structure

```
sukuna-3d-showcase/
│
├── app.py             # Streamlit entry point — loads and renders index.html
├── index.html          # Complete original HTML/CSS/JS showcase (unmodified design)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## How to Run Locally

1. **Clone or download this project**, then move into the folder:
   ```bash
   cd sukuna-3d-showcase
   ```

2. **(Optional but recommended) Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. Streamlit will open the app automatically in your browser (usually at `http://localhost:8501`).

## How to Upload to GitHub

1. Create a new repository on GitHub (e.g. `sukuna-3d-showcase`) — do **not** initialize it with a README (you already have one).
2. In your local project folder, run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Sukuna 3D Showcase Streamlit app"
   git branch -M main
   git remote add origin https://github.com/<your-username>/sukuna-3d-showcase.git
   git push -u origin main
   ```
3. Refresh your GitHub repository page — `app.py`, `index.html`, `requirements.txt`, and `README.md` should all be visible.

## How to Deploy to Streamlit Community Cloud

1. Go to [https://share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
2. Click **"New app"**.
3. Select:
   - **Repository:** `<your-username>/sukuna-3d-showcase`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Deploy"**.
5. Wait for the build to finish — Streamlit Cloud will install `requirements.txt` automatically and launch the app.
6. Once deployed, you'll get a public URL that looks like:
   ```
   https://<your-username>-sukuna-3d-showcase-app-xxxxxx.streamlit.app
   ```
   (the exact subdomain depends on the app name you choose during deployment).

7. **Submit this deployed URL** as your Home Task link.

## Notes

- No API keys, secrets, or external services are required — the "music" is generated entirely in-browser with the Web Audio API.
- All images are loaded from their original external URLs, so no image files need to be bundled.
