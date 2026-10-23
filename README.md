# Deep Learning Notes

Student-friendly notes on the foundations of deep learning, with diagrams and plotted examples. The MkDocs Material site includes lessons on neural networks, activation functions, training, CNNs, transformers, diffusion, and flow matching.

## Preview locally

1. Install Python 3.10 or newer.
2. Install the project requirements:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the local website:

   ```bash
   python -m mkdocs serve
   ```

4. Open the local address printed by MkDocs (usually `http://127.0.0.1:8000/`).

To check the production build, run:

```bash
python -m mkdocs build --strict
```

The lesson source files are in [`docs/`](docs/), and the sidebar is configured in [`mkdocs.yml`](mkdocs.yml).
