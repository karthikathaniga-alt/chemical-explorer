from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Backend is working!"}


@app.get("/hello")
def say_hello():
    return {"message": "Hello from chemical Explorer"}



chemicals = [
    {
        "name": "Helium",
        "formula": "He",
        "molar_mass": "4.00 g/mol",
        "density": "0.18 g/L",
        "melting_point": "-272 °C",
        "boiling_point": "-269 °C",
        "heat_capacity": "5.19 J/g°C"
            
    },
    {
        "name": "Water",
        "formula": "H2O",
        "molar_mass": "18.02 g/mol",
        "density": "1.00 g/cm³",
        "boiling_point": "100 °C",
        "melting_point": "0 °C",
        "heat_capacity": "4.18 J/g·°C" 
    },
    {
        "name": "Sodium Chloride",
        "formula": "NaCl",
        "molar_mass": "58.44 g/mol",
        "density": "2.16 g/cm3",
        "melting_point": "801 °C",
        "boiling_point": "1465 °C",
        "heat_capacity": "0.86 J/g°C"
    },

    {
        "name": "Carbon Dioxide",
        "formula": "CO2",
        "molar_mass": "44.01 g/mol",
        "density": "1.98 g/L",
        "melting_point": "-56.6 °C",
        "boiling_point": "-78.5 °C",
        "heat_capacity": "0.84 J/g°C"
    },

    {
        "name": "Ammonia",
        "formula": "NH3",
        "molar_mass": "17.03 g/mol",
        "density": "0.73 g/L",
        "melting_point": "-77.7 °C",
        "boiling_point": "-33.3 °C",
        "heat_capacity": "2.06 J/g°C"
    },

    {
        "name": "Methane",
        "formula": "CH4",
        "molar_mass": "16.04 g/mol",
        "density": "0.66 g/L",
        "melting_point": "-182.5 °C",
        "boiling_point": "-161.5 °C",
        "heat_capacity": "2.20 J/g°C"
    },

    {
        "name": "Oxygen",
        "formula": "O2",
        "molar_mass": "32.00 g/mol",
        "density": "1.43 g/L",
        "melting_point": "-219 °C",
        "boiling_point": "-183 °C",
        "heat_capacity": "0.92 J/g°C"
    },

    {
        "name": "Hydrogen",
        "formula": "H2",
        "molar_mass": "2.02 g/mol",
        "density": "0.09 g/L",
        "melting_point": "-259 °C",
        "boiling_point": "-253 °C",
        "heat_capacity": "14.30 J/g°C"
    },

    {
        "name": "Nitrogen",
        "formula": "N2",
        "molar_mass": "28.01 g/mol",
        "density": "1.25 g/L",
        "melting_point": "-210 °C",
        "boiling_point": "-196 °C",
        "heat_capacity": "1.04 J/g°C"
    },

    {
        "name": "Iron",
        "formula": "Fe",
        "molar_mass": "55.85 g/mol",
        "density": "7.87 g/cm3",
        "melting_point": "1538 °C",
        "boiling_point": "2862 °C",
        "heat_capacity": "0.45 J/g°C"
    },

    {
        "name": "Copper",
        "formula": "Cu",
        "molar_mass": "63.55 g/mol",
        "density": "8.96 g/cm3",
        "melting_point": "1085 °C",
        "boiling_point": "2562 °C",
        "heat_capacity": "0.39 J/g°C"
    },
    {
        "name": "Ethanol",
        "formula": "C2H5OH",
        "molar_mass": "46.07 g/mol",
        "density": "0.789 g/cm3",
        "melting_point": "-114.1 °C",
        "boiling_point": "78.37 °C",
        "heat_capacity": "2.44 J/g°C"
    },

    {
        "name": "Benzene",
        "formula": "C6H6",
        "molar_mass": "78.11 g/mol",
        "density": "0.876 g/cm3",
        "melting_point": "5.5 °C",
        "boiling_point": "80.1 °C",
        "heat_capacity": "1.74 J/g°C"
    },

    {
        "name": "Acetic Acid",
        "formula": "CH3COOH",
        "molar_mass": "60.05 g/mol",
        "density": "1.049 g/cm3",
        "melting_point": "16.6 °C",
        "boiling_point": "118.1 °C",
        "heat_capacity": "2.05 J/g°C"
    },

    {
        "name": "Sulfuric Acid",
        "formula": "H2SO4",
        "molar_mass": "98.08 g/mol",
        "density": "1.84 g/cm3",
        "melting_point": "10 °C",
        "boiling_point": "337 °C",
        "heat_capacity": "1.38 J/g°C"
    }

]
@app.get("/chemicals")
def get_chemicals():    
     return chemicals

@app.get("/chemical/name/{name}")
def search_by_name(name: str):

    for chemical in chemicals:

        if name.lower() in chemical["name"].lower():
            return chemical

    return {"message": "Chemical not found"}

@app.get("/chemical/formula/{formula}")
def search_by_formula(formula: str):

    for chemical in chemicals:

        if chemical["formula"].lower() == formula.lower():
            return chemical

    return {"message": "Formula not found"}




