# Learn Python – Scientific Computing

A hands-on Python course focused on scientific computing.  
Each folder covers one topic with runnable example scripts.

## Course Structure

| Folder | Topic | Scripts |
|--------|-------|---------|
| `01_basics/` | Python fundamentals | variables & types, control flow, functions |
| `02_numpy/` | NumPy | arrays, mathematical operations |
| `03_pandas/` | Pandas | DataFrames, data analysis |
| `04_matplotlib/` | Matplotlib | line plots, scatter, bar, histogram, subplots |
| `05_scipy/` | SciPy | statistics, integration, optimization, interpolation, signal processing |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/karimnorouzi/learnpython.git
cd learnpython
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run any example script

```bash
python 01_basics/01_variables_and_types.py
python 02_numpy/01_arrays.py
python 03_pandas/02_data_analysis.py
python 05_scipy/01_scientific_computing.py
```

> **Matplotlib scripts** save PNG files in the current directory (no display required).

## Prerequisites

- Python 3.10 or later
- pip

## License

This project is licensed under the GNU General Public License v3.0 – see [LICENSE](LICENSE) for details.
