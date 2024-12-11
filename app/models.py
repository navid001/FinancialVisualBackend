from app import db

class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(7), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    profit_margin = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'date': self.date,
            'year': self.year,
            'month': self.month,
            'cost': self.cost,
            'revenue': self.revenue,
            'profit': self.profit,
            'profit_margin': self.profit_margin
        }
