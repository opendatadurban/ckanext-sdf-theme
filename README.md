# SDF CKAN UI Extension

# ckanext-sdftheme

A custom CKAN theme extension for the MzansiXchange’s National Treasury-Secure Data Facility’s (NT-SDF) API Catalog. This extension overrides CKAN’s default templates and styles to apply MzansiXchange and NT branding while preserving the necessary functionality.

---

## Features

- Custom colour palette and typography applied via CSS overrides
- Restyled navbar, hero section, footer, buttons, and dataset listings
- Toggle pill buttons for View/Edit switching modes on datasets, organisations, and groups
- Custom homepage layout via `home/index.html` override
- Compatible with CKAN 2.10

---

## Requirements

- CKAN 2.10

### Docker Setup Requirements

If you are running CKAN via Docker (recommended for local development):

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine 20.10+
- Docker Compose v2

---

## Installation

There are two ways to install this extension — using the ckan-docker setup (recommended for local development) or into an existing CKAN virtual environment.

---

### Option 1: Using ckan-docker (Recommended)

[ckan-docker](https://github.com/ckan/ckan-docker) is the official Docker-based setup for CKAN. It provides all the infrastructure (PostgreSQL, Solr, Redis) needed to run CKAN locally.

### 1. Clone ckan-docker

```jsx
git clone https://github.com/ckan/ckan-docker.git
cd ckan-docker
```

### 2. Clone this extension into the src directory

```jsx
git clone [https://github.com/YOUR_ORG/ckanext-sdftheme.git src/ckanext-sdftheme](https://github.com/afia-ocl/ckanext-sdf-theme.git)
```

### 3. Add the extension to the Dockerfile

In `ckan/Dockerfile.dev`, add the following lines to install the extension at build time:

```jsx
COPY src/ckanext-sdftheme /srv/app/src_extensions/ckanext-sdftheme
RUN pip install -e /srv/app/src_extensions/ckanext-sdftheme
```

### 4. Configure your `.env` file

Copy the sample env file and edit it:

```jsx
cp .env.example .env
```

Add `sdftheme` to your plugins list:

```jsx
CKAN__PLUGINS="image_view text_view datatables_view datastore envvars sdftheme"
```

### 5. Build and start the containers

```jsx
docker compose -f docker-compose.dev.yml up --build -d
```

CKAN will be available at `http://localhost:5000`.

---

### Option 2: Standard Installation (existing CKAN setup)

### 1. Activate your CKAN virtual environment

```jsx
. /usr/lib/ckan/default/bin/activate
```

### 2. Clone and install the extension

```jsx
cd /usr/lib/ckan/default/src
git clone https://github.com/YOUR_ORG/ckanext-sdftheme.git
cd ckanext-sdftheme
pip install -e .
```

### 3. Add to your CKAN plugins

In your `ckan.ini`, add `sdftheme`:

```jsx
ckan.plugins = ... sdftheme
```

### 4. Restart CKAN

```jsx
sudo supervisorctl restart ckan
```

---

## Configuration

The following optional environment variables can be set in your `.env`:

```jsx
# Site logo — must be a path to a file served from a public directory
CKAN__SITE_LOGO=/images/your-logo.svg
```

Place your logo at:

```jsx
ckanext/sdftheme/public/images/your-logo.svg
```

---

## Project Structure

`ckanext-sdftheme/
├── ckanext/
│   └── sdftheme/
│       ├── assets/
│       │   ├── style.css          # Main stylesheet — edit this to restyle
│       │   ├── script.js          # Optional JS
│       │   └── webassets.yml      # Asset registration
│       ├── public/
│       │   └── images/            # Static images served at /images/
│       ├── templates/             # Jinja2 template overrides
│       │   ├── home/
│       │   │   └── index.html
│       │   ├── user/
│       │   │   └── login.html
│       │   ├── package/           # Dataset templates
│       │   ├── organization/      # Organisation templates
│       │   └── group/             # Group templates
│       ├── plugin.py              # Extension entry point
│       └── ...
├── setup.cfg
├── setup.py
└── README.md`

---

## Customising Styles

All visual overrides live in `ckanext/sdftheme/assets/style.css`. The file uses CSS custom properties (variables) defined at the top under `:root` — this is the easiest place to make sweeping changes:

```jsx
:root {
  --sdf-lavender-grey : #909cc2;
  --sdf-ghost-white   : #f7f5fb;
  --sdf-pine-teal     : #004643;
  --sdf-dusty-grape   : #52489c;
  --sdf-old-gold      : #b5b556;
}
```

Change these variables to retheme the entire site at once.

---

## Potential Improvements

### Migrate CSS to SCSS

Currently the theme uses a single plain CSS file. A natural improvement would be to migrate to SCSS, which would allow:

- **Variables as SCSS variables** — refactor `:root` CSS variables into `_variables.scss` for easier management and the ability to use them in calculations
- **Partials** — split the stylesheet into logical files (`_navbar.scss`, `_hero.scss`, `_footer.scss`, etc.) and import them into a single `main.scss`
- **Nesting** — write cleaner, more readable selectors
- **Mixins** — reuse common patterns like button styles or responsive breakpoints
- **`darken()` / `lighten()`** — generate tints and shades of brand colours programmatically

To set this up you would need to:

1. Install Sass: `npm install -g sass` or `brew install sass/sass/sass`
2. Create a `scss/` directory alongside `assets/`
3. Write your SCSS source files there
4. Compile to CSS with:

```jsx
   sass scss/main.scss ckanext/sdftheme/assets/style.css
```

1. Add a `package.json` with a watch script for development:

```jsx
   {
     "scripts": {
       "watch": "sass --watch scss/main.scss:ckanext/sdftheme/assets/style.css",
       "build": "sass scss/main.scss ckanext/sdftheme/assets/style.css --style=compressed"
     }
   }
```

Commit the compiled `style.css` to the repository so that users who clone the extension do not need to run a build step to use it.

### Other Improvements

- **Add i18n support** — translate any hardcoded strings in templates using `{{ _('...') }}`
- **Dark mode** — add a `@media (prefers-color-scheme: dark)` block using the existing CSS variables
- **Add a `CHANGES.md`** — track changes between versions as the theme evolves
- **Automated CSS build in CI** — add a GitHub Actions workflow to compile SCSS and fail if the compiled output is out of date

---

## Development

To work on the theme locally using Docker without rebuilding the image, copy updated files directly into the running container:

```jsx
# Copy updated CSS
docker compose -f docker-compose.dev.yml cp \
  src/ckanext-sdftheme/ckanext/sdftheme/assets/style.css \
  ckan-dev:/srv/app/src_extensions/ckanext-sdftheme/ckanext/sdftheme/assets/style.css
```

Then hard-refresh your browser (Cmd+Shift+R on Mac).

To override a template, copy it from CKAN core into the same relative path under `ckanext/sdftheme/templates/` and modify it there. Never edit CKAN core files directly.