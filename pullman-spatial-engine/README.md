# 🏡 Pullman Spatial Hedonic Valuation Engine

A high-performance production web service packaging high-dimensional econometric housing data for Pullman, WA. This system successfully bridges native econometric **R spatial frameworks** into production-ready **Python FastAPI endpoints** with full asynchronous data validation.

## 🛠️ System Architecture & Stack
- **Econometric Core:** R (Spatial Stats Stack: `spatialreg`, `spdep`)
- **Application Layer:** Python 3.11+, FastAPI (Async worker architecture)
- **Data Validation:** Pydantic v2 (Strict geospatial coordinate boundary constraint checking)

The architecture prevents runtime cross-contamination by running isolated sub-process calls directly to the R execution engine, parsing vector metrics into serialized JSON outputs in real time.

## 🚀 Quick Start & Deployment

### 1. System Requirements
Ensure you have `R` (with packages `spatialreg` and `spdep`) and `Python 3.11+` installed globally on your machine.

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com
cd pullman-spatial-engine

# Install Python production dependencies
pip install -r requirements.txt
```

### 3. Execution
Launch the FastAPI development cluster:
```bash
uvicorn app.main:app --reload
```
Navigate to `http://127.0.0` to interact with the auto-generated Swagger UI interactive documentation.

## 📊 Econometric Specification
The engine evaluates structural property configurations (X) adjusted for localized spatial lag matrices (W) simulating geographic spillover coefficients across Pullman neighborhoods, specifically mapping decaying distance parameters relative to the Washington State University campus core.
