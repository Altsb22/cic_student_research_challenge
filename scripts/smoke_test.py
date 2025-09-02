#!/usr/bin/env python3
"""
smoke_test.py
Quick environment verification for:
"Mental Health, Economic Strain, and Vaccine Uptake During COVID-19:
 A Longitudinal, Data-Driven Story (2020–2023)"

What this does:
- Checks Python >= 3.13
- Prints key package versions (pandas, numpy, matplotlib, seaborn, statsmodels,
  scikit-learn, folium, branca, IPython, jupyterlab, ipykernel)
- Fits a tiny OLS and LASSO on synthetic data
- Saves a pairplot (PNG) and a folium map (HTML) into the output/ folder
"""

import sys
import os

REQUIRED_PY = (3, 13)

def fail(msg: str, code: int = 1):
    print(f"\n❌ {msg}")
    sys.exit(code)

def check_python():
    print("=== Python version check ===")
    print(sys.version)
    if sys.version_info < REQUIRED_PY:
        fail(f"Python {REQUIRED_PY[0]}.{REQUIRED_PY[1]}+ is required.")
    print("✅ Python version OK\n")

def safe_import(name, pip_hint=None):
    try:
        module = __import__(name)
        # Handle subpackages like statsmodels.api cleanly
        return module
    except ImportError:
        hint = f"Try installing with: pip install {pip_hint or name}"
        fail(f"Missing required package: {name}\n{hint}")

def print_versions():
    import importlib
    def ver(modname, label=None):
        try:
            m = importlib.import_module(modname)
            v = getattr(m, "__version__", "(no __version__)")
            print(f"{label or modname}: {v}")
        except Exception as e:
            print(f"{label or modname}: MISSING ({e.__class__.__name__})")

    print("=== Package versions ===")
    ver("pandas")
    ver("numpy")
    ver("matplotlib")
    ver("seaborn")
    ver("statsmodels")
    ver("sklearn", label="scikit-learn")
    ver("folium")
    ver("branca")
    ver("IPython")
    ver("jupyterlab")
    ver("ipykernel")
    print()

def run_smoke():
    # Imports (will raise if missing)
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    from sklearn.linear_model import LassoCV
    from sklearn.preprocessing import StandardScaler
    import folium
    from branca.colormap import linear

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # --- Synthetic dataset ---
    rng = np.random.default_rng(42)
    n = 120
    X = pd.DataFrame({
        "Tot_Pop": rng.normal(1_000_000, 200_000, n),
        "Mean_Unempl": rng.normal(5.5, 1.2, n),
        "Pov_Ad_Tot": rng.normal(10_000, 3_000, n),
        "Ad_Poor_MH_fourteen": rng.normal(12, 3, n),
    })
    beta = np.array([8e-5, -0.3, -1.5, 0.9])
    y = (X.values @ beta) + rng.normal(0, 1.0, n) + 50.0
    y = pd.Series(y, name="Cov_Vacc_one")

    # --- OLS ---
    Xc = sm.add_constant(X, has_constant="add")
    ols = sm.OLS(y, Xc).fit()
    print("=== OLS quick check ===")
    print(f"R^2: {ols.rsquared:.4f}")
    print("Params:")
    for k, v in ols.params.items():
        print(f"  {k:>22s} : {float(v): .6f}")
    print()

    # --- LASSO (standardized) ---
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    lasso = LassoCV(cv=5, random_state=42).fit(Xs, y)
    print("=== LASSO quick check ===")
    print(f"alpha: {float(lasso.alpha_):.6g}")
    print("coef (std-space):", [float(c) for c in lasso.coef_], "\n")

    # --- Pairplot ---
    sns.pairplot(pd.concat([X, y], axis=1), diag_kind="hist")
    pairplot_path = os.path.join("output", "smoke_pairplot.png")
    plt.savefig(pairplot_path, dpi=120, bbox_inches="tight")
    plt.close("all")
    print(f"✅ Saved pairplot to {pairplot_path}")

    # --- Folium map ---
    m = folium.Map(location=[37.8, -96], zoom_start=4, tiles="cartodbpositron")
    folium.Marker([38.5, -97.5], popup="Center Marker").add_to(m)
    colormap = linear.YlOrRd_09.scale(0, 100)
    colormap.caption = "Sample Color Scale"
    m.add_child(colormap)
    map_path = os.path.join("output", "smoke_map.html")
    m.save(map_path)
    print(f"✅ Saved folium map to {map_path}\n")

def main():
    check_python()

    # Ensure key libs are present before running (gives clearer errors)
    safe_import("pandas")
    safe_import("numpy")
    safe_import("matplotlib")
    safe_import("seaborn")
    safe_import("statsmodels")     # statsmodels.api used later
    safe_import("sklearn", "scikit-learn")
    safe_import("folium")
    safe_import("branca")
    safe_import("IPython")
    # jupyterlab/ipykernel are not required to *run* this script from terminal
    # but we include them in the version printout if present
    try:
        __import__("jupyterlab")
    except ImportError:
        pass
    try:
        __import__("ipykernel")
    except ImportError:
        pass

    print_versions()
    run_smoke()
    print("✅ Smoke test completed successfully.")

if __name__ == "__main__":
    main()
