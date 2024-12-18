from app import db
from app.models import FinancialData

# Dummy data for 5 years
dummy_data = [
    
    # 2019
    {"date": "2019-01", "year": 2019, "month": 1, "cost": 48000, "revenue": 65000, "profit": 17000, "profit_margin": 26.15},
    {"date": "2019-02", "year": 2019, "month": 2, "cost": 52000, "revenue": 71000, "profit": 19000, "profit_margin": 26.76},
    {"date": "2019-03", "year": 2019, "month": 3, "cost": 55000, "revenue": 78000, "profit": 23000, "profit_margin": 29.49},
    {"date": "2019-04", "year": 2019, "month": 4, "cost": 51000, "revenue": 73000, "profit": 22000, "profit_margin": 30.14},
    {"date": "2019-05", "year": 2019, "month": 5, "cost": 54000, "revenue": 76000, "profit": 22000, "profit_margin": 28.95},
    {"date": "2019-06", "year": 2019, "month": 6, "cost": 58000, "revenue": 82000, "profit": 24000, "profit_margin": 29.27},
    {"date": "2019-07", "year": 2019, "month": 7, "cost": 62000, "revenue": 89000, "profit": 27000, "profit_margin": 30.34},
    {"date": "2019-08", "year": 2019, "month": 8, "cost": 59000, "revenue": 85000, "profit": 26000, "profit_margin": 30.59},
    {"date": "2019-09", "year": 2019, "month": 9, "cost": 56000, "revenue": 79000, "profit": 23000, "profit_margin": 29.11},
    {"date": "2019-10", "year": 2019, "month": 10, "cost": 54000, "revenue": 75000, "profit": 21000, "profit_margin": 28.00},
    {"date": "2019-11", "year": 2019, "month": 11, "cost": 57000, "revenue": 81000, "profit": 24000, "profit_margin": 29.63},
    {"date": "2019-12", "year": 2019, "month": 12, "cost": 63000, "revenue": 92000, "profit": 29000, "profit_margin": 31.52},
    
    # 2020 
    {"date": "2020-01", "year": 2020, "month": 1, "cost": 52000, "revenue": 72000, "profit": 20000, "profit_margin": 27.78},
    {"date": "2020-02", "year": 2020, "month": 2, "cost": 54000, "revenue": 75000, "profit": 21000, "profit_margin": 28.00},
    {"date": "2020-03", "year": 2020, "month": 3, "cost": 45000, "revenue": 58000, "profit": 13000, "profit_margin": 22.41},
    {"date": "2020-04", "year": 2020, "month": 4, "cost": 42000, "revenue": 51000, "profit": 9000, "profit_margin": 17.65},
    {"date": "2020-05", "year": 2020, "month": 5, "cost": 44000, "revenue": 54000, "profit": 10000, "profit_margin": 18.52},
    {"date": "2020-06", "year": 2020, "month": 6, "cost": 48000, "revenue": 61000, "profit": 13000, "profit_margin": 21.31},
    {"date": "2020-07", "year": 2020, "month": 7, "cost": 51000, "revenue": 68000, "profit": 17000, "profit_margin": 25.00},
    {"date": "2020-08", "year": 2020, "month": 8, "cost": 53000, "revenue": 72000, "profit": 19000, "profit_margin": 26.39},
    {"date": "2020-09", "year": 2020, "month": 9, "cost": 55000, "revenue": 75000, "profit": 20000, "profit_margin": 26.67},
    {"date": "2020-10", "year": 2020, "month": 10, "cost": 56000, "revenue": 78000, "profit": 22000, "profit_margin": 28.21},
    {"date": "2020-11", "year": 2020, "month": 11, "cost": 58000, "revenue": 82000, "profit": 24000, "profit_margin": 29.27},
    {"date": "2020-12", "year": 2020, "month": 12, "cost": 61000, "revenue": 88000, "profit": 27000, "profit_margin": 30.68},
    
    # 2021 
    {"date": "2021-01", "year": 2021, "month": 1, "cost": 59000, "revenue": 85000, "profit": 26000, "profit_margin": 30.59},
    {"date": "2021-02", "year": 2021, "month": 2, "cost": 62000, "revenue": 89000, "profit": 27000, "profit_margin": 30.34},
    {"date": "2021-03", "year": 2021, "month": 3, "cost": 65000, "revenue": 94000, "profit": 29000, "profit_margin": 30.85},
    {"date": "2021-04", "year": 2021, "month": 4, "cost": 68000, "revenue": 98000, "profit": 30000, "profit_margin": 30.61},
    {"date": "2021-05", "year": 2021, "month": 5, "cost": 70000, "revenue": 102000, "profit": 32000, "profit_margin": 31.37},
    {"date": "2021-06", "year": 2021, "month": 6, "cost": 73000, "revenue": 107000, "profit": 34000, "profit_margin": 31.78},
    {"date": "2021-07", "year": 2021, "month": 7, "cost": 75000, "revenue": 112000, "profit": 37000, "profit_margin": 33.04},
    {"date": "2021-08", "year": 2021, "month": 8, "cost": 77000, "revenue": 115000, "profit": 38000, "profit_margin": 33.04},
    {"date": "2021-09", "year": 2021, "month": 9, "cost": 76000, "revenue": 113000, "profit": 37000, "profit_margin": 32.74},
    {"date": "2021-10", "year": 2021, "month": 10, "cost": 75000, "revenue": 111000, "profit": 36000, "profit_margin": 32.43},
    {"date": "2021-11", "year": 2021, "month": 11, "cost": 78000, "revenue": 116000, "profit": 38000, "profit_margin": 32.76},
    {"date": "2021-12", "year": 2021, "month": 12, "cost": 82000, "revenue": 124000, "profit": 42000, "profit_margin": 33.87},
    
    # 2022
    {"date": "2022-01", "year": 2022, "month": 1, "cost": 80000, "revenue": 120000, "profit": 40000, "profit_margin": 33.33},
    {"date": "2022-02", "year": 2022, "month": 2, "cost": 82000, "revenue": 123000, "profit": 41000, "profit_margin": 33.33},
    {"date": "2022-03", "year": 2022, "month": 3, "cost": 85000, "revenue": 128000, "profit": 43000, "profit_margin": 33.59},
    {"date": "2022-04", "year": 2022, "month": 4, "cost": 87000, "revenue": 131000, "profit": 44000, "profit_margin": 33.59},
    {"date": "2022-05", "year": 2022, "month": 5, "cost": 89000, "revenue": 135000, "profit": 46000, "profit_margin": 34.07},
    {"date": "2022-06", "year": 2022, "month": 6, "cost": 92000, "revenue": 140000, "profit": 48000, "profit_margin": 34.29},
    {"date": "2022-07", "year": 2022, "month": 7, "cost": 95000, "revenue": 145000, "profit": 50000, "profit_margin": 34.48},
    {"date": "2022-08", "year": 2022, "month": 8, "cost": 97000, "revenue": 148000, "profit": 51000, "profit_margin": 34.46},
    {"date": "2022-09", "year": 2022, "month": 9, "cost": 96000, "revenue": 146000, "profit": 50000, "profit_margin": 34.25},
    {"date": "2022-10", "year": 2022, "month": 10, "cost": 94000, "revenue": 143000, "profit": 49000, "profit_margin": 34.27},
    {"date": "2022-11", "year": 2022, "month": 11, "cost": 97000, "revenue": 148000, "profit": 51000, "profit_margin": 34.46},
    {"date": "2022-12", "year": 2022, "month": 12, "cost": 102000, "revenue": 157000, "profit": 55000, "profit_margin": 35.03},
    
    # 2023
    {"date": "2023-01", "year": 2023, "month": 1, "cost": 100000, "revenue": 155000, "profit": 55000, "profit_margin": 35.48},
    {"date": "2023-02", "year": 2023, "month": 2, "cost": 103000, "revenue": 160000, "profit": 57000, "profit_margin": 35.63},
    {"date": "2023-03", "year": 2023, "month": 3, "cost": 106000, "revenue": 165000, "profit": 59000, "profit_margin": 35.76},
    {"date": "2023-04", "year": 2023, "month": 4, "cost": 108000, "revenue": 168000, "profit": 60000, "profit_margin": 35.71},
    {"date": "2023-05", "year": 2023, "month": 5, "cost": 110000, "revenue": 172000, "profit": 62000, "profit_margin": 36.05},
    {"date": "2023-06", "year": 2023, "month": 6, "cost": 113000, "revenue": 177000, "profit": 64000, "profit_margin": 36.16},
    {"date": "2023-07", "year": 2023, "month": 7, "cost": 116000, "revenue": 182000, "profit": 66000, "profit_margin": 36.26},
    {"date": "2023-08", "year": 2023, "month": 8, "cost": 118000, "revenue": 185000, "profit": 67000, "profit_margin": 36.22},
    {"date": "2023-09", "year": 2023, "month": 9, "cost": 117000, "revenue": 183000, "profit": 66000, "profit_margin": 36.07},
    {"date": "2023-10", "year": 2023, "month": 10, "cost": 115000, "revenue": 180000, "profit": 65000, "profit_margin": 36.11},
    {"date": "2023-11", "year": 2023, "month": 11, "cost": 118000, "revenue": 185000, "profit": 67000, "profit_margin": 36.22},
    {"date": "2023-12", "year": 2023, "month": 12, "cost": 123000, "revenue": 194000, "profit": 71000, "profit_margin": 36.60}
]

def init_db():
    db.create_all()
    
    # Check if data already exists
    if FinancialData.query.first() is None:
        for entry in dummy_data:
            financial_entry = FinancialData(**entry)
            db.session.add(financial_entry)
        db.session.commit()
