# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.engine import run_spatial_prediction

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
    Endpoint to trigger the econometric spatial valuation.
    """
    try:
        predicted_value = run_spatial_prediction(
            sqft=features.sqft,
            bedrooms=features.bedrooms,
            bathrooms=features.bathrooms,
            age=features.age,
            latitude=features.latitude,
            longitude=features.longitude
        )
        
        return {
            "status": "success",
            "location_context": "Pullman, WA",
            "valuation": predicted_value,
            "currency": "USD"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
