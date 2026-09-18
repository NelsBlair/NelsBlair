# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import subprocess
import os

app = FastAPI(
    title="Pullman Spatial Hedonic Valuation Engine",
    description="Production-grade API wrapping high-dimensional econometric spatial models for Pullman, WA.",
    version="1.0.0"
)

class PropertyFeatures(BaseModel):
    sqft: float = Field(..., gt=0, description="Total square footage of the property")
    bedrooms: int = Field(..., gt=0, description="Number of bedrooms")
    bathrooms: float = Field(..., gt=0, description="Number of bathrooms")
    age: int = Field(..., ge=0, description="Age of the property in years")
    latitude: float = Field(..., ge=46.70, le=46.76, description="Pullman Latitude bounds")
    longitude: float = Field(..., ge=-117.22, le=-117.10, description="Pullman Longitude bounds")

    model_config = {
        "json_schema_extra": {
            "example": {
                "sqft": 1850.0,
                "bedrooms": 3,
                "bathrooms": 2.5,
                "age": 12,
                "latitude": 46.7302,
                "longitude": -117.1691
            }
        }
    }

@app.post("/api/v1/valuate", response_model=dict)
async def valuate_property(features: PropertyFeatures):
    """
    Executes the spatial hedonic pipeline by bridging the request to the native R runtime.
    """
    try:
        # Construct isolated CLI command to invoke R script execution without runtime bloat
        r_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../R/spatial_model.R"))
        
        r_command = f"""
        source('{r_script_path}')
        cat(predict_property_value({features.sqft}, {features.bedrooms}, {features.bathrooms}, {features.age}, {features.latitude}, {features.longitude}))
        """
        
        # Execute sub-process pipeline to extract computation (R results)
        process = subprocess.run(
            ["Rscript", "-e", r_command],
            capture_output=True,
            text=True,
            check=True
        )
        
        result_output = process.stdout.strip()
        if not result_output:
            raise HTTPException(status_code=500, detail="R engine returned empty response.")
            
        predicted_value = float(result_output)
        
        return {
            "status": "success",
            "location_context": "Pullman, WA",
            "valuation": predicted_value,
            "currency": "USD"
        }
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"R spatial engine execution failed: {e.stderr}")
    except ValueError:
        raise HTTPException(status_code=500, detail="Failed to parse R engine response into mathematical float.")
