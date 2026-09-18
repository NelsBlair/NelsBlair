# Python-to-R execution bridge

# app/engine.py
import subprocess
import os

def run_spatial_prediction(sqft: float, bedrooms: int, bathrooms: float, age: int, latitude: float, longitude: float) -> float:
    """
    Executes the spatial hedonic pipeline by bridging the request to the native R runtime.
    """
    r_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../R/spatial_model.R"))
    
    r_command = f"""
    source('{r_script_path}')
    cat(predict_property_value({sqft}, {bedrooms}, {bathrooms}, {age}, {latitude}, {longitude}))
    """
    
    # Execute sub-process pipeline to extract computation
    process = subprocess.run(
        ["Rscript", "-e", r_command],
        capture_output=True,
        text=True,
        check=True
    )
    
    result_output = process.stdout.strip()
    if not result_output:
        raise RuntimeError("R engine returned empty response.")
        
    return float(result_output)
