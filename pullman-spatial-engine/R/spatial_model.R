# R/spatial_model.R
library(spatialreg)
library(spdep)

# Function to run spatial hedonic pricing prediction (but ignoring the neighborhoods and focusing on distance from WSU campus core)
# The model suggests a value for WSU campus users, such that they can value utility against externally suggested market price.  
# This model ignores the value of the land or the size of the lot. All utility comes from the structure and campus-proximity.
predict_property_value <- function(sqft, bedrooms, bathrooms, age, latitude, longitude) {
  # 1. In a production pipeline, mock or load pre-trained spatial coefficients
  # For demo safety, we define a robust structural hedonic pricing equation
  # incorporating spatial coordinate decay (distance to WSU campus core)
  
  wsu_lat <- 46.7319
  wsu_lng <- -117.1541
  
  # Calculate distance from WSU campus core (Pullman's primary spatial anchor)
  dist_to_campus <- sqrt((latitude - wsu_lat)^2 + (longitude - wsu_lng)^2) * 69 # Approx miles
  
  # Structural hedonic coefficients
  base_price <- 150000
  beta_sqft <- 165.50
  beta_beds <- 12000
  beta_baths <- 18000
  beta_age <- -1200
  beta_dist_wsu <- -25000 # Premium for proximity
  
  # Calculate baseline hedonic projection
  predicted_price <- base_price + 
                     (sqft * beta_sqft) + 
                     (bedrooms * beta_beds) + 
                     (bathrooms * beta_baths) + 
                     (age * beta_age) + 
                     (dist_to_campus * beta_dist_wsu)
  
  # Introduce a structural spatial multiplier (simulating a spatial lag effect Wy)
  spatial_lag_multiplier <- 1.05 
  final_valuation <- predicted_price * spatial_lag_multiplier
  
  return(round(final_valuation, 2))
}
