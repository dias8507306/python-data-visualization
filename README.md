# Python Data Visualization (Matplotlib, Seaborn, Plotly, Mayavi)

Exercises from a *Data Visualization in Python* course. They go from Matplotlib basics to Seaborn statistical plots, interactive 3D Plotly figures and Mayavi scenes. One script is a mini analysis project that builds a synthetic ride-hailing dataset and produces 12 analysis charts.

## Contents

| Scripts | Topic |
|---|---|
| `03.py` … `03_6.py` | line plots, markers / styles, legends, subplots, `GridSpec` layouts |
| `04.py` | **mini project:** synthetic ride-booking dataset (1000 rides, generated with NumPy) and 12 charts: missing data, booking status, success by vehicle / hour / weekday, revenue distribution, revenue vs distance, revenue share, daily rides, heatmap, box plot, monthly trend (see `images/`) |
| `05.py` … `16.py` | text and annotations (`figtext`, titles, fonts, arrows / connection styles), axes, grids, layout |
| `17.py` … `30.py` | random-data plots, inset axes, colormaps and colorbars, bar / pie / scatter / histograms |
| `31.py` … `43.py` | **Seaborn** with public datasets (`mpg`, `flights`, `iris`, `penguins`, `tips`, `geyser`, `titanic`, `diamonds`): relational, categorical, distribution, regression plots, heatmaps, pair / joint plots |
| `44.py`, `45.py` | **Plotly** 3D: parametric spiral, scene, camera, axis and colorbar settings |
| `mayavi_chapter15.py`, `mayavi_diverse_plots.py` | **Mayavi** 3D: meshes, `quiver3d` vector fields, surfaces |

`images/` holds the 12 charts produced by `04.py`.

## Tech stack

Python 3 · Matplotlib · NumPy · pandas · Seaborn · Plotly · Mayavi (optional)

## How to run

```bash
python -m venv .venv && .venv/Scripts/activate      # Windows; on macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python scripts/03.py                   # opens a Matplotlib window
cd images && python ../scripts/04.py   # regenerates the 12 PNG charts into images/
```

The Seaborn scripts download the public example datasets from the seaborn-data repository on first run, so they need an internet connection. The Mayavi scripts need `pip install mayavi PyQt5` (VTK), which is easiest on Python 3.10/3.11.

> All data in this repository is randomly generated; brand names are anonymized. The other datasets are seaborn's public example datasets.

Author: Dias Ayazbay.

## Кратко (RU)

Сборник упражнений по визуализации данных на Python: Matplotlib, Seaborn, Plotly и Mayavi.
`04.py` генерирует синтетический набор данных и строит 12 аналитических графиков (в папке `images/`).
Скрипты Seaborn используют открытые демо-датасеты. Все остальные данные сгенерированы случайно.
