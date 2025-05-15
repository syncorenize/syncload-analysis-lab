# Contributing to Syncload Analysis Lab

We’re excited to collaborate with you – whether you’re building your first notebook, improving docs, or adding advanced features.

---

## What you can contribute

- New Jupyter notebooks (e.g. latency trends, error heatmaps, endpoint performance)
- CLI tools (e.g. CSV summarizers, converters)
- Plugins (e.g. Grafana exporters, anomaly detection)
- Improved datasets, examples or visualizations
- Docs and improvements to this guide

---

## Getting started

1. **Fork this repo** on GitHub
2. Clone your fork and set up the environment:
   ```bash
   git clone https://github.com/YOUR-USERNAME/syncload-analysis-lab.git
   cd syncload-analysis-lab
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Make your changes in a new branch:
   ```bash
   git checkout -b feature/my-analysis-module

4. Run and test your code:

   - If you're using notebooks: run it cell-by-cell
   - If you're using CLI: document the usage
   - Follow the project style: readable, clean, documented


5. Commit and push your changes:
   ```bash
    git add .
    git commit -m "Add new latency heatmap notebook"
    git push origin feature/my-analysis-module
   
6. Create a pull request on GitHub

---

## Guidelines

- Prefer Python 3.8+, use venv for local environments
- Place notebooks in /notebooks, datasets in /datasets
- Keep code clean, commented, and focused
- Small PRs are welcome – even tiny fixes matter
- Be kind, constructive, and open to feedback

Feel free to open an issue at any time. 

By submitting a contribution, you agree that your work will be published under the MIT license.