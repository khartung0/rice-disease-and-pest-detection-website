# Rice research public website

Standalone public presentation repository. It has no dependency on, credentials for, or Git
history from the private research repository. All tracked content here is intended to be public.

## Local preview

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
python scripts/render_publication.py
.venv/Scripts/python -m mkdocs serve
```

Run `python scripts/render_publication.py` before `.venv/Scripts/python -m mkdocs build --strict`.
The renderer builds results/download pages from the release selected in `publication.json`.
The website checkout includes `publications/engineering-v1/`; a fresh bootstrap without bundles
must stage that release first. Generated `site/` and downloadable asset copies stay ignored.
The six short pages serve researchers and students; full-precision aggregates accompany the
D003 engineering example. Interactive Plotly charts remain a later addition.

## Connect the GitHub repository

The public remote is `https://github.com/khartung0/rice-disease-and-pest-detection-website.git`.
The local `origin` is configured and `site_url` points to
`https://khartung0.github.io/rice-disease-and-pest-detection-website/`.
The publishing branch is `main`. Pushes to it trigger the website build and deployment.

To publish subsequent content updates from this directory:

```powershell
git status --short
git add .
git commit -m "docs: update public research website"
git push -u origin main
```

In GitHub, set **Settings → Pages → Build and deployment → Source: GitHub Actions**.
Run **Actions → Publish website → Run workflow** on `main`. The first push may occur before
Pages is enabled; the manual run handles that. Future pushes to `main` build and deploy;
pull requests build only. The deployment job reports the website URL.

The workflow uses the public repository's built-in `GITHUB_TOKEN`; no private-repository token
or cross-repository credential is required. Hosting follows GitHub Pages' public-repository
plan rules. No custom domain or separately hosted Python app is needed.

## Content updates

Edit public narrative pages here. Import only reviewed, explicitly selected aggregate
publication bundles from the research workflow. Select a later release in `publication.json`
only after its matching content/renderer is ready. Do not mirror the
private repository or copy its complete `docs/`, `.git/`, experiments, manifests, or raw data.
The bootstrap template is not a synchronization mechanism and must not overwrite this repo.
`docs/results.md` and `docs/downloads.md` are generated: edit their renderer or source bundle,
not those tables by hand. Narrative pages are edited normally. CI renders before building.
